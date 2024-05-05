from flask import Blueprint, render_template, jsonify, redirect, url_for

from config import config
from app.database import db
from app.models import Project


admin_blueprint = Blueprint("admin_blue", __name__)
base_conf = config.get("base")


@admin_blueprint.get("/admin")
def admin_home():
    return render_template("admin_panel.html")


@admin_blueprint.post("/admin")
def post_new_project():
    return redirect(url_for("admin_blue.admin_home"))
