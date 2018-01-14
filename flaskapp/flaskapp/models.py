"""A user login system"""
class Account(object):
    """register new users and login existing ones"""

    # constructor (new object of the class instantiated.)
    def __init__(self):
        # dicts placeholder
        self.accounts = []

    def adduser(self, username, email, password, confirm):
        """add a new user"""
        # dictionary to hold user's info
        self.registrant = dict()
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


class Lists(object):
    """keep user's lists"""

    # constructor
    def __init__(self):
        # placeholder for lists
        self.recipes = []

    def addrecipe(self, owner, title, procedures):
        """add a new recipe"""
        arecipe = dict()
        if title:
            counter = 1
            for i in self.recipes:
                counter += 1
                if i['id'] == counter:
                    counter += 1
            arecipe['title'] = title
            arecipe['id'] = counter
            arecipe['username'] = owner
            arecipe['procedures'] = procedures
            arecipe['shared'] = False
            arecipe['zone'] = ""
            self.recipes.append(arecipe)
            # return true
            return 1
        else:
            # return false
            return 0


    def mylists(self):
        """returns available recipes"""
        return self.recipes
