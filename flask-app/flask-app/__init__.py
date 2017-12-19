"""Import objects"""
from flask import Flask, render_template, url_for, request, flash

APP = Flask(__name__)

APP.config['SECRET_KEY'] = 'zyxwvutsrqponmlkj'

@APP.route("/")
def index():
    """Root - display homepage"""
    return render_template("index.html")

@APP.route("/login")
def login():
    """Display login form"""
    return render_template("login.html")

@APP.route("/signup", methods=['GET', 'POST'])
def signup():
    """Display signup form"""
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        confirm = request.form['confirm']
    
        if username.isapha() != True:
            flash("something went wrong!")
            render_template("signup.html")
    else:

        return render_template("signup.html")

@APP.route("/dashboard")
def dashboard():
    """Display logged in user's recipes"""
    flash("testing!")
    return render_template("dashboard.html")

@APP.route("/edit")
def edit():
    """Display a form to add or edit recipes"""
    return render_template("edit.html")

@APP.route("/view")
def view():
    """Display a certain user's recipe"""
    return render_template("view.html")

if __name__ == '__main__':
    APP.run(debug=True)
