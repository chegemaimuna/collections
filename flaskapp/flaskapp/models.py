"""A user login system"""
class Account(object):
    """register new users and login existing ones"""

    # constructor (new object of the class instantiated.)
    def __init__(self):
        # dicts placeholder
        self.accounts = []
        # dictionary to hold user's info
        self.registrant = dict()

    def adduser(self, username, email, password, confirm):
        """add a new user"""
        found = 0
        if password == confirm:
            for someone in self.accounts:
                if username == someone['username'] or email == someone['email']:
                    found = 1
                    break
            if found is 0:
                self.registrant['username'] = username
                self.registrant['email'] = email
                self.registrant['password'] = password
                self.accounts.append(self.registrant)
                return True
            else:
                return False
        else:
            return "pass_fail"
    def login(self, username, password):
        """login an existing user"""
        for registrant in self.accounts:
            if username in registrant['username'] and password in registrant['password']:
                return True
        else:
            return False
