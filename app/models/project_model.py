from sqlalchemy.dialects.postgresql import ARRAY

from app import db


project_categories = db.Table(
    "project_categories",
    db.Column("project_id", db.Integer, db.ForeignKey("project.id"), primary_key=True),
    db.Column(
        "category_id", db.Integer, db.ForeignKey("project_category.id"), primary_key=True
    ),
)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    work_uuid = db.Column(db.String(36), nullable=False)
    work_title = db.Column(db.String(50), nullable=False)
    work_desc = db.Column(db.String(), nullable=False)
    work_requirements = db.Column(ARRAY(db.String()), nullable=False)
    work_links = db.Column(ARRAY(db.String()), nullable=False)
    work_images = db.Column(ARRAY(db.String()), nullable=False)

    categories = db.relationship(
        "ProjectCategory",
        secondary=project_categories,
        backref=db.backref("projects", lazy="dynamic"),
    )

    def __repr__(self):
        return f"<Project {self.name}>"


class ProjectCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"<ProjectCategory {self.name}>"
