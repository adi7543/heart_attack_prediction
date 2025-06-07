import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("heart_attack_prediction_dataset.csv")
df = df.drop("Patient ID", axis=1)

st.title("Heart Attack Risk Prediction")

st.subheader("Dataset Preview")
st.write(df.head())

st.write("Samples, Features")
st.write(df.shape)

st.subheader("Dataset Summary")
st.write(df.describe())

st.subheader("Plot a Chart")
columns = df.columns.tolist()

x = st.selectbox("select a feature for x",columns)
y = st.selectbox("select a feature for y",columns)

c = ['scatter','line','bar']
C = st.selectbox("Select a Chart", c)

if st.button("Plot") is True:
    if C == "line":
        fig, ax = plt.subplots()  # Create a figure and axes
        ax.plot(df[x], df[y])  # Plot your data
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_title(f"{y} vs {x}")

        st.pyplot(fig)
    elif C == "scatter":
        fig, ax = plt.subplots()  # Create a figure and axes
        ax.scatter(df[x], df[y])  # Plot your data
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_title(f"{y} vs {x}")

        st.pyplot(fig)
    else:
        fig, ax = plt.subplots()  # Create a figure and axes
        ax.bar(df[x], df[y])  # Plot your data
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_title(f"{y} vs {x}")

        st.pyplot(fig)