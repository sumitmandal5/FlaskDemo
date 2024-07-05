# Initializes the Flask app.

from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

from api.endpoints import persona
from models import initialize_persons_db


def create_app():
    app = Flask(__name__)
    ### swagger specific ###
    SWAGGER_URL = '/swagger'
    SWAGGER_RESOURCE = '/static/swagger.json'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        SWAGGER_RESOURCE,
        config={
            'app_name': "Flask_Demo_App"
        }
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    ### end swagger specific ###
    # Register blueprints
    app.register_blueprint(persona.router, url_prefix='/')

    return app


def initialize_data():
    initialize_persons_db();
