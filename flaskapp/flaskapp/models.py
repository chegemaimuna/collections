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

"""Lists"""
class Lists(object):
    """keep user's lists"""

    # constructor
    def __init__(self):
        # placeholder for lists
        self.lists = []
        # placeholder for list info(components)
        self.alist = dict()

    def add_list(self, username, list_name):
        """Adds a new list"""
        if list_name:
            if len(self.lists) == 0:
                pk = 1
            else:
                pk = int(self.lists[-1]['id']) + 1
            alist["list_name"] = list_name
            alist["id"] = pk
            alist["username"] = username
            alist["shared"] = False
            alist["zone"] = ""
            self.lists.append(alists)
            return "success"
        else:
            return "null_list"
    # returns a list for a user
    def mylists(self):
        return self.lists

    #handle shopping list sharing and unsharing
    def share_shoppinglist(self, list_id):
        counter=0
        for i in self.shoppinglists:
            if int(i['id'])==int(list_id):
                if i['shared']==False:
                    self.shoppinglists[counter]['shared']=True
                    return "success"
                else:
                    self.shoppinglists[counter]['shared']=False
                    return "success"
            counter=counter+1

        return "error"
    #handle updates on shoppinglist name
    def update_shoppinglist(self, list_id, new_name):
        counter=0
        for i in self.shoppinglists:
            if int(i['id'])==int(list_id):
                self.shoppinglists[counter]['name']=new_name
                return "success"
            counter=counter+1

        return "error"

    #handle updates on shoppingzone
    def update_zone(self, list_id, szone):
        counter=0
        for i in self.shoppinglists:
            if int(i['id'])==int(list_id):
                self.shoppinglists[counter]['zone']=szone
                return "success"
            counter=counter+1

        return "error"

    def delete_list(self, list_id):
        counter=0
        for i in self.shoppinglists:
            if int(i['id'])==int(list_id):
                self.shoppinglists.pop(counter)
                return "success"
            counter=counter+1
        return "error"