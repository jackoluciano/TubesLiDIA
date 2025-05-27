import pandas as pd

file_path = "DATASET/AI_VIBRANCY.xlsx"

# Cek sheet yang ada
xls = pd.ExcelFile(file_path)
print("Sheet yang ada:", xls.sheet_names)

# Baca sheet 'Data Utama'
data = pd.read_excel(file_path, sheet_name="Worksheet")

print(data.info())
print(data.isnull().sum())
print("Jumlah baris duplikat:", data.duplicated().sum())
print(data.dtypes)
print(data.describe())

for col in data.select_dtypes(include='float64').columns:
    zero_count = (data[col] == 0).sum()
    print(f"Kolom {col} memiliki {zero_count} nilai 0 dari total {len(data)} data")

