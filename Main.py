import streamlit as st

st.header("Data Science Project")

st.subheader("Group Members :")
st.write("""
        ***Adil Usman - 23151***  
        ***Hadia Rafiq - 25195***  
        ***Anas Tanveer - 23173***  
        """)
st.subheader("Project Title :")
st.write("**HEART ATTACK RISK PREDICTION**")

st.write("""         
        **Description:**  
        This project aims to predict the likelihood of a heart attack based on various individual attributes and health indicators. 
        The dataset includes both categorical and numerical features, and several biometric and lifestyle-related variables. 
        The target variable, **Heart Attack Risk**, is binary (**0 = No Risk, 1 = At Risk**).  
          
        **ML Model**  
        
        **Ensemble Method** 
           ***Random Forest***
           ***XGBoost Classifier***
           ***Logistic Regression*** 
        """)
st.write("""
        To **Preview Dataset and Visualizations** and to test a new sample, please select a page from the **left pane**.
         """)