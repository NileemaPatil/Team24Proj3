from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os


db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres_lc@10.2.8.12/mweAnnotationPlatform'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'THIS IS A SECRET KEY'

    app.debug = True

    bcrypt.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    jwt = JWTManager(app)
    # CORS(app)
    cors = CORS(app, resources={r"/*": {"origins": ["http://localhost:5000"]}})

    with app.app_context():
        from app.controllers.user_controller import user_blueprint
        from app.controllers.project_controller import project_blueprint
        from app.controllers.sentence_controller import sentence_blueprint
        from app.controllers.menu_controller import menu_blueprint
        from app.controllers.cart_controller import cart_blueprint
        app.register_blueprint(user_blueprint, url_prefix="/user")
        app.register_blueprint(project_blueprint, url_prefix="/project")
        app.register_blueprint(sentence_blueprint, url_prefix="/sentence")
        app.register_blueprint(menu_blueprint, url_prefix="/menu")
        app.register_blueprint(cart_blueprint, url_prefix="/cart")

        db.create_all()

    return app
