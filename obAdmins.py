class admins():
    def __init__(self,name,password,phone_number):
        self.name = name
        self.password = password
        self.phone = phone_number
        
    def getName(self):
        return self.name
    def getPassword(self):
        return self.password
    def getPhone(self):
        return self.phone
    def setName(self,name):
        self.name = name
    def setPassword(self,password):
        self.password = password
    def setPhone(self,phone):
        self.phone = phone