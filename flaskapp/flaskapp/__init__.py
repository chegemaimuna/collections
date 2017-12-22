"""Import objects"""
from flask import Flask

APP = Flask(__name__)

# Note: views import done after app initialization
import flaskapp.views

APP.config['SECRET_KEY'] = 'zyxwvutsrqponmlkj'


if __name__ == '__main__':
    APP.run(debug=True)
