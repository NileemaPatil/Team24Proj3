from datetime import datetime

from .. import db


class Address(db.Model):
    __tablename__ = 'address'

    addressid = db.Column(db.Integer, primary_key=True)
    userid = db.relationship('user', backref='address', lazy=True)
    typeofaddress = db.Column(db.String(120), nullable=False)
    address_desc = db.Column(db.String(120), nullable=False)
    createddate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updateddate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

