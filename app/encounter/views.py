# app/encounter/views.py

from flask import render_template
from flask_login import current_user, login_required

from .forms import OpenEncounterForm

from . import encounter

from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import Person, Facility, Role

@encounter.route('/open_encounter', methods=['GET', 'POST'])
def open_encounter():
    """
    Render the open_encounter template on the / route
    """
    form = OpenEncounterForm
    return render_template('encounter/open_encounter.html', title="Open Encounter")
