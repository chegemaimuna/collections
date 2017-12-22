"""Import objects"""
from flask import render_template, url_for, request, flash, jsonify
from flaskapp import APP
from flaskapp import models

# an instance of Account class (responsible for user registration and login)
registrant = models.Account()

@APP.route("/")
def index():
    """Root - display homepage"""
    return render_template("index.html")

@APP.route("/login", methods=['POST', 'GET'])
def login():
    """Display login form and check for details"""
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        acc = Account()
        login = acc.Login(username, password)
        
        if login == "success":
             return render_template('dashboard.html')
        else:
            return render_template('login.html')

    else:
        return render_template("login.html")

@APP.route("/signup", methods=['GET', 'POST'])
def signup():
    """Display signup form and add new registrants"""
    if request.method == "POST":
        # collect the submited data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm = request.form['confirm']

        # check for empty input bypass(if user disables javascript in the browser)
        #if username == "" or email == "" or password == "" or confirm == "":
        #    return '<h1>Error! please input required data</h1>'
        #else:
            # create an instance of the class Account to play with.

        signup = registrant.Adduser(username, email, password, confirm)
        if signup == "success":
            return '<h1>success</h1>'
        elif signup == "exists":
            return '<h1>User exists</h1>'
        elif signup == "pass_fail":
            return '<h1>password mismatch!</h1>'
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
