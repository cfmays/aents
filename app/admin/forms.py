# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired


class FacilityForm(FlaskForm):
    """
    Form for admin to add or edit a facility
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RoleForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AnimalForm(FlaskForm):
    """
    Form for admin to add or edit an animal
    """
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')