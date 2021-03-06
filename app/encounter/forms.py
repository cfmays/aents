# app/encounter/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, SelectField, BooleanField, TimeField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Optional

from ..models import Person, Animal, Encounter

class OpenEncounterForm(FlaskForm):
    """
    Form for individual users to open a new encounter
    """   
    #animal_id = SelectField(u'Animal', coerce=int)
    only_my_animals = BooleanField(default=True, label='Show only animals I have permission for')
    submit = SubmitField('Save')

class OpenEncounterFormFacility(FlaskForm):
    """
    Form for facility-wide users to open a new encounter
    """     
    person_id = SelectField(u'Person', coerce=int)
    animal_id = SelectField(u'Animal', coerce=int)
    start_date = DateField(u'Start Date', format='%Y-%m-%d')
    start_time = TimeField(u'Start Time')
    submit = SubmitField('Save')
