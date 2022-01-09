import pandas as pd
import requests
import streamlit as st


################# FUNCTION OPTIONS MAPS

def get_global_map():
    result = requests.get("http://localhost:8000/global_map").json()
    return result


##################

def get_countries():
    result = requests.get("http://localhost:8000/countries").json()
    return result
