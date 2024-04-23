from .. import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    firstname = db.Column(db.String(120), nullable=False)
    lastname = db.Column(db.String(120), nullable=False)
    mobileno = db.Column(db.BIGINT, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    aadharID = db.Column(db.String(120), unique=True, nullable=False)
    userrole = db.Column(db.String(50), nullable=False)
    userStatus = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updatedDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    remarks = db.Column(db.String(120), nullable=False)

