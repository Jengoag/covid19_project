import pandas as pd
import requests
import streamlit as st


################# FUNCTION OPTIONS MAPS

def get_global_map():
    result = requests.get("http://localhost:8000/global_map").json()

    df = pd.DataFrame(
        result,
        columns=['lat', 'lon'])

    st.map(df)


##################

def get_countries():
    result = requests.get("http://localhost:8000/countries").json()
    return result













""" def country_covid():
    result = requests.get("http://localhost:5000/country_covid").json()

    df = pd.DataFrame(
         result,
        columns=['age', 'total'])

    st.vega_lite_chart(df, 
{   
    "title": {"text": "Population by Age", "anchor": "middle", "fontSize": 30, "color": ["#A08508"]},
    "width": 800,
    "height": 600,
    "mark": {"type": "bar", "color": ["#A08508"]},
        "encoding": {
            'y': {"title": "Population", "aggregate": "sum", "scale": {"domain": [0,700000]}, 'field': 'total'},
            'x': {"title": "Age", 'field': 'age'}
            }
    })


def get_graph_by_country(option):

    if option=='España':
        population_by_age()


    st.subheader(f"Casos de covid en {'PAIS'}")

        year_author_df = pd.DataFrame(df.groupby(['read_at_year'])[
            'author_gender'].value_counts(normalize=True))
        year_author_df.columns = ['Percentage']
        year_author_df.reset_index(inplace=True)
        year_author_df = year_author_df[year_author_df['read_at_year'] != '']
        fig = Figure()
        ax = fig.subplots()
        sns.lineplot(x=year_author_df['read_at_year'], y=year_author_df['Percentage'],
                     hue=year_author_df['author_gender'], ax=ax)
        ax.set_xlabel('Year')
        ax.set_ylabel('Percentage')
        st.pyplot(fig) """
