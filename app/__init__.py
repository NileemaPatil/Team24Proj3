from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS


db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1/Test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

    bcrypt.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    jwt = JWTManager(app)
    CORS(app)

    with app.app_context():
        from .controllers.user_controller import user_blueprint
        from .controllers.project_controller import project_blueprint
        from .controllers.sentence_controller import sentence_blueprint
        from .controllers.weather_controller import weather_blueprint

        app.register_blueprint(user_blueprint, url_prefix="/user")
        app.register_blueprint(project_blueprint, url_prefix="/project")
        app.register_blueprint(sentence_blueprint, url_prefix="/sentence")
        app.register_blueprint(weather_blueprint, url_prefix="/weather")

        db.create_all()

    return app
