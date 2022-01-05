from fastapi import APIRouter
from bson import json_util
from json import loads
from api.data_cleaning.db.connection import db

router = APIRouter()

# endpoint de inicio 

@router.get("/")
def init_root():
    return "message: Visualización de datos Covid 19"
    
@router.get("/global_map")
def global_map():
    query = f"""
        SELECT "Country", lat, lon
        FROM geolocation
        ;
    """
    result = db.execute(query).fetchall()

    return loads(json_util.dumps(result))
 
@router.get("/countries")
def countries():
    query = f"""
       SELECT "Country"
       FROM geolocation
      ;
    """
    result = db.execute(query).fetchall()

    return loads(json_util.dumps(result)) 
