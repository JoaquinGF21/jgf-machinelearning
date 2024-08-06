import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.info("This app builds a machine learning model")

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
  
  st.write('**X**')
  X = df.drop('species', axis = 1)
  X

  st.write('**Y**')
  y = df.species
  y



with st.expander('Data visualization'):
  # bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g
  st.scatter_chart(data=df, x='Bill Length (mm)', y='Body Mass (g)', color='Species')
                  
