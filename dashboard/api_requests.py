import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_URL = os.getenv("API_URL")

def get_countries_names():
    result_country_names = requests.get(f"{API_URL}/countries_names").json()
    c_names = [country["Country"] for country in result_country_names]
    return list(c_names)
    
def get_result_total():
    result_total = requests.get(f"{API_URL}/result_total").json()
    return result_total

def get_geolocation():
    result_geolocation = requests.get(f"{API_URL}/geolocation").json()
    return result_geolocation

def progression_total():
    result_progression_total = requests.get(f"{API_URL}/progression_total").json()
    return result_progression_total