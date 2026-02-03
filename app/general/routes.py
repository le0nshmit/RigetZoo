from . import general_bp
from flask import render_template

@general_bp.route('/')
def index():
    return render_template('general/index.html')