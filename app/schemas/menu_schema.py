from .. import ma

class MenuSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'created_on', 'items')

class MenuItemSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'menu_id', 'created_on')

menu_schema = MenuSchema()
menus_schema = MenuSchema(many=True)
menu_item_schema = MenuItemSchema()
menu_items_schema = MenuItemSchema(many=True)