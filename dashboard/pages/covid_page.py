from api_requests import get_countries_names, get_result_total, get_geolocation, progression_total
from visual import visual_countries, progression_total_graph
import streamlit as st

################  SELECTOR DE PAIS 

def world_comparison():
    countries = get_countries_names()
    countries.insert(0, "Worldwide")
    options = st.multiselect('Countries', countries)

    if options:
        data_total = get_result_total()
        if "Worldwide" in options:
            visual_countries(countries[1:], data_total)
            plt = progression_total_graph(progression_total(), countries[1:])
            st.pyplot(plt)
        else:
            visual_countries(options, data_total)
            plt = progression_total_graph(progression_total(), options)
            st.pyplot(plt)
   

    


