from datetime import timedelta
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from ..services.user_service import create_user, check_user, get_user, update_user, delete_user
from ..schemas.user_schema import user_schema

    user_blueprint = Blueprint('user_blueprint', __name__)

    @user_blueprint.route('/register', methods=['POST'])
    def register_user():
        data = request.get_json()
        user, error = create_user(data)
        if error:
            return jsonify({"error": error}), 400
        return user_schema.jsonify(user), 201

    @user_blueprint.route('/login', methods=['POST'])
    def login_user():
        data = request.get_json()
        user, error = check_user(data['email'], data['password'])
        if error:
            return jsonify({"error": error}), 401
        expires = timedelta(minutes=30)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return jsonify(access_token=access_token, user_id=user.id), 200

    @user_blueprint.route('/users/<int:user_id>', methods=['GET'])
    @jwt_required()
    def user_details(user_id):
        user, error = get_user(user_id)
        if error:
            return jsonify({"error": error}), 400
        if not user:
            return jsonify({"message": "User not found"}), 404
        return user_schema.jsonify(user), 200

    @user_blueprint.route('/users/<int:user_id>', methods=['PUT'])
    @jwt_required()
    def update_user_details(user_id):
        data = request.get_json()
        user, error = update_user(user_id, data)
        if error:
            return jsonify({"error": error}), 400
        return user_schema.jsonify(user), 200

    @user_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
    @jwt_required()
    def remove_user(user_id):
        _, error = delete_user(user_id)
        if error:
            return jsonify({"error": error}), 400
        return jsonify({"message": "User deleted successfully."}), 204

    # The existing /protected route can remain as is for your reference
    @user_blueprint.route('/protected', methods=['GET'])
    @jwt_required()
    def protected():
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200
