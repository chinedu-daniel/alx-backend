#!/usr/bin/env python3
"""
Basic Babel setup
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)


class Config:
    """
    creating a locale
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

    @babel.localeselector
    def get_locale():
        """
        use the locale from the user settings
        """
        return request.accept_languages.best_match(app.config["LANGUAGES"])


app.config.from_object(Config)


@app.route('/', methods=["GET"])
def home():
    """home route serving the default page"""
    return render_template("0-index.html",)


if __name__ == "__main__":
    app.run(debug=True)
