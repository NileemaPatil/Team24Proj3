import datetime
import re

from sqlalchemy import func

from .. import db
from ..models.weather_model import Weather

from ..schemas.weather_schema import weather_schema, weathers_schema


def create_weather(data, current_user):
    new_weather = Weather(
        date=datetime.datetime.now(),
        weather_main=data['weather_main'],
        weather_description=data['weather_description'],
        windspeed=data['windspeed'],
        temperature=data['temperature'],
        humidity=data['humidity'],
        location=data['location'],
        uploaded_by=current_user,
        uploaded_on=datetime.datetime.now()
    )

    db.session.add(new_weather)
    db.session.commit()
    return new_weather


def get_weather_by_location(location):
    weather = Weather.query.filter_by(location=location).order_by(Weather.id .desc()).all()
    return weather


def get_weather_data():
    weather = Weather.query.filter_by().all()
    print(weather)
    return weather

