"""A user login system"""
class Account(object):
    """Handles registration of new users and login existing ones"""

    # constructor (new object of the class instantiated.)
    def __init__(self):
        self.accounts = []

    def adduser(self, username, email, password, confirm):
        """add a new user"""
        registrant = {}
        found = False
        if password == confirm:
            for someone in self.accounts:
                if username == someone['username'] or email == someone['email']:
                    found = True
                    break
            if found is False:
                registrant['username'] = username
                registrant['email'] = email
                registrant['password'] = password
                self.accounts.append(registrant)
                return "success"
            else:
                return "exists"
        else:
            return "pass_fail"
    def login(self, username, password):
        """login an existing user"""
        for registrant in self.accounts:
            if username == registrant['username'] and password == registrant['password']:
                return "success"
        else:
            return "fail"
