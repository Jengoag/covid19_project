from api_requests import get_countries_names, get_result_total, get_geolocation 
from visual import visual_countries, geolocation_map
import streamlit as st


def world_comparison():
    countries = get_countries_names()
    option = st.multiselect('Countries', countries)

    if option:
        data_total = get_result_total(option)
        visual_countries(option, data_total)

    


