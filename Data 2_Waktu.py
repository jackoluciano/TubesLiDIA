from matplotlib import pyplot as plt 

import numpy as np

import pandas as pd

data = pd.read_csv("AI VIBRANCY.csv")



# Diambil 5 negara unggul untuk divisualisasi
negara = ['united states', 'china', 'india', 'canada', 'united kingdom']
data = data[data['country'].str.lower().isin(negara)]
data = data.sort_values(by='year')

plt.figure(figsize=(12, 6))
for i in negara:
    data_negara = data[data['country'].str.lower() == i]
    plt.plot(data_negara['year'], data_negara['private_investment'], label=i.title())

plt.xlabel('Year')
plt.ylabel('Investment (Milyar dalam USD)')
plt.title('Private Investment in AI from 2017 until 2021')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# Diambil 5 negara unggul untuk divisualisasi
negara = ['united states', 'china', 'india', 'canada', 'united kingdom']
data = data[data['country'].str.lower().isin(negara)]
data = data.sort_values(by='year')

plt.figure(figsize=(12, 6))
for i in negara:
    data_negara = data[data['country'].str.lower() == i]
    plt.plot(data_negara['year'], data_negara['number_of_newly_funded_companies'], label=i.title())

plt.xlabel('Year')
plt.ylabel('Number of Companies')
plt.title('Newly Funded AI Companies from 2017 until 2021')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



# Diambil 5 negara unggul untuk divisualisasi
negara = ['united states', 'china', 'india', 'canada', 'united kingdom']
data = data[data['country'].str.lower().isin(negara)]
data = data.sort_values(by='year')

plt.figure(figsize=(12, 6))
for i in negara:
    data_negara = data[data['country'].str.lower() == i]
    plt.plot(data_negara['year'], data_negara['number_of_total_patent_fillings'], label=i.title())

plt.xlabel('Year')
plt.ylabel('Patent Fillings')
plt.title('Patent Fillings in from 2017 until 2021')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()




# Diambil 5 negara unggul untuk divisualisasi
negara = ['united states', 'china', 'india', 'canada', 'united kingdom']
data = data[data['country'].str.lower().isin(negara)]
data = data.sort_values(by='year')

plt.figure(figsize=(12, 6))
for i in negara:
    data_negara = data[data['country'].str.lower() == i]
    plt.plot(data_negara['year'], data_negara['number_of_total_patent_grants'], label=i.title())

plt.xlabel('Year')
plt.ylabel('Patent Grants')
plt.title('Patent Grants in AI from 2017 until 2021')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()