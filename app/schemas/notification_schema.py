from .. import ma

class FeedbackSchema(ma.Schema):
    class Meta:
        fields = ('notificationid', 'userid', 'notificationdesc', 'notificationcreateddate', 'notificationtype','notificationstatus' ,'createddate','updateddate')
