# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import FacilityForm, RoleForm, AnimalForm
from .. import db
from ..models import Facility, Role, Encounter, Animal

def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)


# Facility Views


@admin.route('/facilities', methods=['GET', 'POST'])
@login_required
def list_facilities():
    """
    List all facilities
    """
    check_admin()

    facilities = Facility.query.all()

    return render_template('admin/facilities/facilities.html',
                           facilities=facilities, title="Facilities")


@admin.route('/facilities/add', methods=['GET', 'POST'])
@login_required
def add_facility():
    """
    Add a facility to the database
    """
    check_admin()

    add_facility= True

    form = FacilityForm()
    if form.validate_on_submit():
        facility = Facility(name=form.name.data,
                                description=form.description.data)
        try:
            # add facility to the database
            db.session.add(facility)
            db.session.commit()
            flash('You have successfully added a new facility.')
        except:
            # in case facility name already exists
            flash('Error: facility name already exists.')

        # redirect to facilities page
        return redirect(url_for('admin.list_facilities'))

    # load facility template
    return render_template('admin/facilities/facility.html', action="Add",
                           add_facility=add_facility, form=form,
                           title="Add Facility")


@admin.route('/facility/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_facility(id):
    """
    Edit a facility
    """
    check_admin()

    add_facility = False

    facility = Facility.query.get_or_404(id)
    form = FacilityForm(obj=facility)
    if form.validate_on_submit():
        facility.name = form.name.data
        facility.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the facility.')

        # redirect to the facilities page
        return redirect(url_for('admin.list_facilities'))

    form.description.data = facility.description
    form.name.data = facility.name
    return render_template('admin/facilities/facility.html', action="Edit",
                           add_facility=add_facility, form=form,
                           facility=facility, title="Edit Facility")


@admin.route('/facilities/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_facility(id):
    """
    Delete a facility from the database
    """
    check_admin()

    facility = Facility.query.get_or_404(id)
    db.session.delete(facility)
    db.session.commit()
    flash('You have successfully deleted the facility.')
    # cfm ask to delete all that facilities' users?

    # redirect to the facilities page
    return redirect(url_for('admin.list_facilities'))

    return render_template(title="Delete Facility")

# Role Views

@admin.route('/roles')
@login_required
def list_roles():
    check_admin()
    """
    List all roles
    """
    roles = Role.query.all()
    return render_template('admin/roles/roles.html',
                           roles=roles, title='Roles')


@admin.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
    """
    Add a role to the database
    """
    check_admin()

    add_role = True

    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data,
                    description=form.description.data)

        try:
            # add role to the database
            db.session.add(role)
            db.session.commit()
            flash('You have successfully added a new role.')
        except:
            # in case role name already exists
            flash('Error: role name already exists.')

        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))

    # load role template
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title='Add Role')


@admin.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):
    """
    Edit a role
    """
    check_admin()

    add_role = False

    role = Role.query.get_or_404(id)
    form = RoleForm(obj=role)
    if form.validate_on_submit():
        role.name = form.name.data
        role.description = form.description.data
        db.session.add(role)
        db.session.commit()
        flash('You have successfully edited the role.')

        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))

    form.description.data = role.description
    form.name.data = role.name
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title="Edit Role")


@admin.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
    """
    Delete a role from the database
    """
    check_admin()

    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have successfully deleted the role.')

    # redirect to the roles page
    return redirect(url_for('admin.list_roles'))

    return render_template(title="Delete Role")

@admin.route('/people')
@login_required
def list_people():
    check_admin()
    """
    List all people at this facility
    """
    roles = Role.query.all()
    return render_template('admin/roles/roles.html',
                           roles=roles, title='Roles')

@admin.route('/animals', methods=['GET', 'POST'])
@login_required
def list_animals():
    """
    List all animals
    """
    check_admin()

    animals = Animal.query.all()

    return render_template('admin/animals/animals.html',
                           animals=animals, title="Animals")

@admin.route('/animals/add', methods=['GET', 'POST'])
@login_required
def add_animal():
    """
    Add an animal to the database
    """
    check_admin()

    add_animal = True

    form = AnimalForm()
    if form.validate_on_submit():
        animal = Animal(name=form.name.data)

        try:
            # add animal to the database
            db.session.add(animal)
            db.session.commit()
            flash('You have successfully added a new animal.')
        except:
            # in case animal name already exists
            flash('Error: animal name already exists.')

        # redirect to the animals page
        return redirect(url_for('admin.list_animals'))

    # load animal template
    return render_template('admin/animals/animal.html', add_animal=add_animal,
                           form=form, title='Add Animal')


@admin.route('/animals/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_animal(id):
    """
    Edit an animal
    """
    check_admin()

    add_animal = False

    animal = Animal.query.get_or_404(id)
    form = AnimalForm(obj=animal)
    if form.validate_on_submit():
        animal.name = form.name.data
        db.session.add(animal)
        db.session.commit()
        flash('You have successfully edited the animal.')

        # redirect to the animals page
        return redirect(url_for('admin.list_animals'))

    form.name.data = animal.name
    return render_template('admin/animals/animal.html', add_animal=add_animal,
                           form=form, title="Edit Animal")


@admin.route('/animals/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_animal(id):
    """
    Delete an animal from the database
    """
    check_admin()

    animal = Animal.query.get_or_404(id)
    db.session.delete(animal)
    db.session.commit()
    flash('You have successfully deleted the animal.')

    # redirect to the animals page
    return redirect(url_for('admin.list_animals'))

    return render_template(title="Delete Animal")