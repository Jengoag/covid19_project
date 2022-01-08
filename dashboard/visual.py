from numpy.lib.function_base import cov
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

plt.set_loglevel('WARNING')

def visual_countries(option, data_table):
    columns_list = ["confirmed", "deaths", "recovered", "balance"]

    for country in option:
        st.markdown(f"\n<h3 style='text-align:center; background-color:#A9A9A9;'><b>{country}</b></h3>", unsafe_allow_html=True)
        data_countries_columns = st.columns(4)
        for idx,column in enumerate(columns_list):
            with data_countries_columns[idx]:
                visual_occurrence(data_table, country, column)

def visual_occurrence(data_table, country, column):
    for row in data_table:
        if row["Country"] == country:
            st.markdown(f"<h2 style='text-align:center; background-color:{select_color(column)};'><b>{column.capitalize()}</b></h2>", unsafe_allow_html=True)
            if column == "balance":
                st.markdown(f"<p style='text-align:center'><b>{get_difference(row)}</b></p>", unsafe_allow_html=True)
            else:
                st.markdown(f"<p style='text-align:center'><b>{row[column]}</b></p>", unsafe_allow_html=True)
    
def select_color(column):
    if column == "confirmed": return "DeepSkyBlue"
    if column == "deaths": return "OrangeRed"
    if column == "recovered": return "LightGreen"
    if column == "balance": return "Teal"

def get_difference(row):
    return  row["recovered"] - row["deaths"] 

""" def geolocation_map(geospatial, start_location = None):
    m = Map(start_location ,zoom_start=5)
    for location in geospatial:
        Marker(location=[location["Lat"], location["Long"]], tooltip=location["Name"]).add_to(m)
    folium_static(m) """

def progression_total_graph(progression_total, options):
    covid_data = pd.DataFrame(progression_total)
    plt.figure(figsize=[20,10])
    columns = [column for column in covid_data.columns[1:]]

    for country in options:
        dates = []
        values = []
        for row in covid_data.values:
            if row[0] == country:
                values.append([row[2]])
                dates.append(row[4])
        
        plt.ylabel('Cases')
        plt.xlabel('Date')
        plt.xticks(rotation=75)
        plt.plot(dates, values, label=row[0])


    plt.legend(options)
    return plt  