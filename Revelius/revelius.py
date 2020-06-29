"""
Module Docstring
"""
__author__ = "Trinidad Huerta"
__version__ = "0.1.0"
__license__ = "MIT"

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'