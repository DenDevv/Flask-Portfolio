from flask import Blueprint, render_template, jsonify

from config import config
from app.database import db
from app.models import Project


app_blueprint = Blueprint("app", __name__)
base_conf = config.get("base")


@app_blueprint.route("/", methods=["GET"])
def home():
    projects = Project.query.all()
    c_projects = {i: [] for i in base_conf.categories}

    for project in projects:
        c_projects.get(project.category).append(project)

    return c_projects

    # return render_template(
    #     "home.html", projects=c_projects, categories=base_conf.categories
    # )


@app_blueprint.route("/work/<work_uuid>", methods=["GET"])
def check_work(work_uuid):
    project = Project.query.filter_by(work_uuid=work_uuid).first()

    return render_template("check_work.html", project=project)
