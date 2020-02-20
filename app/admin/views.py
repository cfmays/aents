# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import FacilityForm, RoleForm 
from .. import db
from ..models import Facility, Role, Encounter

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

