from matplotlib import pyplot as plt 

import numpy as np
import pandas as pd

data = pd.read_excel("DATASET/AI_VIBRANCY.xlsx")

#1
data_2021 = data[data['year'] == 2021]
countries = data_2021['country']
new_funded = data_2021['number_of_newly_funded_companies']

x = np.arange(0, len(countries))
width = 0.9

plt.figure(figsize=(16, 6))
plt.bar(x, new_funded, width=width, label='Newly Funded Companies')                                    

plt.xticks(x, countries, rotation=90)
plt.xlabel('Country')
plt.ylabel('Value')
plt.title('Total of Newly Funded Companies by Country in 2021')
plt.legend()
plt.tight_layout()
plt.show()



#2
data_2021 = data[data['year'] == 2021]
journals = data_2021['number_of_total_journal_publications']
conferences = data_2021['number_of_total_conference_publications']
repositories = data_2021['number_of_total_repository_publications']

x = np.arange(0, len(countries) * 1.7, 1.7)
width = 0.5

plt.figure(figsize=(14, 6))
plt.bar(x - width, journals, width, label='Journal Publications')
plt.bar(x, conferences, width, label='Conference Publications')
plt.bar(x + width, repositories, width, label='Repository Publications')

plt.xticks(x, countries, rotation=90)
plt.xlabel('Country')
plt.ylabel('Number of Publications')
plt.title('AI Publications by Type per Country in 2021')
plt.legend()
plt.tight_layout()
plt.show()



#3
data_2021 = data[data['year'] == 2021]
fillings = data_2021['number_of_total_patent_fillings']
grants = data_2021['number_of_total_patent_grants']

x = np.arange(0, len(countries) * 1.7, 1.7)
width = 0.7

plt.figure(figsize=(14, 6))
plt.bar(x - width/2, fillings, width, label='Patent Fillings')
plt.bar(x + width/2, grants, width, label='Patent Grants')

plt.xticks(x, countries, rotation=90)
plt.xlabel('Country')
plt.ylabel('Number of Patents')
plt.title('Patent Fillings vs Patent Grants by Country in 2021')
plt.legend()
plt.tight_layout()
plt.show()