from . import booking_bp
from flask import render_template

@booking_bp.route('/booking')
def booking():
    return render_template('booking/booking.html')