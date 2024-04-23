from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.user_service import get_user_role, get_user_userStatus
from ..services.canteen_service import create_canteen, get_canteen
from ..schemas.canteen_schema import canteen_schema

canteen_blueprint = Blueprint('canteen_blueprint', __name__)


@canteen_blueprint.route('/add_canteen', methods=['POST'])
@jwt_required()
def add_canteen():
    current_user = get_jwt_identity()
    data = request.json
    canteen = create_canteen(data, current_user)
    return canteen_schema.jsonify(canteen), 201


@canteen_blueprint.route('/get_canteen_list', methods=['GET'])
@jwt_required()
def get_canteen_list():
    current_user = get_jwt_identity()
    user_role = get_user_role(current_user)
    canteenlist = get_canteen()
    current_user = get_jwt_identity()


    canteen_data = []

    for canteen in canteenlist:
        canteen_data = {
            "canteenid": canteen.canteenid,
            "location": canteen.location,
            "canteenname": canteen.canteenname,
            "canteenowner": canteen.canteenowner,
            "canteenstatus": canteen.canteenstatus
        }




        canteen_data.append(canteen_data)

    # Use jsonify to convert the list of dictionaries to a JSON response
    return jsonify(canteen_data)
