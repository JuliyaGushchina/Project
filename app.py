import streamlit as st
import pandas as pd
import numpy as np


df = pd.read_csv("data/music_genre_train.csv")
st.table(df)
