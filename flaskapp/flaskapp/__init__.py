"""Import objects"""
from flask import Flask

APP = Flask(__name__)

# Note: views import done after app initialization
import flaskapp.views
from flaskapp import models

APP.config['SECRET_KEY'] = 'zyxwvutsrqponmlkj0987654321'



if __name__ == '__main__':
    APP.run(debug=True)
