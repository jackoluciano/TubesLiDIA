import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

#NaN handling
df = pd.read_excel("DATASET/AI_VIBRANCY.xlsx", usecols="C:O,AE", nrows=146, na_values=["-"])

df.columns = [
    "private_investment",
    "number_of_newly_funded_companies",
    "number_of_total_journal_publications",
    "number_of_total_conference_publications",
    "number_of_total_repository_publications",
    "number_of_total_journal_citations",
    "number_of_total_conference_citations",
    "number_of_total_repository_citations",
    "number_of_total_patent_fillings",
    "number_of_total_patent_grants",
    "year_h_index",
    "relative_ai_skill_pen",
    "ai_talent_concentration",
    "vibrancy"  #dependent variable
]

independent_cols = df.columns[:-1]  #semua kecuali kolom terakhir

for col in independent_cols:
    x = df[col]
    y = df["vibrancy"]

    # drop NaN agar tidak error
    valid_data = pd.concat([x, y], axis=1).dropna()
    x_valid = sm.add_constant(valid_data[col])
    y_valid = valid_data["vibrancy"]

    model = sm.OLS(y_valid, x_valid).fit()

    print(f"Regresi {col} -> vibrancy")
    print(model.summary())
    print('-' * 80)
