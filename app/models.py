# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

# [START model]

# Build secondary table for many to many between animals and persons
permissions = db.Table('permissions',
    db.Column('animal_id', db.Integer, db.ForeignKey('animal.animal_id')), 
    db.Column('person_id', db.Integer, db.ForeignKey('person.person_id'))
)

# Build secondary table for many to many between facilities and persons
workers = db.Table('workers',
    db.Column('facility_id', db.Integer, db.ForeignKey('facility.facility_id'))
    db.Column('person_id', db.Integer, db.ForeignKey('person.person_id'))
)

class Encounter(db.Model):
    __tablename__ = 'encounters'

    id = db.Column(db.Integer, primary_key=True)
    enc_date = db.Column(db.Date, index=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    animal_id = db.Column(db.Integer, db.ForeignKey('animals.id'))
    check_out_time = db.Column(db.DateTime)
    check_in_time = db.Column(db.DateTime)
    handling_time = db.Column(db.Integer)
    holding_time = db.Column(db.Integer)
    crate_time = db.Column(db.Integer)
    comments = db.Column(db.string(255))

    def __repr__(self):
        return"<Encounter(person='%s', animal='%s', date='%s')" % (self.person_id, self.animal_id, self.enc_date)

class Facility(db.Model):
    __tablename__='facilities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    persons = db.relationship('Person', secondary='workers', backref='facilities', lazy = 'dynamic')

    def __repr__(self):
        return "<Facility name='%s')" % (self.name)

class Person(db.Model):
    __tablename__ = 'persons'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(60), index=True)
    first_name = db.Column(db.String(60), index=True)
    role = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_active = db.Column(db.Boolean, index=True)
    comments = db.Column(db.string(255))
    animals = db.relationship('Animal', secondary='permissions', backref='persons', lazy = 'dynamic')
    
    def __repr__(self):
        return "<Person name='%s', '%s')" % (self.first_name, self.last_name)

class Animal_Type(db.Model):
    __tablename__ = 'animal_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    animals = db.relationship('Animal')

    def __repr__(self):
        return "<Animal type='%s')" % (self.name)

class Animal_String(db.Model):
    __tablename__ = 'animal_string'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24))
    animals = db.relationship('Animal')
    
    def __repr__(self):
        return "<Animal string='%s')" % (self.name)

class Animal_Status(db.Model):
    __tablename__ = 'animal_status'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24))

    def __repr__(self):
        return "<Animal status='%s')" % (self.name)

class Animal_Group(db.Model):
    __tablename__ = 'animal_group'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24))
    animals = db.relationship('Animal')

    def __repr__(self):
        return "<Animal group='%s')" % (self.name)
 

class Animal(db.Model):
    __tablename__ = 'animal'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    animal_type = db.Column(db.Integer, db.ForeignKey('Animal_Type.id'))
    animal_string = db.Column(db.Integer, db.ForeignKey('Animal_String.id'))
    animal_status = db.Column(db.Integer, db.ForeignKey('Animal_Status.id'))
    animal_group = db.Column(db.Integer, db.ForeignKey('Animal_Group.id'))
    max_enc_per_day = db.Column(db.Integer)
    comments = db.Column(db.string(255))

    def __repr__(self):
        return "<Animal='%s')" % (self.name)