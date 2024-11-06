#!/usr/bin/env python3
""" A simple i18n enabled Flask app """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Class for custom app configurations """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)  # Load attributes in Config class into app

babel = Babel(app)  # Instantiate Babel instance


@babel.localeselector
def get_locale():
    """ Get client's locale """
    lang = request.accept_languages.best_match(app.config["LANGUAGES"])
    return lang


@app.route("/")
def home():
    """ Renders the homepage """
    return render_template('3-index.html')


if __name__ == "__main__":
    """ Starts the application """
    app.run(debug=True)
