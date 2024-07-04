# Initializes the Flask app.

from flask import Flask
from api.endpoints import persona
from flasgger import Swagger

from models import initialize_persons_db


def create_app():
    app = Flask(__name__)
    # Swagger configuration
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/docs/apispec_1.json',
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/docs/"
    }
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "My API",
            "description": "API documentation",
            "version": "1.0.0"
        },
        "basePath": "/",  # Base path for all API endpoints
    }

    # Initialize Swagger
    Swagger(app, config=swagger_config, template=swagger_template)

    # Register blueprints
    app.register_blueprint(persona.router, url_prefix='/')
    return app

def initialize_data():
    initialize_persons_db();
