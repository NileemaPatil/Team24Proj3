from .. import db, bcrypt
from ..models.user_model import User
from sqlalchemy.exc import SQLAlchemyError

def create_user(data):
    try:
        if User.query.filter_by(email=data['email']).first():
            return None, "User with that email already exists."

        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        new_user = User(
            name=data['name'],
            email=data['email'],
            password=hashed_password,
            language=data.get('language', 'en'),
            role=data.get('role', 'user')
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user, None
    except SQLAlchemyError as e:
        db.session.rollback()
        return None, f"Database error: {str(e)}"

def check_user(email, password):
    try:
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user, None
        return None, "Invalid email or password."
    except SQLAlchemyError as e:
        return None, f"Database error: {str(e)}"

def get_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return None, "User not found."
        return user, None
    except SQLAlchemyError as e:
        return None, f"Database error: {str(e)}"

def update_user(user_id, data):
    try:
        user = User.query.get(user_id)
        if not user:
            return None, "User not found."

        user.name = data.get('name', user.name)
        if 'password' in data:
            user.password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        user.language = data.get('language', user.language)
        user.role = data.get('role', user.role)

        db.session.commit()
        return user, None
    except SQLAlchemyError as e:
        db.session.rollback()
        return None, f"Database error: {str(e)}"

# Other functions in user_service.py remain unchanged

def get_user_language(user_id):
    """
    Retrieve the language preference of a user by their user ID.
    """
    user, _ = get_user(user_id)  # Reuses the get_user function already defined
    if user:
        return user.language, None
    else:
        return None, "User not found."

def get_user_role(user_id):
    """
    Retrieve the role of a user by their user ID.
    """
    user, _ = get_user(user_id)  # Reuses the get_user function already defined
    if user:
        return user.role, None
    else:
        return None, "User not found."

def delete_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return None, "User not found."

        db.session.delete(user)
        db.session.commit()
        return "User deleted successfully.", None
    except SQLAlchemyError as e:
        db.session.rollback()
        return None, f"Database error: {str(e)}"
