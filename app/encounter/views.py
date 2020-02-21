# app/encounter/views.py

from flask import render_template
from flask_login import current_user, login_required

from . import encounter

from .forms import OpenEncounterForm, OpenEncounterFormFacility
from .. import db
from ..models import Person, Facility, Role, Animal

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


@encounter.route('/open_new_encounter_facility', methods=['GET', 'POST'])
@login_required
def open_new_encounter_facility():
    """
    Open a new encounter for a faciity-wide login (choose person from dropdown)
    """
    form = OpenEncounterFormFacility()
    form.person_id.choices = [(p.id, p.username) for p in Person.query.order_by('username')]
    form.animal_id.choices = [(a.id, a.name) for a in Animal.query.order_by('name')]
    return render_template('encounters/open_encounter_facility.html', 
                           form=form,
                           title="Open New Encounter")
#form.facility_id.choices = [(f.id, f.name) for f in Facility.query.order_by('name')]