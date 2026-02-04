from flask import Blueprint, render_template

booking_bp = Blueprint('booking', __name__, template_folder='templates')

from . import routes