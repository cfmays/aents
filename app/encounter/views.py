# app/encounter/views.py

from flask import render_template
from flask_login import current_user, login_required

from .forms import OpenEncounterForm 

from . import encounter

from .forms import OpenEncounterForm
from .. import db
from ..models import Person, Facility, Role

@encounter.route('/open_new_encounter', methods=['GET', 'POST'])
@login_required
def open_new_encounter():
    """
    Open a new encounter
    """

    #facilities = Facility.query.all()
    form = OpenEncounterForm()
    return render_template('encounters/open_encounter.html', 
                           form=form,
                           title="Open New Encounter")
