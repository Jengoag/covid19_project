import requests


def get_countries_names():
    result_country_names = requests.get("http://localhost:8000/countries_names").json()
    c_names = [country["Country"] for country in result_country_names]
    return list(c_names)
    
def get_result_total():
    result_total = requests.get("http://localhost:8000/result_total").json()
    return result_total

def get_geolocation(countries):
    result_geolocation = requests.get("http://localhost:8000//geolocation").json()
    return result_geolocation
    