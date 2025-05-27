from matplotlib import pyplot as plt

import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler

data = pd.read_excel("DATASET/AI_VIBRANCY.xlsx")

# 1. Karena nilainya sangat besar dan timpang, gunakan log agar distribusi lebih merata
data['log_patent_fillings'] = np.log1p(data['number_of_total_patent_fillings'])
data['log_patent_grants'] = np.log1p(data['number_of_total_patent_grants'])

# 2. Karena range sangat besar dan tidak seragam, gunakan normalisasi Min-Max
scaler = MinMaxScaler()
data[['journal_norm', 'conference_norm', 'repository_norm']] = scaler.fit_transform(
    data[[
        'number_of_total_journal_publications',
        'number_of_total_conference_publications',
        'number_of_total_repository_publications'
    ]]
)

data['log_patent_fillings'] = np.log1p(data['number_of_total_patent_fillings'])
data['log_patent_grants'] = np.log1p(data['number_of_total_patent_grants'])
