from flask import Blueprint, render_template

from app.models import Project, ProjectCategory


app_blueprint = Blueprint("app", __name__)


@app_blueprint.route('/', methods=['GET'])
def home():
    return render_template("home.html")


@app_blueprint.route('/work/{work_uuid}', methods=['GET'])
def check_work(work_uuid):
    return