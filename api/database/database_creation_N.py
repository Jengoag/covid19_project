from connection_db import engine
import pandas as pd

covid_19 = engine.get_database("covid_19")["confirmed"]

covid_19.to_sql("confirmed", engine)