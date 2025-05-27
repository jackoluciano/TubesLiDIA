# IMPOR MODUL

import pandas as pd

# IMPOR DATA

data1 = pd.read_excel("D:/TUGAS LIDIA/DATASET/AI_VIBRANCY.xlsx", na_values=["-"])
print(data1)

# KAMUS DATA

menu= ["private_investment", "number_of_newly_funded_companies", "number_of_total_journal_publications", 
       "number_of_total_conference_publications", "number_of_total_repository_publications", "number_of_total_journal_citations",
       "number_of_total_conference_citations", "number_of_total_repository_citations", "number_of_total_patent_fillings",
       "number_of_total_patent_grants",	"year_h_index", "relative_ai_skill_pen", "ai_talent_concentration",	"norm_private_investment",
       "norm_number_of_newly_funded_companies",	"norm_number_of_total_journal_publications", "norm_number_of_total_conference_publications",
       "norm_number_of_total_repository_publications", "norm_number_of_total_journal_citations", "norm_number_of_total_conference_citations",
       "norm_number_of_total_repository_citations", "norm_number_of_total_patent_fillings", "norm_number_of_total_patent_grants", 
       "norm_year_h_index", "norm_relative_ai_skill_pen", "norm_ai_talent_concentration", "econ_pillar", "rd_pillar", "vibrancy"]

percentile= [10,25,50,75,90]

print("")

# RATA-RATA DAN STANDAR DEVIASI
print("RATA-RATA DAN STANDAR DEVIASI")
print(f"{'Atribut':<45} | {'Rata-rata':>12} | {'Standar Deviasi':>15}")
print("-" * 78)
for i in range(29):
    rata2 = data1[menu[i]].mean()
    std = data1[menu[i]].std()
    if i != 0:
        print(f"{menu[i]:<45} | {rata2:>12.2f} | {std:>15.2f}")
    else:
        print(f"{menu[i]:<45} | {rata2/1000:>11.2f}k | {std/1000:>14.2f}k")
print("")

# PERSENTIL
print("PERSENTIL")
print(f"{'Atribut':<45} | {'P10':>10} | {'P25':>10} | {'P50':>10} | {'P75':>10} | {'P90':>10}")
print("-" * 110)
for i in range(29):
    p10 = data1[menu[i]].quantile(0.10)
    p25 = data1[menu[i]].quantile(0.25)
    p50 = data1[menu[i]].quantile(0.50)
    p75 = data1[menu[i]].quantile(0.75)
    p90 = data1[menu[i]].quantile(0.90)
    if i != 0:
        print(f"{menu[i]:<45} | {p10:>10.2f} | {p25:>10.2f} | {p50:>10.2f} | {p75:>10.2f} | {p90:>10.2f}")
    else:
        print(f"{menu[i]:<45} | {p10/1000:>9.2f}k | {p25/1000:>9.2f}k | {p50/1000:>9.2f}k | {p75/1000:>9.2f}k | {p90/1000:>9.2f}k")
print("")

# MAKSIMUM DAN MINIMUM
print("MAKSIMUM DAN MINIMUM")
print(f"{'Atribut':<45} | {'Maksimum':>12} | {'Minimum':>10}")
print("-" * 73)
for i in range(29):
    maksimum = data1[menu[i]].max()
    minimum = data1[menu[i]].min()
    if i != 0:
        print(f"{menu[i]:<45} | {maksimum:>12.2f} | {minimum:>10.2f}")
    else:
        print(f"{menu[i]:<45} | {maksimum/1000:>11.2f}k | {minimum:>10.2f}")
print("")

# DISTRIBUSI FREKUENSI DATA

print("DISTRIBUSI FREKUENSI")
for i in range(29):
    print(data1[menu[i]].value_counts())
    print("")
print("")