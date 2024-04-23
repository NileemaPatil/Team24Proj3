from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.menu_service import create_menu, get_menu, get_menu_items, create_menu_item
from app.schemas.menu_schema import MenuSchema, MenuItemSchema

menu_blueprint = Blueprint('menu_blueprint', __name__)

menu_schema = MenuSchema()
menu_item_schema = MenuItemSchema()

@menu_blueprint.route('/menus', methods=['POST'])
@jwt_required()
def create_menu():
    data = request.get_json()
    name = data.get('name')
    menu = create_menu(name)
    return menu_schema.jsonify(menu), 201

@menu_blueprint.route('/menus/<int:menu_id>', methods=['GET'])
def get_menu_details(menu_id):
    menu = get_menu(menu_id)
    if menu:
        return menu_schema.jsonify(menu), 200
    else:
        return jsonify({"message": "Menu not found"}), 404

@menu_blueprint.route('/menus/<int:menu_id>/items', methods=['GET'])
def get_menu_items_list(menu_id):
    menu_items = get_menu_items(menu_id)
    if menu_items:
        return menu_item_schema.jsonify(menu_items, many=True), 200
    else:
        return jsonify({"message": "No menu items found"}), 404

@menu_blueprint.route('/menus/<int:menu_id>/items', methods=['POST'])
@jwt_required()
def create_menu_item(menu_id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    menu_item = create_menu_item(name, description, price, menu_id)
    if menu_item:
        return menu_item_schema.jsonify(menu_item), 201
    else:
        return jsonify({"message": "Failed to create menu item"}), 400