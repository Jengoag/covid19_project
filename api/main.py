from fastapi import FastAPI
from fastapi import APIRouter
from bson import json_util
from json import loads
from database.sql import db

router = APIRouter()

# endpoint de inicio 

@router.get("/")
def init_root():
    return "message: Visualización de datos Covid 19"
    
@router.get("/global_map")
def global_map():
    query = f"""
        SELECT country, lat, lon
        FROM geolocation
        WHERE country like 'Albania'
        ;
    """
    result = db.execute(query).fetchall()

    return loads(json_util.dumps(result))