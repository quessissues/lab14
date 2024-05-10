import pandas as pd
import pyreadstat

# Чтение файлов SPSS и сохранение в формат Excel

# Чтение и сохранение данных для 2014 года
data, meta = pyreadstat.read_sav('./lab_12_excel/UZB_2014_FIES_v01_EN_M_v01_A_OCS (1).sav')
data.to_excel('UZB-2014.xlsx', index=False)

# Чтение и сохранение данных для 2015 года
data1, meta1 = pyreadstat.read_sav('./lab_12_excel/UZB_2015_FIES_v01_EN_M_v01_A_OCS (1).sav')
data1.to_excel('UZB-2015.xlsx', index=False)

# Чтение и сохранение данных для 2016 года
data2, meta2 = pyreadstat.read_sav('./lab_12_excel/UZB_2016_FIES_v01_EN_M_v01_A_OCS (1).sav')
data2.to_excel('UZB-2016.xlsx', index=False)

# Чтение и сохранение данных для 2017 года
data3, meta3 = pyreadstat.read_sav('./lab_12_excel/UZB_2017_FIES_v01_EN_M_v01_A_OCS (2).sav')
data3.to_excel('UZB-2017.xlsx', index=False)
