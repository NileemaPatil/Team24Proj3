from datetime import datetime

from .. import db


class Canteen(db.Model):
    __tablename__ = 'canteen'

    canteenid = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(120), nullable=False)
    canteenname = db.Column(db.String(120), nullable=False)
    canteenowner = db.Column(db.String(120), nullable=False)
    canteenstatus = db.Column(db.String(120), nullable=True)
    createddate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updateddate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


