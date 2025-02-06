import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv("titanic.csv")  # Load dataset

st.write("Summary Statistics")
st.dataframe(df.describe())

st.write("Number of missing values by columns:")
st.dataframe(df.isnull().sum())  # Identify missing values

st.write("Heatmap for Missing Values")
fig, ax = plt.subplots()
sns.heatmap(df.isnull(), cmap="viridis", cbar=False)
st.pyplot(fig)

st.subheader("Handle Missing Data")
column = st.selectbox("Choose a column to Fill", df.select_dtypes(include=['number']).columns)
method = st.radio("Choose a method", ["Original DF", "Drop Rows", "Drop Columns (>50% Missing)", "Impute Mean", "Impute Median", "Impute Zero"])

df_clean = df.copy()  # Ensure df_clean is always defined

if method == "Original DF":
    df_clean = df_clean
elif method == "Drop Rows":
    df_clean = df_clean.dropna()
elif method == "Drop Columns (>50% Missing)":
    df_clean = df_clean.drop(columns=df_clean.columns[df_clean.isnull().mean() > 0.5])
elif method == "Impute Mean":
    df_clean[column] = df_clean[column].fillna(df[column].mean())
elif method == "Impute Median":
    df_clean[column] = df_clean[column].fillna(df[column].median())
elif method == "Impute Zero":
    df_clean[column] = df_clean[column].fillna(0)

st.subheader("Cleaned Dataset Preview")
st.write(column)

fig, ax = plt.subplots()
sns.histplot(df_clean[column])
st.pyplot(fig)