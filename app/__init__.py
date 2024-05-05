from flask import Flask, json
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from config import config
from app.database import db
from app.models import Project


base_conf = config.get("base")

app = Flask(__name__)
admin = Admin(app, name="Admin Panel", template_mode="bootstrap4")
admin.add_view(ModelView(Project, db.session))


def create_app():
    from app.views import app_blueprint, admin_blueprint

    app.secret_key = base_conf.APP_SECRET
    app.config["SQLALCHEMY_DATABASE_URI"] = base_conf.DB_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["FLASK_ADMIN_SWATCH"] = "lux"

    json.provider.DefaultJSONProvider.ensure_ascii = False

    # Set up extensions.
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Register blueprints.
    app.register_blueprint(app_blueprint)
    app.register_blueprint(admin_blueprint)

    return app
