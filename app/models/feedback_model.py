from datetime import datetime

from .. import db


class Feedback(db.Model):
    __tablename__ = 'feedback'

    feedbackid = db.Column(db.Integer, primary_key=True)
    feedbackuserid =db.Column(db.Integer, nullable=False)
    feedbackdesc= db.Column(db.String(120), nullable=False)
    orderid=db.Column(db.Integer, nullable=False)
    menuitemid=db.Column(db.Integer, nullable=False)
    feedbackdate = db.Column(db.String(120), nullable=False)
    feedbackstatus = db.Column(db.String(120), nullable=False)
    feedbackaction = db.Column(db.String(120), nullable=True)
    feedbackclosureremarks=db.Column(db.String(120), nullable=True)
    feedbackactionuserid=db.Column(db.Integer, nullable=True)
    createddate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updateddate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    feedbackusername =db.Column(db.String(120), nullable=True)


