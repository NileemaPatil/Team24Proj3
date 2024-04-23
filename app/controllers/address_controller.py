from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.project_service import create_project, get_projects_by_language, get_projects, \
    get_projects_with_annotation_counts_with_language, get_projects_with_annotation_counts
from ..schemas.project_schema import project_schema, projects_schema
from ..services.user_service import get_user_role, get_user_userStatus
from ..services.address_service import create_address, get_address
from ..schemas.address_schema import address_schema, addresss_schema

address_blueprint = Blueprint('address_blueprint', __name__)


@address_blueprint.route('/add_address', methods=['POST'])
@jwt_required()
def add_address():
    current_user = get_jwt_identity()
    data = request.json
    address = create_address(data, current_user)
    return address_schema.jsonify(address), 201


@address_blueprint.route('/get_address_list', methods=['GET'])
@jwt_required()
def get_address_list():
    current_user = get_jwt_identity()
    user_role = get_user_role(current_user)
    addresslist = get_address()
    current_user = get_jwt_identity()


    address_data = []

    for address in addresslist:
        address_data = {
            "addressid": address.addressid,
            "userid": address.userid,
            "typeofaddress": address.typeofaddress,
            "address_desc": address.address_desc
        }
        address_data.append(address_data)

    # Use jsonify to convert the list of dictionaries to a JSON response
    return jsonify(address_data)
