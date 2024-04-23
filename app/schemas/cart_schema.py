from .. import ma
from .menu_schema import MenuItemSchema

class CartItemSchema(ma.Schema):
    menu_item = ma.Nested(MenuItemSchema)

    class Meta:
        fields = ('id', 'menu_item', 'quantity', 'created_at')

class CartSchema(ma.Schema):
    items = ma.List(ma.Nested(CartItemSchema))

    class Meta:
        fields = ('id', 'user_id', 'items', 'created_at')

cart_schema = CartSchema()
cart_item_schema = CartItemSchema()