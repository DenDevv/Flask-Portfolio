from sqlalchemy.dialects.postgresql import ARRAY

from app.database import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    work_uuid = db.Column(db.String(36), nullable=False)
    work_title = db.Column(db.String(50), nullable=False)
    work_desc = db.Column(db.String(), nullable=False)
    work_requirements = db.Column(ARRAY(db.String()), nullable=False)
    work_links = db.Column(ARRAY(db.String()), nullable=False)
    work_images = db.Column(ARRAY(db.String()), nullable=False)
    category = db.Column(db.String(30), nullable=False)
