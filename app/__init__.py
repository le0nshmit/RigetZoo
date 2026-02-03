from flask import Flask

def create_app():
    app = Flask(__name__)

    from .general import general_bp

    app.register_blueprint(general_bp)

    return app

 