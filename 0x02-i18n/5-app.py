#!/usr/bin/env python3
""" A simple i18n enabled Flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel


# Mock database user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ Class for custom app configurations """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)  # Load attributes in Config class into app

babel = Babel(app)  # Instantiate Babel instance


def get_user():
    """ Gets logged in user """
    user_id = request.args.get('login_as')
    if not user_id:
        return None
    return users.get(int(user_id))


@app.before_request
def before_request():
    """ Sets global user object """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """ Gets client's locale """
    # Check if 'locale' is in query parameters
    lang = request.args.get('locale')
    if lang in app.config["LANGUAGES"]:
        return lang

    # Fall back to the best match from 'Accept Languages' header
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def home():
    """ Renders the homepage """
    return render_template('5-index.html')


if __name__ == "__main__":
    """ Starts the application """
    app.run()
