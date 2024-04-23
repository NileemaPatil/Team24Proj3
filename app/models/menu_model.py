from .. import db
from datetime import datetime

class Menu(db.Model):
    __tablename__ = 'menus'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    items = db.relationship('MenuItem', backref='menu', lazy='dynamic')

class MenuItem(db.Model):
    __tablename__ = 'menu_items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)