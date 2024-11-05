#!usr/bin/env python3
""" A simple i18n enabled Flask app """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """ Class for custom app configurations """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
# Load attributes in Config class into app
app.config.from_object(Config)

# Instantiate Babel instance
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Gets client's locale """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home():
    render_template("2-index.html")


if __name__ == "__main__":
    """ Start Flask app """
    app.run()
