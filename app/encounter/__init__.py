# app/encounter/__init__.py

from flask import Blueprint

encounter = Blueprint('encounter', __name__)

from . import views