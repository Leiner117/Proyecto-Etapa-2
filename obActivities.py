class activities:
    def __init__(self,descripcion,course,date,start_time,end_time,status):
        self.decripcion = descripcion
        self.course = course
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
    def getDescripcion(self):
        return self.decripcion
    def getCourse(self):
        return self.course
    def getDate(self):
        return self.date
    def getStart_time(self):
        return self.start_time
    def getEnd_time(self):
        return self.end_time
    def getStatus(self):
        return self.status
    def setDescripcion(self,var):
        self.decripcion = var
    def setCourse(self,var):
        self.course = var
    def setDate(self,var):
        self.date = var
    def setStart_time(self,var):
        self.start_time = var
    def setEnd_time(self,var):
        self.end_time = var
    def setStatus(self,var):
        self.status = var