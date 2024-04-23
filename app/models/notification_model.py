from datetime import datetime

from .. import db


class Project(db.Model):
    __tablename__ = 'notification'

    notificationid = db.Column(db.Integer, primary_key=True)
    userid =db.Column(db.Integer, nullable=False)
    notificationdesc= db.Column(db.String(120), nullable=False)
    notificationcreateddate=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    notificationtype= db.Column(db.String(120), nullable=False)
    notificationstatus = db.Column(db.String(50), nullable=False)
    createddate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updateddate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)



