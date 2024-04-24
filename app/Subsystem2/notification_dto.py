from datetime import datetime

from .. import db


# notification_dto.py

class NotificationDTO:
    #tablename__ = 'notification'
    def __init__(self, notificationid, userid, notificationdesc, notificationcreateddate, notificationtype,
                 notificationstatus, createddate, updateddate):
        self.notificationid = notificationid
        self.userid = userid
        self.notificationdesc = notificationdesc
        self.notificationcreateddate = notificationcreateddate
        self.notificationtype = notificationtype
        self.notificationstatus = notificationstatus
        self.createddate = createddate
        self.updateddate = updateddate
