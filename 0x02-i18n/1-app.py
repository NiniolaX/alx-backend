#!/usr/bin/env python3
""" A simple i18n enabled Flask app """
from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """ Class for custom configurations of app """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)  # Load attributes in Config class into app

babel = Babel(app)  # Instantiate Babel


@app.route("/")
def home():
    """ Renders the homepage """
    return render_template("1-index.html")


if __name__ == "__main__":
    """ Start Flask app """
    app.run()
