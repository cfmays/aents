# app/encounter/views.py

from flask import flash, render_template
from flask_login import current_user, login_required

from . import encounter

from .forms import OpenEncounterForm, OpenEncounterFormFacility
from .. import db
from ..models import Person, Facility, Role, Animal, Encounter

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

    if form.validate_on_submit():
        # build the datetime
        start_datetime = form.start_date.data.strftime('%Y-%m-%d') + ' ' + form.start_time.data.strftime('%H:%M')
        print('HERE is the datetime:  ', start_datetime)
        encounter = Encounter(person_id = form.person_id.data,
                                animal_id=form.animal_id.data,
                                check_out_time=start_datetime)
        # add encounter to the database
        db.session.add(encounter)
        db.session.commit()
        flash('You have successfully opened a new encounter.')

    return render_template('encounters/open_encounter_facility.html', 
                           form=form,
                           title="Open New Encounter")
