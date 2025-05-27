import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.read_excel('D:/TUGAS LIDIA/DATASET/AI_VIBRANCY.xlsx', nrows=146)

x = df['number_of_newly_funded_companies']
y = df['vibrancy']

#hapus baris yang ada NaN
mask = x.notna() & y.notna()
x = x[mask]
y = y[mask]

x_with_const = sm.add_constant(x)
model = sm.OLS(y, x_with_const).fit()
y_pred = model.predict(x_with_const)

#visualisasi dan pengaturan lainnya
plt.scatter(x, y, label='Data Aktual')
plt.plot(x, y_pred, color='red', label='Garis Regresi')
plt.xlabel('Number of Newly Funded Companies')
plt.ylabel('Vibrancy')
plt.title('Regresi Linear: New Funded Companies vs Vibrancy')
plt.legend()
plt.show()
