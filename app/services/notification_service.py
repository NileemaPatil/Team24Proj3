import datetime
import re

from sqlalchemy import func

from .. import db
from ..models.notification_model import notification

from ..schemas.notification_schema import notification_schema


def create_notification(data, current_user):
    new_notification = Notification(
        notificationid=data['notificationid'],
        userid=data['userid'],
        notificationdesc=data['notificationdesc'],
        notificationcreateddate=data['notificationcreateddate'],
        notificationtype=data['notificationtype'],
        notificationstatus=data['notificationstatus'],
        createddate=datetime.datetime.now(),
        updateddate=datetime.datetime.now()
    )


    db.session.add(new_notification)
    db.session.flush()
    db.session.commit()
    return new_notification

def get_notification(notificationid):
    notification = Notification.query.filter_by(Notification.notificationid == notificationid).order_by(Notification.notificationid.desc()).all()
    return feedback

def get_user_notification(userid):
    notification = Notification.query.filter_by(Notification.userid == userid).order_by(Notification.notificationid.desc()).all()
    return feedback

def get_notification():
    notification = Notification.query.filter_by().order_by(Notification.notificationid.desc()).all()
    return notification
