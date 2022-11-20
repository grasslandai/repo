import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explorer_page

show_predict_page()

#show_explorer_page()

#page = st.sidebar.selectbox("Explore or predict", ("Predict", "Explore"))
#
#if page == "Predict":
#    show_predict_page()
#else:
#    show_explorer_page()
