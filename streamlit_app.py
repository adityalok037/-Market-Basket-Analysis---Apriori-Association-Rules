import streamlit as st
import pickle
import pandas as pd

# Load the pickle files
with open('model pkl files/best_associations.pkl', 'rb') as f:
    best_df = pickle.load(f)

with open('model pkl files/medium_associations.pkl', 'rb') as f:
    medium_df = pickle.load(f)

with open('model pkl files/low_associations.pkl', 'rb') as f:
    low_df = pickle.load(f)

# Streamlit app
st.title("Product Association Search")

# Input field for the product search
product = st.text_input("Enter a product name to search for associations:")

if product:
    # Filter the DataFrames based on the product
    best_results = best_df[best_df['Antecedents'].str.contains(product, case=False)]
    medium_results = medium_df[medium_df['Antecedents'].str.contains(product, case=False)]
    low_results = low_df[low_df['Antecedents'].str.contains(product, case=False)]
    
    st.write(f"Results for: **{product}**")
    
    # Display the best results
    if not best_results.empty:
        st.subheader("Best Associations")
        st.dataframe(best_results)
    else:
        st.write("No best associations found.")

    # Display the medium results
    if not medium_results.empty:
        st.subheader("Medium Associations")
        st.dataframe(medium_results)
    else:
        st.write("No medium associations found.")

    # Display the low results
    if not low_results.empty:
        st.subheader("Low Associations")
        st.dataframe(low_results)
    else:
        st.write("No low associations found.")
