# -*- coding: utf-8 -*-
"""This module has methods that are used in the other modules in this package."""

import os


def set_flask_environment(app) -> str:
    """Set the flask development environment.

    Parameters
    ----------
    app: flask.Flask
        The flask application object

    Raises
    ------
    KeyError
        If the FLASK_ENV environment variable is not set.

    Returns
    -------
    str:
        Flask operating environment i.e development

    """
    if os.environ['FLASK_ENV'] == 'production':  # pragma: no cover
        app.config.from_object('API.config.ProductionConfig')
    elif os.environ['FLASK_ENV'] == 'development':  # pragma: no cover
        app.config.from_object('API.config.DevelopmentConfig')
    elif os.environ['FLASK_ENV'] == 'test':
        app.config.from_object('API.config.TestingConfig')
    else:
        app.config.from_object('API.config.DevelopmentConfig')

    return os.environ['FLASK_ENV']
