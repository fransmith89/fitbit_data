import os

from flask import Flask

from fitbit_data.blueprints.core import core_api


def create_app():
    app = Flask(__name__)
    app.config.update(load_config())
    app.register_blueprint(core_api)
    return app


def load_config():
    return {
        # debug reloads app on code changes
        # TODO: change default to False when we're done playing
        'DEBUG': os.environ.get('DEBUG', True)
    }
