from .. import db
from app.models.cart_model import Cart, CartItem, Order, OrderItem
from .menu_service import get_menu_items

def get_or_create_cart(user_id):
    cart = Cart.query.filter_by(user_id=user_id).first()
    if not cart:
        cart = Cart(user_id=user_id)
        db.session.add(cart)
        db.session.commit()
    return cart

def add_to_cart(user_id, menu_item_id, quantity=1):
    cart = get_or_create_cart(user_id)
    menu_item = get_menu_items(menu_item_id)
    cart_item = CartItem.query.filter_by(cart_id=cart.id, menu_item_id=menu_item_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(cart_id=cart.id, menu_item_id=menu_item_id, quantity=quantity)
        cart.items.append(cart_item)
    db.session.commit()
    return cart_item

def remove_from_cart(user_id, cart_item_id):
    cart = get_or_create_cart(user_id)
    cart_item = CartItem.query.get(cart_item_id)
    if cart_item and cart_item.cart_id == cart.id:
        db.session.delete(cart_item)
        db.session.commit()
        return True
    return False

def place_order(user_id):
    cart = get_or_create_cart(user_id)
    order = Order(user_id=user_id)
    total_cost = 0
    for cart_item in cart.items:
        menu_item = get_menu_items(cart_item.menu_item_id)
        order_item = OrderItem(order_id=order.id, menu_item_id=menu_item.id, quantity=cart_item.quantity, price=menu_item.price)
        order.items.append(order_item)
        total_cost += menu_item.price * cart_item.quantity
    order.total_cost = total_cost
    db.session.add(order)
    db.session.commit()
    cart.items = []
    db.session.commit()
    return order