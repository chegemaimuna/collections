"""Import objects"""
from flask import render_template, url_for, request, flash, jsonify, redirect
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
        # server side validation for users that might bypass javascript check by disabling it in their browser
        if username == "" or password == "":
            return '<h1>Please input the required details!</h1>'
        login = registrant.login(username, password)
        
        if login is True:
             return redirect(url_for('dashboard'))
        elif login is False:
            flash("error", "error")
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

        # server side validation for users that might bypass javascript check by disabling it in their browser
        if username == "" or email == "" or password == "" or confirm == "":
            return '<h1>Error! please input required data</h1>'
        signup = registrant.adduser(username, email, password, confirm)
        if signup is True:
            return redirect(url_for('dashboard'))
        elif signup is False:
            flash("email or username exists")
            return render_template("signup.html")
        elif signup == "pass_fail":
            flash("password mismatch!")
            return render_template("signup.html")
    else:
        return render_template("signup.html")

@APP.route("/dashboard")
def dashboard():
    """Display logged in user's recipes"""
    return render_template("dashboard.html")

@APP.route("/edit")
def edit():
    """Display a form to add or edit recipes"""
    return render_template("edit.html")

@APP.route("/view")
def view():
    """Display a certain user's recipe"""
    return render_template("view.html")
