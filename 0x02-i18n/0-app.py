#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():
    """
    Basic Flask app
    """
    return render_template('0-index.html',)


if __name__ == "__main__":
    app.run(debug=True)
