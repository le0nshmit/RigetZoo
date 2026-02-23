from . import general_bp
from flask import render_template

@general_bp.route('/')
def index():
    return render_template('index.html')


@general_bp.route('/booking')
def booking():
    return render_template('booking.html')