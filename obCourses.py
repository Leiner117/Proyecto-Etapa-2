class course():
    def __init__(self,name,credits,start_date,end_date,status):
        self.name = name
        self.credits = credits
        self.shool_hours = credits*3
        self.start_date = start_date
        self.end_date = end_date
        self.class_time = []
        self.careers_belong = []
        self.status = status
    #gets
    def getName(self):
        return self.name
    def getCredits(self):
        return self.credits
    def getSchool_hours(self):
        return self.shool_hours
    def getStart_date(self):
        return self.start_date
    def getEnd_date(self):
        return self.end_date
    def getClass_time(self):
        return self.class_time
    def getCareers_belong(self):
        return self.careers_belong
    def getStatus(self):
        return self.status
    
    #sets
    def setName(self,name):
        self.name = name
    def setCredits(self,credits):
        self.credits = credits
    def setSchool_hours(self,school_hours):
        self.shool_hours = school_hours
    def setStart_date(self,start_date):
        self.start_date = start_date
    def setEnd_date(self,end_date):
        self.end_date = end_date
    def setClass_time(self, class_time):
        self.class_time = class_time
    def setCareers_belong(self,careers_belong):
        self.careers_belong = careers_belong
    def setStatus(self,status):
        self.status = status
    