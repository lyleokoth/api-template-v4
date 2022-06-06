# -*- coding: utf-8 -*-
"""This module executes the application."""

from flask.cli import FlaskGroup

from api import app

cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()
