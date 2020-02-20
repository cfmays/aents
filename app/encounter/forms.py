# app/encounter/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Optional

from ..models import Person, Animal, Encounter

class OpenEncounterForm(FlaskForm):
    """
    Form for users to open a new encounter
    """   

    #animal_id = SelectField(u'Animal', coerce=int)
    #only_my_animals = BooleanField(default=True, label='Show only animals I have permission for')
    submit = SubmitField('Save')
