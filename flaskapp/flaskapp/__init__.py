"""Import objects"""
from flask import Flask

#  create an instance of the Flask class 
APP = Flask(__name__)

# Note: views import done after app initialization
import flaskapp.views
from flaskapp import models

APP.config.update(
    DEBUG=True,
    SECRET_KEY='@Dinos2B@PandasNot@Sloths'
)

if __name__ == '__main__':
    APP.run(debug=True)
