import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# instantiate extensions
db = SQLAlchemy()
app = Flask(__name__)


# creating app
def create_app():
    APP_SECRET = os.getenv("APP_SECRET")

    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")

    from app.views import app_blueprint

    # Instantiate app.
    app.secret_key = APP_SECRET
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Set up extensions.
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Register blueprints.
    app.register_blueprint(app_blueprint)

    return app
