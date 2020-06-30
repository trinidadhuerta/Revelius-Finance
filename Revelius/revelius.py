"""
Module Docstring
"""

__author__ = "Trinidad Huerta"
__version__ = "0.1.0"
__license__ = "MIT"

from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'thisisasecret' #this needs to be actually a random key

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()