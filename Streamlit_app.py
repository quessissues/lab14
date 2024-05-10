import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Определение списка стран и годов
countries = ['KGZ', 'KZ', 'TJK', 'UZB']
years = range(2014, 2018)

# Создание пустых списков для хранения значений m для каждой страны
m_values = {country: [] for country in countries}

# Загрузка данных для каждой страны и каждого года
def load_data(country, year):
    @st.cache_data  # Используем st.cache_data вместо st.cache
    def _load_data(country, year):
        df = pd.read_excel(f'./Lab_12_ex/{country}-{year}.xlsx')
        return df

    return _load_data(country, year)


# Вычисление значений m для каждой страны и года
def calculate_m_values():
    for country in countries:
        for year in years:
            # Загружаем данные
            df = load_data(country, year)
            # Заполняем пропущенные значения нулями
            df.fillna(0, inplace=True)
            # Вычисляем значение m
            m_value = (df['Prob_Mod_Sev'] * df['wt']).sum() / df['wt'].sum()
            # Добавляем значение m в соответствующий список
            m_values[country].append(m_value)

# Вызываем функцию для вычисления значений m
calculate_m_values()

# Создание графика для страны и года
def plot_data(country, year):
    st.subheader(f'График для {country} {year}')
    plt.figure(figsize=(10, 6))
    for country_name, m_list in m_values.items():
        plt.plot(years, m_list, marker='o', linestyle='-', label=country_name)
    plt.title(f'Среднее значение m для {country} {year}')
    plt.xlabel('Год')
    plt.ylabel('Среднее значение m')
    plt.xticks(np.arange(2014, 2018, step=1))
    plt.legend()
    st.pyplot()

# Добавление хедера
st.title('Анализ данных по странам Центральной Азии')
st.markdown('Это приложение анализирует данные по странам Центральной Азии.')

# Добавление бокового меню
st.sidebar.header('Настройки графика')
selected_country = st.sidebar.selectbox('Выберите страну:', countries)
selected_year = st.sidebar.selectbox('Выберите год:', years)

st.subheader(f'Данные для {selected_country} за {selected_year}')
df = load_data(selected_country, selected_year)
st.write(df)  # Показываем данные
plot_data(selected_country, selected_year)  # Строим график
import streamlit as st

# Disable the PyplotGlobalUseWarning
st.set_option('deprecation.showPyplotGlobalUse', False)

