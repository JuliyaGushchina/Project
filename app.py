import streamlit as st
import pandas as pd
import numpy as np

def open_data(path="data/music_genre_train.csv"):
  df = pd.read_csv(path)
  
  return df

st.table(df)
