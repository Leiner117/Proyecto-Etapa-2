class hours_class:
    def __init__(self,day,start_time,end_time):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
    def getDay(self):
        return self.day
    def getStart_time(self):
        return self.start_time
    def getEnd_time(self):
        return self.end_time
    def setDay(self,day):
        self.day = day
    def setStart_time(self,start_time):
        self.start_time = start_time
    def setEnd_time(self,end_time):
        self.end_time = end_time
    def __str__(self):
        return f"[{self.day},{self.start_time},{self.end_time}]"
