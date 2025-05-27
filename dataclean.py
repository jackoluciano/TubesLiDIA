import pandas as pd

# Membaca data dari file Excel
file_path = "DATASET/AI_INDEX.xlsx"
data = pd.read_excel(file_path, sheet_name="Worksheet")

# 1. Cek duplikasi dan hapus jika ada
print(f"Jumlah baris sebelum hapus duplikasi: {len(data)}")
data = data.drop_duplicates()
print(f"Jumlah baris setelah hapus duplikasi: {len(data)}")

# 2. Cek missing values dan tangani (jika ada)
print("\nMissing values per kolom sebelum penanganan:")
print(data.isnull().sum())

# Contoh penanganan: jika ada missing values, isi dengan median kolom (khusus numerik)
for col in data.select_dtypes(include='number').columns:
    if data[col].isnull().sum() > 0:
        median_value = data[col].median()
        data[col].fillna(median_value, inplace=True)

print("\nMissing values per kolom setelah penanganan:")
print(data.isnull().sum())

# 3. Cek nilai nol di kolom numerik dan ganti dengan median jika dianggap perlu
print("\nJumlah nilai nol di kolom numerik sebelum penanganan:")
for col in data.select_dtypes(include='number').columns:
    count_zero = (data[col] == 0).sum()
    print(f"{col}: {count_zero}")

# Contoh: ganti nilai nol dengan median (jika nol dianggap invalid)
for col in data.select_dtypes(include='number').columns:
    count_zero = (data[col] == 0).sum()
    if count_zero > 0:
        median_value = data[col].median()
        data.loc[data[col] == 0, col] = median_value

print("\nJumlah nilai nol di kolom numerik setelah penanganan:")
for col in data.select_dtypes(include='number').columns:
    count_zero = (data[col] == 0).sum()
    print(f"{col}: {count_zero}")

# 4. Tampilkan info data setelah pembersihan
print("\nInformasi data setelah cleansing:")
print(data.info())

# Simpan data yang sudah dibersihkan ke file baru
data.to_excel("DATASETBARU/AI_INDEX_cleaned.xlsx", index=False)
print("\nData telah dibersihkan dan disimpan ke 'AI_INDEX_cleaned.xlsx'")
