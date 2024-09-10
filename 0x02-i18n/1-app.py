#!/usr/bin/env python3
"""
Basic Babel setup
"""
from flask import Flask, g, request
from flask_babel import Babel

app = Flask(__name__)
app.config-from_pyfile('mysettings.cfg')
babel = Babel(app)


class Config:
    """
    creating a locale
    """
    LANGUAGES = ['en', 'fr']

    @babel.localeselector
    def get_locale():
        """
        making 'en' a default locale
        """
        if user is not None:
            return user.locale
        return request.accept_languaes.best_match(['en'])

    @babel.timezoneselector
    def get_timezone():
        """
        UTC default timezone
        """
        user = getattr(g, 'user', None)
        if user is not None:
            return user.timezone
