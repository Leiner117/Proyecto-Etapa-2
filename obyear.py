class years:
    def __init__(self,date_year):
        self.date_year = date_year
        self.list_months = []
    def getDate_year(self):
        return self.date_year
    def getList_months(self):
        return self.list_months
    def setList_months(self,list_months):
        self.list_months = list_months
    def setDate_year(self,date_year):
        self.date_year = date_year