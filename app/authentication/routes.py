from flask import render_template
from . import authentication_bp

@authentication_bp.route('/auth')
def authentication():
    return render_template('authentication.html')