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
    def Login(self, username, password, confirm):
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
