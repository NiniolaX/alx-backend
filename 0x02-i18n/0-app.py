#!usr/bin/env python3
""" Flask app for i18n project """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """ Returns the home page """
    return render_template("0-index.html")


if __name__ == "__main__":
    """ Start the Flask app """
    app.run()
