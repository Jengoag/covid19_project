from fastapi import APIRouter
from bson import json_util
from json import loads
from api.data_cleaning.db.connection import db

router = APIRouter()

@router.get("/")
def init():
    return "<p>Covid-19</p>"


@router.get("/countries_names")
def countries_names():
    query = f"""
        SELECT "Country"
        FROM geolocation
        ;
    """
    result = db.execute(query).fetchall()

    return loads(json_util.dumps(result))


@router.get("/result_total")
def result_total():
    query = f"""
        SELECT confirmed."Country", confirmed."Occurrence" AS confirmed, deaths."Occurrence" as deaths, recovered."Occurrence" as recovered
        FROM confirmed
        INNER JOIN deaths
        ON confirmed."Country" = deaths."Country"
        INNER JOIN recovered
        ON confirmed."Country" = recovered."Country"
        WHERE confirmed."Date" = '1/22/21' and deaths."Date" = '1/22/21' and recovered."Date" = '1/22/21';
    """
    result = db.execute(query).fetchall()

    return loads(json_util.dumps(result))

@router.get("/geolocation")
def geolocation():
    query = f"""
        SELECT "Country", lat, lon
        FROM geolocation
    """
    result = db.execute(query).fetchall()

    return loads(json_util.dumps(result))


@router.get("/progression_total")
def progression_total():
    query = f"""
        SELECT confirmed."Country", confirmed."Occurrence" AS confirmed , deaths."Occurrence" AS deaths,recovered."Occurrence" AS recovered, confirmed."Date"
        FROM confirmed
        INNER JOIN deaths
        ON confirmed."Country" = deaths."Country" AND confirmed."Date" = deaths."Date"
        INNER JOIN recovered
        ON confirmed."Country" = recovered."Country" AND confirmed."Date" = recovered."Date"
        ORDER BY confirmed."Occurrence" 
    """
    result = db.execute(query).fetchall()

    return loads(json_util.dumps(result))
    



