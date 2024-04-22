from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os

# Initialize Flask extensions
db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()


def create_app():
    # Create a Flask application instance
    app = Flask(__name__)

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI',
                                                           'postgresql://postgres:postgres_lc@10.2.8.12/mweAnnotationPlatform')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Secret keys configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_fallback_secret_key')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY',
                                                  'your_jwt_secret_key')  # Keep your existing JWT_SECRET_KEY

    # Initialize Flask extensions with app context
    bcrypt.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    jwt = JWTManager(app)
    CORS(app)

    # Import and register blueprints
    with app.app_context():
        from .controllers.user_controller import user_blueprint
        from .controllers.project_controller import project_blueprint
        from .controllers.sentence_controller import sentence_blueprint

        app.register_blueprint(user_blueprint, url_prefix="/user")
        app.register_blueprint(project_blueprint, url_prefix="/project")
        app.register_blueprint(sentence_blueprint, url_prefix="/sentence")

        # Create all database tables if they don't exist
        db.create_all()

    return app


# If the file is executed as a standalone script, run the application
if __name__ == '__main__':
    app_instance = create_app()
    app_instance.run(host='0.0.0.0', port=5000, debug=True)
