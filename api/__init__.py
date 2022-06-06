# -*- coding: utf-8 -*-
"""This module contains initialization code for the api package."""
from flask import Flask

from .blueprints.default.views import default
from .helpers import set_flask_environment

app = Flask(__name__)
app.register_blueprint(default)


set_flask_environment(app=app)
