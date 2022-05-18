class weeks:

    def __init__(self,num_month):
        self.num_month = num_month
        self.hours_week = 0
        self.percentage = 0
        self.list_days = []
    def getNum_month(self):
        return self.num_month
    def getHours_weeks(self):
        return self.hours_week
    def getPercentaje(self):
        return self.percentage
    def getList_days(self):
        return self.list_days
    def setNum_month(self,num_month):
        self.num_month = num_month
    def setHours_week(self,hours_week):
        self.hours_week = hours_week
    def setPercentaje(self,percentaje):
        self.percentage = percentaje
    def setList_days(self,list_days):
        self.list_days = list_days