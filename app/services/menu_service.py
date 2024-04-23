from .. import db
from ..models.menu_model import Menu, MenuItem

def create_menu(name):
    new_menu = Menu(name=name)
    db.session.add(new_menu)
    db.session.commit()
    return new_menu

def get_menu(menu_id):
    return Menu.query.get(menu_id)

def get_menu_items(menu_id):
    menu = Menu.query.get(menu_id)
    return menu.items

def create_menu_item(name, description, price, menu_id):
    new_menu_item = MenuItem(name=name, description=description, price=price, menu_id=menu_id)
    db.session.add(new_menu_item)
    db.session.commit()
    return new_menu_item