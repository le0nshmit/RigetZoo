from flask import Flask

def create_app():
    app = Flask(__name__)

    from .general import general_bp
    from .booking import booking_bp

    app.register_blueprint(general_bp)
    app.register_blueprint(booking_bp, url_prefix='/booking')


    return app

 