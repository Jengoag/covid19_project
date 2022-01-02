import streamlit as st
import requests
import math

def get_card_by_district(district):
    if district == "Ciutat Vella":
        get_card(0, "#A08508")
    if district == "Horta-Guinardó":
        get_card(1, "#A02922")
    if district == "Sants-Montjuïc":
        get_card(2, "#83a971")
    if district == "Sarrià-Sant Gervasi":
        get_card(3, "#746393")
    if district == "Sant Martí":
        get_card(4, "#e08f78")
    if district == "Gràcia":
        get_card(5, "#3f7284")
    if district == "Eixample":
        get_card(6, "#87a757")
    if district == "Nou Barris":
        get_card(7, "#dc7082")
    if district == "Sant Andreu":
        get_card(8, "#eacf84")
    if district == "Les Corts":
        get_card(9, "#506a75")

def get_card(index, color):
    st.markdown(f"<h1 style='text-align: center; color: {color} '> {get_population()[index]['district']} </h1>", unsafe_allow_html = True)
    st.text('')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"**Population:** {get_population()[index]['TOTAL_POPULATION_BY_DISTRICT']}")
        st.markdown(f"**Rent:** {math.trunc(get_renta()[index]['import_anual'])}")

    with col2:
        st.markdown(f"**Wifi:** {get_wifi()[index]['TOTAL_WIFI_BY_DISTRICT']}")
        st.markdown(f"**Parks:** {math.trunc(get_parks()[index]['TOTAL_PARQUES_BY_DISTRICT'])}")
                    
    with col3:
        st.markdown(f"**Animals:** {math.trunc(get_animals()[index]['total'])}")
        st.markdown(f"**Dog's Areas:** {get_area()[index]['TOTAL_AREA_BY_DISTRICT']}")
    

def get_population():
    return requests.get("http://localhost:5000/population_by_district").json()

def get_area():
    return requests.get("http://localhost:5000/area_by_district").json()

def get_animals():
    return requests.get("http://localhost:5000/animals_by_district").json()

def get_parks():
    return requests.get("http://localhost:5000/parques_by_district").json()

def get_wifi():
    return requests.get("http://localhost:5000/wifi_by_district").json()

def get_renta():
    return requests.get("http://localhost:5000/renta_by_district").json()