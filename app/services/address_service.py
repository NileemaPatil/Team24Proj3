import datetime
import re

from sqlalchemy import func

from .. import db
from ..models.address_model import Address

from ..schemas.address_schema import address_schema, addresss_schema


def create_address(data, current_user):
    new_address = Address(
        addressid=data['addressid'],
        userid=data['userid'],
        typeofaddress=data['typeofaddress'],
        address_desc=data['address_desc'],
        createddate=datetime.datetime.now(),
        updateddate=datetime.datetime.now()
    )


    db.session.add(new_address)
    db.session.flush()
    db.session.commit()
    return new_address

def get_addresss():
    address = Address.query.filter_by().order_by(Address.adressid.desc()).all()
    return address



def get_address(userid):
    address = Address.query.filter_by(Address.userid == userid).order_by(Address.adressid.desc()).all()
    return address

