"""Import objects"""
import re
import urllib
from flask import render_template, url_for, request, flash, redirect, session
from flaskapp import APP
from flaskapp.models import *

from flaskapp.helpers import *

# an instance of Account class (responsible for user registration and login)
REGISTRANT = Account()
LIST = Lists()

@APP.route("/")
def index():
    """Root - display homepage"""
    return render_template("index.html")

@APP.route("/login", methods=['POST', 'GET'])
def login():
    """Display login form and check for details"""
    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        # server side validation for users that might bypass
        # javascript check by disabling it in their browser
        if username == "" or password == "":
            return apology("please input required details")
        login_rigistrant = REGISTRANT.login(username, password)
        if login_rigistrant is True:
            session["username"] = username
            return redirect(url_for('dashboard', username=session["username"]))
        elif login_rigistrant is False:
            return apology("please check your details and try again")

    else:
        return render_template("login.html")

@APP.route("/signup", methods=['GET', 'POST'])
def signup():
    """Display signup form and add new registrant"""
    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # collect the submited data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm = request.form['confirm']

        # server side validation for users that might bypass
        # javascript check by disabling it in their browser
        #if username == "" or email == "" or password == "" or confirm == "":
        #    flash("please enable javascript in your broswer!")
        #    return render_template("signup.html")
        # check for correct email format
        # check whether email has exactly one @ sign, and at least one . in the part after the @
        #if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
         #   return apology("please check your email format and try again")
        #if len(password) < 8 or not re.search(r"\d" and r"[A-Z]" and r"[a-z]" and r"\W", password):
        #    return apology("password need 8 characters, digits, uppercase, lowercase and symbol")
        #else:
        signup_registrant = REGISTRANT.adduser(username, email, password, confirm)
        if signup_registrant is True:
            return redirect(url_for('dashboard'))
        elif signup_registrant is False:
            return apology("email or username exists")
        elif signup_registrant == "pass_fail":
            return apology("password mismatch!")
    else:
        return render_template("signup.html")

@APP.route("/logout")
@login_required
def logout():
    """Log user out."""

    # forget any username
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))

@APP.route("/dashboard", methods=['GET'])
@login_required
def dashboard():
    available_recipes = LIST.mylists()
    """Display logged in user's recipes"""
    for i in available_recipes:
        if i['username'] == session['username']:
            return render_template("dashboard.html", username=session['username'], available_recipes=available_recipes)
    return render_template("dashboard.html")

@APP.route("/addrecipe", methods=['GET', 'POST'])
@login_required
def addrecipe():
    """Adds a new lists"""
    # if user reached route via POST (as by submitting a form via POST)
    if request.method == 'POST':
        owner = session["username"]
        title = request.form['title']
        procedures = request.form['procedures']
        # add a recpe to recipes
        addrecipe = LIST.addrecipe(owner, title, procedures)
        if addrecipe == True:
            available_recipes = LIST.mylists()
            return render_template("dashboard.html", username=session["username"], available_recipes=available_recipes)
        elif addrecipe == False:
            return apology("please enter required details")
    elif request.method == 'GET':
        return render_template('add.html')



@APP.route("/edit/<id>", methods=['GET', 'POST'])
@login_required
def edit(id):
    """Display a form to add or edit recipes"""
    recipes = LIST.mylists()
    if request.method == 'POST': 
        for idx, item in enumerate(recipes):
            if item['id'] == int(id):
               holder = dict()
               holder['id'] = int(id)
               holder['title'] = request.form['title']
               holder['procedures'] = request.form['procedures']
               holder['username'] = session['username']
               recipes[idx] = holder
               return redirect(url_for('dashboard'))
    elif request.method == 'GET':
	    for j in recipes:
	    	if j['id'] == int(id):
	    		title = j['title']
	    		procedures = j['procedures']
	    		return render_template("edit.html", id=id, title=title, procedures=procedures)
    return render_template("edit.html", id=id)

@APP.route("/review/<id>")
@login_required
def review(id):
    """review a certain recipe"""
    recipelist = LIST.mylists()
    for i in recipelist:
        if i['id'] == int(id):
            recipename = i['title']
            procedures = i['procedures']
            return render_template("view.html", id=id, recipename=recipename, procedures=procedures)
    return render_template("view.html")

@APP.route("/view")
@login_required
def view():
    """Display a certain user's recipe"""
    return render_template("view.html")

@APP.route('/delete/<id>')
@login_required
def delete(id):
	recipe = LIST.mylists()
	for i, d in enumerate(recipe):
		if d['id'] == int(id):
			recipe.pop(i)
			return redirect(url_for('dashboard'))
			break

