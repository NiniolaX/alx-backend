#!/usr/bin/env python3
""" A simple i18n enabled Flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone
import pytz


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
    """ Determines the best locale to use for request """
    # Priority 1: Locale from URL parameters
    lang = request.args.get('locale')
    if lang in app.config["LANGUAGES"]:
        return lang

    # Priority 2: Locale from user settings
    user = g.user
    if user and user.get('locale') in app.config["LANGUAGES"]:
        return user['locale']

    # Priority 3: Locale from `Accept languages` request header
    best_match = request.accept_languages.best_match(app.config["LANGUAGES"])
    if best_match:
        return best_match

    # Priority 4: Default locale
    return app.config["BABEL_DEFAULT_LOCALE"]


def valid_timezone(timezone: str) -> bool:
    """ Validates a given timezone """
    try:
        timezone(timezone)
        return True
    except pytz.exceptions.UnknownTimeZoneError:
        return False


@babel.timezoneselector
def get_timezone():
    """ Sets user timezone """
    # Check for timezone in URL parameters
    timezone_name = request.args.get('timezone')
    if valid_timezone(timezone_name):
        return timezone_name

    # Check for timezone in user settings
    user = g.user
    if user and user.get('timezone'):
        if valid_timezone(user['timezone']):
            return user['timezone']

    # Default to UTC
    return 'UTC'


@app.route("/")
def home():
    """ Renders the homepage """
    return render_template('7-index.html')


if __name__ == "__main__":
    """ Starts the application """
    app.run()
