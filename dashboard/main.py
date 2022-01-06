import streamlit as st
from PIL import Image
from pages.covid_page import world_comparison

    


################### TITLE 

title_image = Image.open("dashboard/src/head_covid.jpeg")
st.image(title_image)

st.markdown("<h1 style='text-align: center; color: #942953 '>Data visualization Covid-19</h1>", unsafe_allow_html = True)

st.markdown("""
 DESCRIPCIÓN DE LA PAGINA 
""")


##################  BARRA LATERAL SELECCION DE PAGINA 

pages = st.sidebar.radio("Select Visualization", ["World comparison covid-19", "Relationship between GDP and deaths from covid"])

if pages == "World comparison covid-19":
    world_comparison()
if pages == "Relationship between GDP and deaths from covid":
    print("in construction")