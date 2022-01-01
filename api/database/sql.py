import os
from dotenv import load_dotenv
load_dotenv()

user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")

from sqlalchemy import create_engine

postgres_url = f'postgresql+psycopg2://{user}:{password}@127.0.0.1:5432'

engine = create_engine(f'{postgres_url}/covid_19')
db = engine.connect()

import pandas as pd

# Tabla confirmed
covid_19 = pd.read_csv('../../data/clean/confirmed.csv')
covid_19.columns = [c.lower() for c in covid_19.columns] 

covid_19.to_sql("confirmed", engine)

# Tabla deaths
covid_19 = pd.read_csv('../../data/clean/deaths.csv')
covid_19.columns = [c.lower() for c in covid_19.columns] 

covid_19.to_sql("deaths", engine)

# Tabla geolocation
covid_19 = pd.read_csv('../../data/clean/geolocation.csv')
covid_19.columns = [c.lower() for c in covid_19.columns] 

covid_19.to_sql("geolocation", engine)

# Tabla recovered
covid_19 = pd.read_csv('../../data/clean/recovered.csv')
covid_19.columns = [c.lower() for c in covid_19.columns] 

covid_19.to_sql("recovered", engine)

# Tabla spending
covid_19 = pd.read_csv('../../data/clean/spending.csv')
covid_19.columns = [c.lower() for c in covid_19.columns] 

covid_19.to_sql("spending", engine)
