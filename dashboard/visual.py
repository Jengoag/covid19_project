from numpy.lib.function_base import cov
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from api_requests import get_geolocation


plt.set_loglevel('WARNING')

def visual_countries(option, data_table, data_countries_columns):
    columns_list = ["Country","confirmed", "deaths", "recovered"]
    for idx,column in enumerate(columns_list):
         with data_countries_columns[idx]:
            st.markdown(f"<p style='font-size:12px; text-align:center; background-color:{select_color(column)};'>{column.capitalize()}</h2>", unsafe_allow_html=True)

    for country in option:
        for idx,column in enumerate(columns_list):
            with data_countries_columns[idx]:
                if data_countries_columns[idx] == 1:
                    st.markdown(f"\n<p style='font-size:12px; text-align:center; background-color:#A9A9A9;'>{country}</p>", unsafe_allow_html=True)
                else:
                    visual_occurrence(data_table, country, column)

def visual_occurrence(data_table, country, column):
    for row in data_table:
        if row["Country"] == country:
            st.markdown(f"<h5 style='font-weight:400; text-align:center'>{row[column]}</h5>", unsafe_allow_html=True)

def select_color(column):
    if column == "Country": return "#F5CBA7 "
    if column == "confirmed": return "#87CEEB"
    if column == "deaths": return "#FFB6C1"
    if column == "recovered": return "#A9DFBF"

def get_difference(row):
    return  row["recovered"] - row["deaths"] 


def progression_total_graph(progression_total, options, column_option_selected):
    column_option_selected_index = get_column_option_selected_index(column_option_selected)
    covid_data = pd.DataFrame(progression_total)
    plt.figure(figsize=[20,10])

    for country in options:
        dates = []
        values = []
        for row in covid_data.values:
            if row[0] == country:
                values.append([row[column_option_selected_index]])
                dates.append(row[4])
        
        plt.ylabel('Cases')
        plt.xlabel('Date')
        plt.xticks(rotation=75)
        plt.plot(dates, values, label=row[0])

    plt.legend(options)
    return plt  

def get_column_option_selected_index(column_option_selected):
    if column_option_selected == "Confirmed": return 1
    if column_option_selected == "Deaths": return 2
    if column_option_selected == "Recovered": return 3

def geolocation_map(options):
    all_geolocations = get_geolocation()
    options_geolocation = []

    for row in all_geolocations:
        if row["Country"] in options:
            options_geolocation.append(row)

    df = pd.DataFrame(
        options_geolocation,
        columns=['lat', 'lon'])

    st.map(df)  