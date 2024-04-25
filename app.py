import streamlit as st
from predict_page import show_predict_page
# from explore_page import show_explore_page
import pickle
import streamlit as st
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

# page = st.selectbox("Explore Or Predict", ("Predict", "Explore"))
# page = st.title("Predict")

# if page == "Predict":
show_predict_page()
# else:
#     show_explore_page()


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .viewerBadge_container__1QSob {display: none;}
            .element-container a[target="_blank"] {
                display: none !important;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


# Load your dataset (replace 'your_dataset.csv' with the path to your dataset)
df = pd.read_csv('survey_results_public.csv')


st.markdown("---")

# Display the dataset using st.dataframe()
st.write("## Dataset feeded to the model.")
st.dataframe(df)

# Add a horizontal rule to separate content
st.markdown("---")

# Define the code credit section
code_credit_section = """
### Code Credits
This Streamlit app was created by Vishesh Yadav.
"""

# Display the code credit section
st.markdown(code_credit_section)
