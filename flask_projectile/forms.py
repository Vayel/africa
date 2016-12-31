from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, URL

class CreateProjectForm(FlaskForm):
    url = StringField('Adresse de la tuile Trello', validators=[DataRequired(), URL()])
