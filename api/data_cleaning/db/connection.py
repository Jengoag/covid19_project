from api.data_cleaning.db.config import postgres_url
from sqlalchemy import create_engine

engine = create_engine(f'{postgres_url}/covid_19')
db = engine.connect()

print("Conected to Database")