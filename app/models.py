# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

# [START model]

# Build secondary table for many to many between animals and persons
permissions = db.Table('permissions', 
    db.Column('animal_id', db.Integer, db.ForeignKey('animals.id')), 
    db.Column('person_id', db.Integer, db.ForeignKey('persons.id'))
)

# Build secondary table for many to many between facilities and persons
workers = db.Table('workers',
    db.Column('facility_id', db.Integer, db.ForeignKey('facilities.id')),
    db.Column('person_id', db.Integer, db.ForeignKey('persons.id'))
)

class Encounter(db.Model):
    __tablename__ = 'encounters'

    id = db.Column(db.Integer, primary_key=True)
    enc_date = db.Column(db.Date, index=True)
    person_id = db.Column(db.Integer, db.ForeignKey('persons.id'))
    animal_id = db.Column(db.Integer, db.ForeignKey('animals.id'))
    check_out_time = db.Column(db.DateTime)
    check_in_time = db.Column(db.DateTime)
    handling_time = db.Column(db.Integer)
    holding_time = db.Column(db.Integer)
    crate_time = db.Column(db.Integer)
    comments = db.Column(db.String(255))

    def __repr__(self):
        return"<Encounter(person='%s', animal='%s', date='%s')" % (self.person_id, self.animal_id, self.enc_date)

class Facility(db.Model):
    __tablename__='facilities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    description = db.Column(db.String(128))
    persons = db.relationship('Person', secondary='workers', backref='facilities', lazy = 'dynamic')

    def __repr__(self):
        return "<Facility name='%s')" % (self.name)

class Role(db.Model):
    __tablename__='roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    description = db.Column(db.String(128))

    def __repr__(self):
        return "<Role name='%s')" % (self.name)

    

class Person(UserMixin, db.Model):
    __tablename__ = 'persons'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(60), index=True)
    username = db.Column(db.String(60), index=True, unique=True)
    email = db.Column(db.String(80), index=True)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(60), index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_person_active = db.Column(db.Boolean, index=True)
    is_admin = db.Column(db.Boolean, default=False)
    comments = db.Column(db.String(255))
    animals = db.relationship('Animal', secondary='permissions', backref='persons', lazy = 'dynamic')
    #facility = db.Column(db.Integer, db.ForeignKey('facilities.id'))
    
    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<Person name='%s', '%s', '%s')" % (self.first_name, self.last_name, self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Person.query.get(int(user_id))

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
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    animal_type = db.Column(db.Integer, db.ForeignKey('animal_type.id'))
    animal_string = db.Column(db.Integer, db.ForeignKey('animal_string.id'))
    animal_status = db.Column(db.Integer, db.ForeignKey('animal_status.id'))
    animal_group = db.Column(db.Integer, db.ForeignKey('animal_group.id'))
    max_enc_per_day = db.Column(db.Integer)
    comments = db.Column(db.String(255))

    def __repr__(self):
        return "<Animal='%s')" % (self.name)