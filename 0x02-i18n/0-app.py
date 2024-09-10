#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
