import ibm_db_sa
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import APP_SETTINGS

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(APP_SETTINGS)

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        from application.auth.routes import auth_blueprint
        app.register_blueprint(auth_blueprint, url_prefix=f'/v1/auth')

        db.create_all()

    return app
