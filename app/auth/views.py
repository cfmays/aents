# app/auth/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import Person


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add a person to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        person = Person(facility=form.facility.data,
                            email=form.email.data,
                            username=form.username.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            password=form.password.data)

        # add person to the database
        db.session.add(person)
        db.session.commit()
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log a person in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():

        # check whether person exists in the database and whether
        # the password entered matches the password in the database
        person = Person.query.filter_by(username=form.username.data).first()
        if person is not None and person.verify_password(
                form.password.data):
            
            # log person in
            login_user(person)

            # redirect to the appropriate dashboard page
            if person.is_admin:
                return redirect(url_for('home.admin_dashboard'))
            else:
                return redirect(url_for('home.dashboard'))
           #return redirect('http://www.ibm.com')

        # when login details are incorrect
        else:
            flash('Invalid user name or password.  Remember that user name is not necessariy your email')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log a person out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))