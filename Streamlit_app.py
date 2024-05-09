import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Terzatel apps')

st.text("Hello, this is my app.")

st.write("This is a Streamlit app used to demonstrate interactive widgets and plots!")

user_input = st.text_input("Please enter your name")

if user_input:
    st.write(f"Hello, {user_input}! Welcome to the Streamlit app.")

number = st.slider("Select a number", 0, 100, 25)
st.write(f"You selected: {number}")

data = pd.DataFrame(
    np.random.randn(50, 2), 
    columns=['A', 'B']
)
