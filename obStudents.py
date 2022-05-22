class students:
    def __init__(self,name,email,career,password):
        self.name = name
        self.email = email
        self.career = career
        self.password = password
        self.courses = []
        self.shedule = []
        self.activities = []
    def getName(self):
        return self.name
    def getEmail(self):
        return self.email
    def getCareer(self):
        return self.career
    def getPassword(self):
        return self.password
    def getCourses(self):
        return self.courses
    def getActivities(self):
        return self.activities
    def getShedule(self):
        return self.shedule
    def setName(self,name):
        self.name = name
    def setEmail(self,email):
        self.email = email
    def setCareer(self,career):
        self.career = career
    def setPassword(self,password):
        self.password = password
    def setCourses(self,courses):
        self.courses = courses
    def setActivities(self,activities):
        self.activities = activities
          
    