import pandas as pd
import requests
import streamlit as st

################# FUNCTION GRAPHS

def population_by_age():
    result = requests.get("http://localhost:5000/population_by_age").json()

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


def population_by_district():
    result = requests.get("http://localhost:5000/population_by_district").json()

    df = pd.DataFrame(
        result,
        columns=['TOTAL_POPULATION_BY_DISTRICT', 'district'])

    st.vega_lite_chart(df, 
    {    
        "title": {"text": "Population by District", "anchor": "middle", "fontSize": 30, "color": ["#A02922"]},
        "width": 800,
        "height": 400,
        "mark": {"type": "bar", "color": ["#A02922"]},
        "encoding": {
            'x': {"title": "POPULATION", "aggregate": "sum", "scale": {"domain": [0,1_400_000]}, 'field': 'TOTAL_POPULATION_BY_DISTRICT'},
            'y': {"title": "District", 'field': 'district'},
        },
        })

def renta_by_district():
    result = requests.get("http://localhost:5000/renta_by_district").json()

    df = pd.DataFrame(
        result,
        columns=['import_anual', 'district'])

    st.vega_lite_chart(df, 
    {    
        "title": {"text": "Rent by District", "anchor": "middle", "fontSize": 30, "color": ["#83a971"]},
        "width": 1000,
        "height": 400,
        "layer": [
            {
            "mark": {"type": "bar", "color": ["#83a971"]},
            "encoding": {
                'x': {"title": "Anual Rent", "aggregate": "sum", "scale": {"domain": [0,33_000]}, 'field': 'import_anual'},
                'y': {"title": "District", 'field': 'district'}
                }
            }, 
            {
            "mark": "rule",
            "encoding": {
                "x": {"aggregate": "mean", "field": "import_anual", "type": "quantitative"},
                "color": {"value": "#FFC300"},
                "size": {"value": 3}
            }
            }
        ]
    })

def wifi_by_district():
    result = requests.get("http://localhost:5000/wifi_by_district").json()

    df = pd.DataFrame(
        result,
        columns=['TOTAL_WIFI_BY_DISTRICT', 'district'])

    st.vega_lite_chart(df, 
    {    
        "title": {"text": "Wifi by District", "anchor": "middle", "fontSize": 30, "color": ["#746393"]},
        "width": 800,
        "height": 400,
        "mark": {"type": "bar", "color": ["#746393"]},
        "encoding": {
            'x': {"title": "WIFI", "aggregate": "sum", "scale": {"domain": [0, 300]}, 'field': 'TOTAL_WIFI_BY_DISTRICT'},
            'y': {"title": "District", 'field': 'district'},
        },
        })


def animals_by_district():
    result = requests.get("http://localhost:5000/animals_by_district").json()

    df = pd.DataFrame(
        result,
        columns=['total', 'district'])

    st.vega_lite_chart(df, 
    {    
        "title": {"text": "Animals by District", "anchor": "middle", "fontSize": 30, "color": ["#e08f78"]},
        "width": 800,
        "height": 400,
        "mark": {"type": "bar", "color": ["#e08f78"]},
        "encoding": {
            'x': {"title": "Animals", "aggregate": "sum", "scale": {"domain": [0, 10_000]}, 'field': 'total'},
            'y': {"title": "District", 'field': 'district'},
        },
        })

def area_by_district():
    result = requests.get("http://localhost:5000/area_by_district").json()

    df = pd.DataFrame(
        result,
        columns=["TOTAL_AREA_BY_DISTRICT", 'district'])

    st.vega_lite_chart(df, 
    {    
        "title": {"text": "Dog's Areas by District", "anchor": "middle", "fontSize": 30, "color": ["#3f7284"]},
        "width": 800,
        "height": 400,
        "mark": {"type": "bar", "color": ["#3f7284"]},
        "encoding": {
            'x': {"title": "Dog's Areas", "aggregate": "sum", "scale": {"domain": [0, 20]}, 'field': "TOTAL_AREA_BY_DISTRICT"},
            'y': {"title": "District", 'field': 'district'},
        },
        })


def parques_by_district():
    result = requests.get("http://localhost:5000/parques_by_district").json()

    df = pd.DataFrame(
        result,
        columns=['TOTAL_PARQUES_BY_DISTRICT', 'district'])

    st.vega_lite_chart(df, 
    {    
        "title": {"text": "Parks by District", "anchor": "middle", "fontSize": 30, "color": ["##dc7082"]},
        "width": 800,
        "height": 400,
        "mark": {"type": "bar", "color": ["#dc7082"]},
        "encoding": {
            'x': {"title": "Parks", "aggregate": "sum", "scale": {"domain": [0, 120]}, 'field': 'TOTAL_PARQUES_BY_DISTRICT'},
            'y': {"title": "District", 'field': 'district'},
        },
        })


############### FUNCTIONS MAPS


def map_parques_by_district():
    result = requests.get("http://localhost:5000//xy_parques").json()
    df = pd.DataFrame(
        result,
        columns=['latitude', 'longitude'])

    st.map(df)

def map_areas_by_district():
    result = requests.get("http://localhost:5000//xy_area").json()
    df = pd.DataFrame(
        result,
        columns=['latitude', 'longitude'])

    st.map(df)


##################   FUNCTION OPTIONS TEXT
    
def get_text_by_option(option):  
    if option=="Map Dog's Areas":
        st.markdown("<h1 style='text-align: center; color: #A08508 '>Map Dog's Areas</h1>", unsafe_allow_html = True)
  
    if option=='Map Parks':
        st.markdown("<h1 style='text-align: center; color: #A08508 '>Map Parks</h1>", unsafe_allow_html = True)


################# FUNCTION OPTIONS GRAPHS AND MAPS

def get_graph_by_option(option):

    if option=='Population by Age':
        population_by_age()

    if option=='Population by District':
        population_by_district()

    if option=='Rent by Distric':
        renta_by_district()

    if option=='Wifi by District':
        wifi_by_district()

    if option=='Animals by District':
        animals_by_district()

    if option=="Dog's Areas by District":
        area_by_district()

    if option=='Population 0-14 by District':
        population_0_14_by_district()

    if option=='Parks by District':
        parques_by_district()


def get_map_by_option(option):  
    if option=='Map Parks':
        map_parques_by_district()
    
    if option=="Map Dog's Areas":
        map_areas_by_district()