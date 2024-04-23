from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.weather_service import create_weather, get_weather_by_location, get_weather_data
from ..schemas.weather_schema import weather_schema, weathers_schema
from ..services.user_service import get_user_userStatus, get_user_role

weather_blueprint = Blueprint('weather_blueprint', __name__)


@weather_blueprint.route('/add_weather', methods=['POST'])
@jwt_required()
def add_weather():
    current_user = get_jwt_identity()
    data = request.json
    weather = create_weather(data, current_user)
    return weather_schema.jsonify(weather), 201


@weather_blueprint.route('/get_weather', methods=['GET'])
def get_weather():
    weather = get_weather_data()

    return weathers_schema.jsonify(weather), 200
