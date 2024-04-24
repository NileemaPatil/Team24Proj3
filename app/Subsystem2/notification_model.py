# notification_model.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from .. import db

Base = declarative_base()

class Notification(db.Model):
    __tablename__ = 'notification'
    notificationid = db.Column(db.Integer, primary_key=True)
    userid =db.Column(db.Integer, nullable=False)
    notificationdesc= db.Column(db.String(120), nullable=False)
    notificationcreateddate=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    notificationtype= db.Column(db.String(120), nullable=False)
    notificationstatus = db.Column(db.String(50), nullable=False)
    createddate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updateddate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<Notification(notificationid={self.notificationid}, userid={self.userid}, " \
               f"notificationdesc={self.notificationdesc}, notificationcreateddate={self.notificationcreateddate}, " \
               f"notificationtype={self.notificationtype}, notificationstatus={self.notificationstatus}, " \
               f"createddate={self.createddate}, updateddate={self.updateddate})>"


