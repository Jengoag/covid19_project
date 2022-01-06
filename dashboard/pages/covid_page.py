from api_requests import get_countries_names, get_result_total, get_geolocation
from visual import visual_countries, geolocation_map
import streamlit as st


def world_comparison():
    countries = get_countries_names()
    countries.insert(0, "Worldwide")
    options = st.multiselect('Countries', countries)

    if options:
        data_total = get_result_total()
        if "Worldwide" in options:
            visual_countries(countries[1:], data_total)
        else:
            visual_countries(options, data_total)
