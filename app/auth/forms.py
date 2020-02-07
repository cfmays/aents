# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Optional

from ..models import Person


class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    facility_id = SelectField(u'Facilty', coerce=int) 
    role_id = SelectField(u'Role', coerce=int)
    email = StringField('Email', validators=[
                                        Optional(),
                                        Email()]) # removed validators=[Email()] so that user can leave it blank
    username = StringField('User Name', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_username(self, field):
        if Person.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')

class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    username = StringField('User name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

