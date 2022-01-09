from api_requests import get_countries_names, get_result_total, get_geolocation, progression_total
from visual import visual_countries, progression_total_graph
import streamlit as st

# SELECTOR DE PAIS


def world_comparison():
    countries = get_countries_names()
    countries.insert(0, "Worldwide")
    options = st.sidebar.multiselect('Countries', countries)

    col1, col2, col3, col4, col5, col6 = st.columns((1, 1, 1, 1, 0.2, 4))
    if options:
        data_total = get_result_total()
        if "Worldwide" in options:
            visual_countries(countries[1:], data_total, [col1, col2, col3, col4])
        else:
            visual_countries(options, data_total, [col1, col2, col3, col4])
        with col6:
            if options:
                column_options = ["Confirmed", "Deaths", "Recovered"]
                column_option_selected = st.sidebar.selectbox('Column Data Visualization', column_options)
                data_total = get_result_total()
                if "Worldwide" in options:
                    plt = progression_total_graph(progression_total(), countries[1:], column_option_selected)
                    st.pyplot(plt)
                else:
                    plt = progression_total_graph(progression_total(), options, column_option_selected)
                    st.pyplot(plt)

   # SELECTOR DE TIPO DE DATO
