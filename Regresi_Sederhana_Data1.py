import pandas as pd
import statsmodels.api as sm

df = pd.read_excel('DATASET/AI_INDEX.xlsx', usecols='B:I', nrows=63)
df.columns = ['talent', 'infrastructure', 'operating', 'research', 'development', 'government', 'commercial', 'total']  #nama kolom eksplisit

columns = df.columns.tolist()  #ambil semua nama kolom untuk perbandingan berpasangan

for i in range(len(columns)):
    for j in range(i+1, len(columns)):  #hindari duplikat dan regresi diri sendiri
        x = df[columns[i]]
        y = df[columns[j]]

        x_with_const = sm.add_constant(x)  #menambahkan konstanta agar regresi punya intercept
        model = sm.OLS(y, x_with_const).fit()

        print(f'Regresi {columns[i]} -> {columns[j]}')  #output arah regresi
        print(model.summary()) #hasil regresi secara statistik
        print('-' * 80)