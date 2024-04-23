from datetime import timedelta

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from ..services.user_service import create_user, check_user
from ..schemas.user_schema import user_schema

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    user = create_user(data)
    return user_schema.jsonify(user)


@user_blueprint.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    user = check_user(data['email'], data['password'])
    if user:
        expires = timedelta(minutes=30)
        access_token = create_access_token(identity=data['email'], expires_delta=expires)
        return jsonify(access_token=access_token, role=user.userrole), 200
    else:
        return jsonify({"message": "Invalid email or password"}), 401


@user_blueprint.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200