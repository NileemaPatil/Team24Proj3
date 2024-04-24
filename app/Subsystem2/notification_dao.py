# notification_dao.py
from datetime import datetime
from .notification_model import Notification
from .notification_dto import NotificationDTO

class NotificationDAO:
    def __init__(self, session):
        self.session = session

    def create_notification(self, notification_dto):
        notification = Notification(
            userid=notification_dto.user_id,
            notificationdesc=notification_dto.description,
            notificationcreateddate=datetime.now(),
            notificationtype=notification_dto.notification_type,
            notificationstatus=notification_dto.status
        )
        self.session.add(notification)
        self.session.commit()
        return notification.notificationid

    def get_all_notifications(self):
        notifications = self.session.query(Notification).all()
        return [NotificationDTO(
            notification.notificationid,
            notification.userid,
            notification.notificationdesc,
            notification.notificationcreateddate,
            notification.notificationtype,
            notification.notificationstatus
        ) for notification in notifications]
