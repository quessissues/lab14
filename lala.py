from google.colab import drive
drive.mount('/content/drive')


import pandas as pd
import pyreadstat

data = pd.read_spss('/content/drive/MyDrive/lab 12/KAZ_2014_FIES_v01_EN_M_v01_A_OCS (1).sav')

data.to_excel('KZ-2014.xlsx')

data1 = pd.read_spss('/content/drive/MyDrive/lab 12/KAZ_2015_FIES_v01_EN_M_v01_A_OCS (1).sav')
data1.to_excel('KZ-2015.xlsx')

data2 = pd.read_spss('/content/drive/MyDrive/lab 12/KAZ_2016_FIES_v01_EN_M_v01_A_OCS (1).sav')
data2.to_excel('KZ-2016.xlsx')

data3 = pd.read_spss('/content/drive/MyDrive/lab 12/KAZ_2017_FIES_v01_EN_M_v01_A_OCS (1).sav')
data3.to_excel('KZ-2017.xlsx')

data_kgz = pd.read_spss('/content/drive/MyDrive/lab 12/KGZ_2014_FIES_v01_EN_M_v01_A_OCS (1).sav')
data_kgz.to_excel('KGZ-2014.xlsx')

data_kgz1 = pd.read_spss('/content/drive/MyDrive/lab 12/KGZ_2015_FIES_v01_EN_M_v01_A_OCS (1).sav')
data_kgz1.to_excel('KGZ-2015.xlsx')

data_kgz2 = pd.read_spss('/content/drive/MyDrive/lab 12/KGZ_2016_FIES_v01_EN_M_v01_A_OCS (1).sav')
data_kgz2.to_excel('KGZ-2016.xlsx')

data_kgz3 = pd.read_spss('/content/drive/MyDrive/lab 12/KGZ_2017_FIES_v01_EN_M_v01_A_OCS (1).sav')
data_kgz3.to_excel('KGZ-2017.xlsx')

data_tjk = pd.read_spss('/content/drive/MyDrive/lab 12/TJK_2014_FIES_v01_EN_M_v01_A_OCS (1).sav')
data_tjk.to_excel('TJK-2014.xlsx')

data_tjk1 = pd.read_spss('/content/drive/MyDrive/lab 12/TJK_2015_FIES_v01_EN_M_v01_A_OCS (1).sav')
data_tjk1.to_excel('TJK-2015.xlsx')

data_tjk2 = pd.read_spss('/content/drive/MyDrive/lab 12/TJK_2016_FIES_v01_EN_M_v01_A_OCS (1).sav')
data_tjk2.to_excel('TJK-2016.xlsx')

data_tjk3 = pd.read_spss('/content/drive/MyDrive/lab 12/TJK_2017_FIES_v01_EN_M_v01_A_OCS (1).sav')
data_tjk3.to_excel('TJK-2017.xlsx')

data_uzb = pd.read_spss('/content/drive/MyDrive/lab 12/UZB_2014_FIES_v01_EN_M_v01_A_OCS (1).sav')
data_uzb.to_excel('UZB-2014.xlsx')

data_uzb1 = pd.read_spss('/content/drive/MyDrive/lab 12/UZB_2015_FIES_v01_EN_M_v01_A_OCS (1).sav')
data_uzb1.to_excel('UZB-2015.xlsx')

data_uzb2 = pd.read_spss('/content/drive/MyDrive/lab 12/UZB_2016_FIES_v01_EN_M_v01_A_OCS (1).sav')
data_uzb2.to_excel('UZB-2016.xlsx')

data_uzb3 = pd.read_spss('/content/drive/MyDrive/lab 12/UZB_2017_FIES_v01_EN_M_v01_A_OCS (2).sav')
data_uzb3.to_excel('UZB-2017.xlsx')

import numpy as np

df_KGZ_2014 = pd.read_excel('/content/drive/MyDrive/lab 12 excel/KGZ-2014.xlsx')
df_KGZ_2014.fillna(0, inplace=True)
df_KGZ_2014.to_excel('/content/drive/MyDrive/lab 12 excel/KGZ-2014.xlsx', index=False)

df_KGZ_2015 = pd.read_excel('/content/drive/MyDrive/lab 12 excel/KGZ-2015.xlsx')
df_KGZ_2015.fillna(0, inplace=True)
df_KGZ_2015.to_excel('/content/drive/MyDrive/lab 12 excel/KGZ-2015.xlsx', index=False)

df_KGZ_2016 = pd.read_excel('/content/drive/MyDrive/lab 12 excel/KGZ-2016.xlsx')
df_KGZ_2016.fillna(0, inplace=True)
df_KGZ_2016.to_excel('/content/drive/MyDrive/lab 12 excel/KGZ-2016.xlsx', index=False)

df_KGZ_2017 = pd.read_excel('/content/drive/MyDrive/lab 12 excel/KGZ-2017.xlsx')
df_KGZ_2017.fillna(0, inplace=True)
df_KGZ_2017.to_excel('/content/drive/MyDrive/lab 12 excel/KGZ-2017.xlsx', index=False)

df_KZ_2014 = pd.read_excel('/content/drive/MyDrive/lab 12 excel/KZ-2014.xlsx')
df_KZ_2014.fillna(0, inplace=True)
df_KZ_2014.to_excel('/content/drive/MyDrive/lab 12 excel/KZ-2014.xlsx', index=False)

df_KZ_2015 = pd.read_excel('/content/drive/MyDrive/lab 12 excel/KZ-2015.xlsx')
df_KZ_2015.fillna(0, inplace=True)
df_KZ_2015.to_excel('/content/drive/MyDrive/lab 12 excel/KZ-2015.xlsx', index=False)

df_KZ_2016 = pd.read_excel('/content/drive/MyDrive/lab 12 excel/KZ-2016.xlsx')
df_KZ_2016.fillna(0, inplace=True)
df_KZ_2016.to_excel('/content/drive/MyDrive/lab 12 excel/KZ-2016.xlsx', index=False)

df_KZ_2017 = pd.read_excel('/content/drive/MyDrive/lab 12 excel/KZ-2017.xlsx')
df_KZ_2017.fillna(0, inplace=True)
df_KZ_2017.to_excel('/content/drive/MyDrive/lab 12 excel/KZ-2017.xlsx', index=False)

df_tjk_2014 = pd.read_excel('/content/drive/MyDrive/lab 12 excel/TJK-2014.xlsx')
df_tjk_2014.fillna(0, inplace=True)
df_tjk_2014.to_excel('/content/drive/MyDrive/lab 12 excel/TJK-2014.xlsx', index=False)

df_tjk_2015 = pd.read_excel('/content/drive/MyDrive/lab 12 excel/TJK-2015.xlsx')
df_tjk_2015.fillna(0, inplace=True)
df_tjk_2015.to_excel('/content/drive/MyDrive/lab 12 excel/TJK-2015.xlsx', index=False)

df_tjk_2016 = pd.read_excel('/content/drive/MyDrive/lab 12 excel/TJK-2016.xlsx')
df_tjk_2016.fillna(0, inplace=True)
df_tjk_2016.to_excel('/content/drive/MyDrive/lab 12 excel/TJK-2016.xlsx', index=False)

df_tjk_2017 = pd.read_excel('/content/drive/MyDrive/lab 12 excel/TJK-2017.xlsx')
df_tjk_2017.fillna(0, inplace=True)
df_tjk_2017.to_excel('/content/drive/MyDrive/lab 12 excel/TJK-2017.xlsx', index=False)

df_uzb_2014 = pd.read_excel('/content/drive/MyDrive/lab 12 excel/UZB-2014.xlsx')
df_uzb_2014.fillna(0, inplace=True)
df_uzb_2014.to_excel('/content/drive/MyDrive/lab 12 excel/UZB-2014.xlsx', index=False)

df_uzb_2015 = pd.read_excel('/content/drive/MyDrive/lab 12 excel/UZB-2015.xlsx')
df_uzb_2015.fillna(0, inplace=True)
df_uzb_2015.to_excel('/content/drive/MyDrive/lab 12 excel/UZB-2015.xlsx', index=False)

df_uzb_2016 = pd.read_excel('/content/drive/MyDrive/lab 12 excel/UZB-2016.xlsx')
df_uzb_2016.fillna(0, inplace=True)
df_uzb_2016.to_excel('/content/drive/MyDrive/lab 12 excel/UZB-2016.xlsx', index=False)

df_uzb_2017 = pd.read_excel('/content/drive/MyDrive/lab 12 excel/UZB-2017.xlsx')
df_uzb_2017.fillna(0, inplace=True)
df_uzb_2017.to_excel('/content/drive/MyDrive/lab 12 excel/UZB-2017.xlsx', index=False)

m_kgz_2014 = (df_KGZ_2014['Prob_Mod_Sev'] * df_KGZ_2014['wt']).sum() / df_KGZ_2014['wt'].sum()

m_kgz_2014

m_kgz_2015 = (df_KGZ_2015['Prob_Mod_Sev'] * df_KGZ_2015['wt']).sum() / df_KGZ_2015['wt'].sum()

m_kgz_2015

m_kgz_2016 = (df_KGZ_2016['Prob_Mod_Sev'] * df_KGZ_2016['wt']).sum() / df_KGZ_2016['wt'].sum()

m_kgz_2016

m_kgz_2017 = (df_KGZ_2017['Prob_Mod_Sev'] * df_KGZ_2017['wt']).sum() / df_KGZ_2017['wt'].sum()

m_kgz_2017

m_kz_2014 = (df_KZ_2014['Prob_Mod_Sev'] * df_KZ_2014['wt']).sum() / df_KZ_2014['wt'].sum()

m_kz_2014

m_kz_2015 = (df_KZ_2015['Prob_Mod_Sev'] * df_KZ_2015['wt']).sum() / df_KZ_2015['wt'].sum()

m_kz_2015

m_kz_2016 = (df_KZ_2016['Prob_Mod_Sev'] * df_KZ_2016['wt']).sum() / df_KZ_2016['wt'].sum()

m_kz_2016

m_kz_2017 = (df_KZ_2017['Prob_Mod_Sev'] * df_KZ_2017['wt']).sum() / df_KZ_2017['wt'].sum()

m_kz_2017

m_tjk_2014 = (df_tjk_2014['Prob_Mod_Sev'] * df_tjk_2014['wt']).sum() / df_tjk_2014['wt'].sum()

m_tjk_2014

m_tjk_2015 = (df_tjk_2015['Prob_Mod_Sev'] * df_tjk_2015['wt']).sum() / df_tjk_2015['wt'].sum()

m_tjk_2015

m_tjk_2016 = (df_tjk_2016['Prob_Mod_Sev'] * df_tjk_2016['wt']).sum() / df_tjk_2016['wt'].sum()

m_tjk_2016

m_tjk_2017 = (df_tjk_2017['Prob_Mod_Sev'] * df_tjk_2017['wt']).sum() / df_tjk_2017['wt'].sum()

m_tjk_2017

m_uzb_2014 = (df_uzb_2014['Prob_Mod_Sev'] * df_uzb_2014['wt']).sum() / df_uzb_2014['wt'].sum()

m_uzb_2014

m_uzb_2015 = (df_uzb_2015['Prob_Mod_Sev'] * df_uzb_2015['wt']).sum() / df_uzb_2015['wt'].sum()

m_uzb_2015

m_uzb_2016 = (df_uzb_2016['Prob_Mod_Sev'] * df_uzb_2016['wt']).sum() / df_uzb_2016['wt'].sum()

m_uzb_2016

m_uzb_2017 = (df_uzb_2017['Prob_Mod_Sev'] * df_uzb_2017['wt']).sum() / df_uzb_2017['wt'].sum()

m_uzb_2017

m_kgz_values = [m_kgz_2014, m_kgz_2015, m_kgz_2016, m_kgz_2017]

m_kgz_values

m_kz_values = [m_kz_2014, m_kz_2015, m_kz_2016, m_kz_2017]

m_kz_values

m_tjk_values = [m_tjk_2014, m_tjk_2015, m_tjk_2016, m_tjk_2017]

m_tjk_values

m_uzb_values = [m_uzb_2014, m_uzb_2015, m_uzb_2016, m_uzb_2017]

m_uzb_values

import matplotlib.pyplot as plt

years = range(2014, 2018)

plt.figure(figsize=(10, 6))
plt.plot(years, m_kgz_values, marker='o', linestyle='-', label='Казахстан')
plt.plot(years, m_kz_values, marker='o', linestyle='-', label='Узбекистан')
plt.plot(years, m_uzb_values, marker='o', linestyle='-', label='Кыргызстан')
plt.plot(years, m_tjk_values, marker='o', linestyle='-', label='Таджикистан')
plt.title('Центральная Азия')
plt.xticks(years)
plt.yticks(np.arange(0, 0.3, 0.05))
plt.legend()
plt.grid(True)
plt.show()
