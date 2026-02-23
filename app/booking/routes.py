from . import booking_bp
from flask import render_template
from .booking import initiliase_database

@booking_bp.route('/zoo')
def zoo():
    return render_template('booking/booking-zoo.html')

