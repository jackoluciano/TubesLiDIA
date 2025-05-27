# IMPOR MODUL

import pandas as pd

# IMPOR DATA

data1 = pd.read_excel("DATASET/AI_INDEX.xlsx")
print(data1)

# KAMUS DATA

menu= ["Talent", "Infrastructure", "Operating Environment", "Research", "Development", "Government Strategy", 
       "Commercial", "Total score", "Region", "Cluster", "Income group", "Political regime"]

percentile= [10,25,50,75,90]

# MENGHITUNG RATA RATA DAN STANDAR DEVIASI

print("")
print("RATA-RATA DAN STANDAR DEVIASI")

print(f"{'Atribut':<25} | {'Rata-rata':>12} | {'Standar Deviasi':>18}")
print("-" * 62)
for i in range(8):
    rata2 = data1[menu[i]].mean()
    std = data1[menu[i]].std()
    print(f"{menu[i]:<25} | {rata2:>12.2f} | {std:>18.2f}")

print("")

# MENGHITUNG PERSENTIL

print("PERSENTIL")

print(f"{'Atribut':<25} | {'10%':>5} | {'25%':>5} | {'50%':>5} | {'75%':>5} | {'90%':>5}")
print("-" * 65)
for i in range(8):
    print(f"{menu[i]:<25} |", end="")
    for y in range(5):
        persentil_val = data1[menu[i]].quantile(percentile[y]/100)
        if y!= 4:
            print(f" {persentil_val:>5.2f} |", end="")
        else:
            print(f" {persentil_val:>5.2f}", end="")
    print("")

print("")

# MENCARI NILAI MAKSIMUM DAN MINIMUM

print("MAKSIMUM DAN MINIMUM")

print(f"{'Atribut':<25} | {'Maksimum':<10} | {'Minimum':<10}")
print("-" * 50)
for i in range(8):
    maks = data1[menu[i]].max()
    mins = data1[menu[i]].min()
    print(f"{menu[i]:<25} | {maks:<10.2f} | {mins:<10.2f}")
print("")

# DISTRIBUSI FREKUENSI DATA

print("DISTRIBUSI FREKUENSI")
for i in range(12):
    print(data1[menu[i]].value_counts())
    print("")
print("")