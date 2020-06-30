"""
Module Docstring
"""

__author__ = "Trinidad Huerta"
__version__ = "0.1.0"
__license__ = "MIT"

from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()