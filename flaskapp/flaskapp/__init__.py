"""Import objects"""
from flask import Flask, session
#from flask_session import Session
from tempfile import mkdtemp

# configure application
APP = Flask(__name__)

# Note: views import done after APP initialization
import flaskapp.views

APP.config.update(
    DEBUG=True,
    SECRET_KEY='@Dinos2B@PandasNot@Sloths'
)
# ensure responses aren't cached
if APP.config["DEBUG"]:
    @APP.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# configure session to use filesystem (instead of signed cookies)
APP.config["SESSION_FILE_DIR"] = mkdtemp()
APP.config["SESSION_PERMANENT"] = False
APP.config["SESSION_TYPE"] = "filesystem"
#Session(APP)

if __name__ == '__main__':
    APP.run(debug=True)
