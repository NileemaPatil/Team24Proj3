import datetime
import re

from sqlalchemy import func

from .. import db
from ..models.canteen_model import Canteen

from ..schemas.canteen_schema import canteen_schema


def create_canteen(data, current_user):
    new_canteen = Canteen(
        canteenid=data['canteenid'],
        location=data['location'],
        canteenname=data['canteenname'],
        canteenowner=data['canteenowner'],
        canteenstatus=data['canteenstatus'],
        createddate=datetime.datetime.now(),
        updateddate=datetime.datetime.now()
    )


    db.session.add(new_canteen)
    db.session.flush()
    db.session.commit()
    return new_canteen

def get_canteen(canteenid):
    canteen = Canteen.query.filter_by(Canteen.canteenid == canteenid).order_by(Canteen.canteenid.desc()).all()
    return canteen



def get_canteen():
    canteens = Canteen.query.filter_by().order_by(Canteen.canteenid.desc()).all()
    return canteens
