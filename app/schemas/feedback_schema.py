from .. import ma

class FeedbackSchema(ma.Schema):
    class Meta:
        fields = ('feedbackid', 'feedbackuserid', 'feedbackdesc', 'orderid', 'menuitemid','feedbackdate' , 'feedbackstatus','feedbackaction','feedbackclosureremarks','feedbackactionuserid','createddate','updateddate','feedbackusername')
