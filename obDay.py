'''
dia
		numero del dia 
		fecha exacta
		horas dia
		porcentaje
		lista actividades
'''
class days:
    def __init__(self,num_Day,date):
        self.num_day = num_Day
        self.date = date
        self.hours = 0
        self.percentaje = 0
        self.list_activities = []
        
    def getNum_day(self):
        return self.num_day
    def getDate(self):
        return self.date
    def getHours(self):
        return self.hours
    def getPercentaje(self):
        return self.percentaje
    def getList_actvities(self):
        return self.list_activities
    def setNum_day(self,var):
        self.num_day = var
    def setDate(self,var):
        self.date = var
    def setHours(self,var):
        self.hours = var
    def setpercentaje(self,var):
        self.percentaje = var
    def setlist_activies(self,var):
        self.list_activities = var