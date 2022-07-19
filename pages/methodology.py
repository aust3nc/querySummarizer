import streamlit as st

html_string = "<h3>this is an html string</h3>"

st.markdown(html_string, unsafe_allow_html=True)