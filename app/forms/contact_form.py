from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import Length, DataRequired


class ContactForm(FlaskForm):
    ...
