from datetime import datetime

from .. import db

class Weather(db.Model):
    __tablename__ = 'weather'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    weather_main = db.Column(db.Text, nullable=False)
    weather_description = db.Column(db.Text, nullable=False)
    windspeed = db.Column(db.Text, nullable=False)
    temperature = db.Column(db.Text, nullable=False)
    humidity = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    uploaded_by = db.Column(db.Text, nullable=False)
    uploaded_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

