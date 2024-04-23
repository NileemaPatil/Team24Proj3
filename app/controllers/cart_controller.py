from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.cart_service import add_to_cart, remove_from_cart, place_order, get_or_create_cart
from app.schemas.cart_schema import CartSchema, CartItemSchema

cart_blueprint = Blueprint('cart_blueprint', __name__)

cart_schema = CartSchema()
cart_item_schema = CartItemSchema()

@cart_blueprint.route('/add', methods=['POST'])
@jwt_required()
def add_to_cart_route():
    user_id = get_jwt_identity()
    data = request.get_json()
    menu_item_id = data['menu_item_id']
    quantity = data.get('quantity', 1)
    cart_item = add_to_cart(user_id, menu_item_id, quantity)
    return cart_item_schema.jsonify(cart_item), 201

@cart_blueprint.route('/remove/<int:cart_item_id>', methods=['DELETE'])
@jwt_required()
def remove_from_cart_route(cart_item_id):
    user_id = get_jwt_identity()
    if remove_from_cart(user_id, cart_item_id):
        return jsonify({"message": "Item removed from cart"}), 200
    else:
        return jsonify({"error": "Failed to remove item from cart"}), 400

@cart_blueprint.route('/', methods=['GET'])
@jwt_required()
def view_cart():
    user_id = get_jwt_identity()
    cart = get_or_create_cart(user_id)
    return cart_schema.jsonify(cart), 200

@cart_blueprint.route('/place_order', methods=['POST'])
@jwt_required()
def place_order_route():
    user_id = get_jwt_identity()
    order = place_order(user_id)
    return jsonify({"message": "Order placed successfully", "order_id": order.id}), 201