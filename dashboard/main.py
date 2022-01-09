import streamlit as st
from PIL import Image
from pages.covid_page import world_comparison

st.set_page_config(layout="wide")
################### TITLE 

title_image = Image.open("dashboard/src/Covid-19.png")
st.image(title_image)

##################  BARRA LATERAL SELECCION DE PAGINA 

pages = st.sidebar.radio("Select Visualization", ["World comparison covid-19", "Relationship GDP covid"])

if pages == "World comparison covid-19":
    world_comparison()
    
if pages == "Relationship GDP covid":
    st.markdown("Relationship between GDP and deaths from covid. In construction")