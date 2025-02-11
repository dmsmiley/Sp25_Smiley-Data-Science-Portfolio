import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("Missing Data Explorer")

# File Upload
df = pd.read_csv("titanic.csv")

st.subheader("Handle Missing Data")
method = st.radio("Choose a method", ["Drop Rows", "Drop Columns (>50% Missing)", "Impute Mean", "Impute Median"])
if method == "Drop Rows":
    df_clean = df.dropna()
elif method == "Drop Columns (>50% Missing)":
    df_clean = df.drop(columns=df.columns[df.isnull().mean() > 0.5])
elif method == "Impute Mean":
    df_clean = df.fillna(df.mean())
elif method == "Impute Median":
    df_clean = df.fillna(df.median())

st.subheader("Cleaned Dataset Preview")
st.write(df_clean.head())
