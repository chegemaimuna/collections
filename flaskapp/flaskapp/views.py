"""Import objects"""
from flask import render_template, url_for, request, flash, jsonify
from flaskapp import APP

# user login sytem
class Account(object):

    # constructor (new object of the class instantiated.)
    def __init__(self):
        self.accounts = []

    # add a new user
    def Adduser(self, username, email, password, confirm):
        registrant = {}
        found = False
        if password == confirm:
            for someone in self.accounts:
                if username == someone['username'] or email == someone['email']:
                        found = True
                        break
            if found == False:
                registrant['username'] = username
                registrant['email'] = email
                registrant['password'] = password
                self.accounts.append(registrant)
                return "success"
            else:
                return "exists"
        else:
            return "pass_fail"
    # Login existing users
    def Login(self, username, password):
        # server side validation for users that might bypass javascript check
        if username == "" or password == "":
            return '<h1>Please input the required details!</h1>'
        elif username and password:
            # check if user exists
            for registrant in self.accounts:
                if username == registrant['username'] and password == registrant['password']:
                    return "success"
        else:
            return "fail"

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
        acc = Account()

        signup = acc.Adduser(username, email, password, confirm)
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
