import datetime
import re

from sqlalchemy import func

from .. import db
from ..models.feedback_model import Feedback

from ..schemas.feedback_schema import feedback_schema


def create_feedback(data, current_user):
    new_feedback = Feedback(
        feedbackid=data['feedbackid'],
        feedbackuserid=data['feedbackuserid'],
        feedbackdesc=data['feedbackdesc'],
        orderid=data['orderid'],
        menuitemid=data['menuitemid'],
        feedbackdate=data['feedbackdate'],
        feedbackstatus=data['feedbackstatus'],
        feedbackaction=data['feedbackaction'],
        feedbackclosureremarks=data['feedbackclosureremarks'],
        feedbackactionuserid=data['feedbackactionuserid'],
        createddate=datetime.datetime.now(),
        updateddate=datetime.datetime.now(),
        feedbackusername=data['feedbackusername']
    )


    db.session.add(new_feedback)
    db.session.flush()
    db.session.commit()
    return new_feedback

def get_feedback(feedbackid):
    feedback = Feedback.query.filter_by(Feedback.feedbackid == feedbackid).order_by(Feedback.feedbackid.desc()).all()
    return feedback

def get_user_feedback(userid):
    feedback = Feedback.query.filter_by(Feedback.feedbackuserid == userid).order_by(Feedback.feedbackid.desc()).all()
    return feedback

def get_feedback():
    feedback = Feedback.query.filter_by().order_by(Feedback.feedbackid.desc()).all()
    return feedback
