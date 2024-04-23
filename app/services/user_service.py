from .. import db, bcrypt
from ..models.user_model import User


def create_user(data):
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'],firstname=data['firstname'],lastname=data['lastname'], mobileno=data['mobileno'], email=data['email'],aadharID=data['aadharID'], userrole=data['userrole'], userStatus=data['userStatus'],  password=hashed_password,
                    remarks=data['remarks'])
    db.session.add(new_user)
    db.session.commit()
    return new_user


def check_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return user
    return None


def get_user_userStatus(email):
    user = User.query.filter_by(email=email).first()
    return user.userStatus


def get_user_role(email):
    user = User.query.filter_by(email=email).first()
    return user.userrole

