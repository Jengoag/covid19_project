import pandas as pd
from sql import engine

# Tabla confirmed
covid_19 = pd.read_csv('data/clean/confirmed.csv')
covid_19.columns = [c.lower() for c in covid_19.columns] 

covid_19.to_sql("confirmed", engine)

# Tabla deaths
covid_19 = pd.read_csv('data/clean/deaths.csv')
covid_19.columns = [c.lower() for c in covid_19.columns] 

covid_19.to_sql("deaths", engine)

# Tabla geolocation
covid_19 = pd.read_csv('data/clean/geolocation.csv')
covid_19.columns = [c.lower() for c in covid_19.columns] 

covid_19.to_sql("geolocation", engine)

# Tabla recovered
covid_19 = pd.read_csv('data/clean/recovered.csv')
covid_19.columns = [c.lower() for c in covid_19.columns] 

covid_19.to_sql("recovered", engine)

# Tabla spending
covid_19 = pd.read_csv('data/clean/spending.csv')
covid_19.columns = [c.lower() for c in covid_19.columns] 

covid_19.to_sql("spending", engine)
