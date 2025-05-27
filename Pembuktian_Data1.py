import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

#ambil kolom research dan total saja
df = pd.read_excel('DATASET/AI_INDEX.xlsx', usecols='E,I', nrows=63)
df.columns = ['research', 'total']

x = df['research']
y = df['total']

x_with_const = sm.add_constant(x)  # tambah konstanta intercept
model = sm.OLS(y, x_with_const).fit()

#buat prediksi garis regresi
y_pred = model.predict(x_with_const)

#visualisasi scatter plot dan garis regresi linear dan pengaturan lainnya
plt.scatter(x, y, label='Data Aktual')
plt.plot(x, y_pred, color='red', label='Garis Regresi')
plt.xlabel('Research')
plt.ylabel('Total')
plt.title('Visualisasi Regresi Linear Research vs Total')
plt.legend()
plt.show()
