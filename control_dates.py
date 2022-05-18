from datetime import date, datetime
import calendar
from obActivities import activities
from obyear import years
from obMonth import months
from obWeek import weeks
from obDay import days

def create_dates(course,student):
    shedule = student.getShedule()#calendario de estudiante
    start_date = course.getStart_date()#fecha de inicio del curso
    end_date = course.getEnd_date()#fecha de finalizacion 
    create_years(start_date,end_date,shedule)#agrega el objeto year al calendario del estudiante
    dif_months = difference_months(start_date,end_date)#diferencia de meses entre las dos fechas 
    dayclass = day_class(course)#lista de los dias de clases 
    gen_weeks(start_date,dif_months,end_date,dayclass,course,shedule)
def create_years(start_date,end_date,shedule):
    if len(shedule) == 0:
        if start_date.year == end_date.year:
            year = years(start_date.year)
            gen_months(year)
            shedule.append(year)
        else:
            year = years(start_date.year)
            year2 = years(end_date.year)
            gen_months(year)
            gen_months(year2)
            shedule.append(year)
            shedule.append(year2)
    else:
        for i in shedule:
            
            if start_date.year == i.getDate_year() or end_date.year == i.getDate_year():
                pass
            elif start_date.year != i.getDate_year():
                year = years(start_date.year)
                gen_months(year)
                shedule.append(year)
            elif end_date.year != i.getDate_year():
                year = years(end_date.year)
                gen_months(year)
                shedule.append(year)
                
def difference_months(start_date,end_date):
    result = (end_date.year-start_date.year) * 12 + (end_date.month-start_date.month)
    return result
def gen_weeks(start_date,difference,end_date,dayclass,course,shedule):
    '''
    Se crea un ciclo donde compara un contador con la diferencia de meses entre las fechas
    se almacenan todos los meses en una lista
    se generan todas las semanas de un mes indicado utilizando una libreria
    las semanas se almacenan en un diccionario asignando de clave el mes que pertenecen las semanas
    este diccionario se almacena en una lista
    retorna la lista con todas las semanas y la lista con todos los meses
    '''
    total_weeks = []
    start_month = start_date.month
    start_year = start_date.year
    i = 0
    
    while difference >= i:
        
        
        obmonth = returnmonth(shedule,start_year,start_month)
        weeks = calendar.monthcalendar(start_year,start_month)
        create_weeks(weeks,start_month,start_year,obmonth,start_date,end_date,dayclass,course)
        start_month = start_month+1
        if start_month > 12:
            start_year = start_year+1
            year = years(start_year)
            gen_months(year)
            shedule.append(year)
            start_month = 1
        i = i+1
        '''else:
            add_daysforweeks(start_month,start_year,dayclass,course,shedule)
            if start_month > 12:
                start_year = start_year+1
                
                start_month = 1
            i = i+1
            start_month = start_month+1'''
            
def add_daysforweeks(start_month,start_year,dayclass,course,shedule):
    weeks = filter_days(start_year,start_month,dayclass,shedule)
    flag = False
    
    for i in shedule:
        if i.getDate_year() == start_year:
            for a in i.getList_months():
                if a.getNum_months() == start_month:
                    for b in a.getList_weeks():
                        for x in b.getList_days():
                            for z in weeks:
                                for m in z:
                                    if m == x.getDate():

                                        x.list_activities.append(create_activities(course,x.getDate()))
                                        for a in x.list_activities:
                                            totaltime = (a.getEnd_time()-a.getStart_time())
                                            totaltime = totaltime.seconds//60
                                            x.hours = x.hours+totaltime
                    
def filter_days(start_year,start_month,dayclass,shedule):
    weeks = calendar.monthcalendar(start_year,start_month)
    flag = False
    auxlist2 = []
    for i in weeks:
        auxlist = []
        for a in i:
            if a != 0:
                if i.index(a) in dayclass:
                    date = str(start_year)+"/"+str(start_month)+"/"+str(a)
                    date = datetime.strptime(date, '%Y/%m/%d')
                    if search_day(shedule,date) == False:
                        for b in shedule:
                            for k in b.getList_months():
                                if k.num_months == date.month:
                                    for n in k.getList_weeks():
                                        if k.list_weeks.index(n) == weeks.index(i):
                                            obday = days(datetime.weekday(date),date)
                                            n.list_days.append(obday)
                                            
                    auxlist.append(date) 
        auxlist2.append(auxlist)                    
        
    return auxlist2
        
            

def add_month(year,month,shedule):
    for i in shedule:
        if year == i.getDate_year():
            i.list_months.append(month)
def create_months(month,year):
    
    name = calendar.month_name[month]
    month1 = months(name,month)
    return month1
def gen_months(year):
    i = 0
    nummonths = 1
    while nummonths <= 12:
        obmonth = months(calendar.month_name[nummonths],nummonths)
        year.list_months.append(obmonth)
        i = i+1
        nummonths = nummonths+1
def create_weeks(list_weeks,month,year,obmonth,start_date,end_date,dayclass,course):
    
    for i in list_weeks:
        obweek = weeks(month)
        for a in i:
            if a != 0:
                numday = i.index(a)
                if verifydays(dayclass,numday) == True:
                    if start_date.month == month:
                        if a >= start_date.day:
                            date = str(year)+"/"+str(month)+"/"+str(a)
                            date = datetime.strptime(date, '%Y/%m/%d')
                            obday = days(numday,date)
                            obday.list_activities.append(create_activities(course,date))
                            for a in obday.list_activities:
                                totaltime = (a.getEnd_time()-a.getStart_time())
                                totaltime = totaltime.seconds//60
                                obday.hours = obday.hours+totaltime
                            obweek.list_days.append(obday)
                            
                        else:
                            pass
                            
                    if month == end_date.month:
                        if a <= end_date.day:
                            
                            date = str(year)+"/"+str(month)+"/"+str(a)
                            date = datetime.strptime(date, '%Y/%m/%d')
                            obday = days(numday,date)
                            obday.list_activities.append(create_activities(course,date))
                            for a in obday.list_activities:
                                totaltime = (a.getEnd_time()-a.getStart_time())
                                totaltime = totaltime.seconds//60
                                obday.hours = obday.hours+totaltime
                            obweek.list_days.append(obday)
                        else:
                            pass
                    if month != start_date.month and end_date.month != month:
                        date = str(year)+"/"+str(month)+"/"+str(a)
                        date = datetime.strptime(date, '%Y/%m/%d')
                        obday = days(numday,date)
                        obday.list_activities.append(create_activities(course,date))
                        for a in obday.list_activities:
                            totaltime = (a.getEnd_time()-a.getStart_time())
                            totaltime = totaltime.seconds//60
                            obday.hours = obday.hours+totaltime
                        obweek.list_days.append(obday)
        obmonth.list_weeks.append(obweek)
        
def create_activities(course,date):
    
    descripcion = "Clase"
    namecourse = course.getName()
    start_time,end_time = select_hours(course,date)
    status = "En curso"
    new_activities = activities(descripcion,namecourse,date,start_time,end_time,status)
    return new_activities
def select_hours(course,date):
    for i in course.class_time:
        if i.day == datetime.weekday(date):
            return i.getStart_time(),i.getEnd_time()
        
def verifydays(dayclass,day):
    
    if day in dayclass:
        return True
def day_class(course):
    auxlist = []
    for i in course.class_time:
        auxlist.append(i.getDay())
    return auxlist
def search_year(year,shedule):
    for i in shedule:
        if year == i.getDate_year():
            return True
    return False
def search_month(shedule,month,year):
    for i in shedule:
        if i.date_year == year:
            for a in i.list_months:
                
                if month == a.getNum_months():
                    return True
    return False
def search_day(shedule,day):
    for i in shedule:#anos
        for a in i.getList_months():#meses
            for b in a.getList_weeks():#semanas
                for h in b.getList_days():#dias
                    if day == h.getDate():
                        return True
    return False
def returndays(shedule,day):
    for i in shedule:#anos
        for a in i.getList_months():#meses
            for b in a.getList_weeks():#semanas
                for h in b.getList_days():#dias
                    if day == h.getDate():
                        return h
def returnmonth(shedule,year,month):
    for i in shedule:
        if i.date_year == year:
            for a in i.list_months:
                if month == a.getNum_months():
                    return a
    
def add_activities(shedule,activies):
    date = activies.date
    if search_year(date.year,shedule) == True:
        
        if search_month(shedule,date.month,date.year) == True:
            
            if search_day(shedule,date) == True:
                day = returndays(shedule,day)
                day.list_activies.append(activies)
            else:
                obday = days(datetime.weekday(date),date)
                obday.list_activities.append(activies)
                for a in obday.list_activities:
                    totaltime = (a.getEnd_time()-a.getStart_time())
                    totaltime = totaltime.seconds//60
                    obday.hours = obday.hours+totaltime
                
                month = returnmonth(shedule,date.year,date.month)
                list_weeks = calendar.monthcalendar(date.year,date.month)
                for i in list_weeks:
                    for a in i:
                        if date.day == a:
                            position_week = list_weeks.index(i)
                            break
                for b in month.list_weeks:
                    if month.list_weeks.index(b) == position_week:
                        b.list_days.append(obday)
                        break
        else:
            obmonth = create_months(date.month,date.year)
            list_weeks = calendar.monthcalendar(date.year,date.month)
            for i in list_weeks:
                ob_week = weeks(date.month)
                for a in i:
                    if date.day == a:
                        obday = days(datetime.weekday(date),date)
                        obday.list_activies.append(activies)
                        for e in obday.list_activities:
                            totaltime = (e.getEnd_time()-e.getStart_time())
                            totaltime = totaltime.seconds//60
                            obday.hours = obday.hours+totaltime
                        ob_week.list_days.append(obday)
                        obmonth.list_weeks.append(ob_week)  
                
                obmonth.list_weeks.append(ob_week)  
    else:
        year = years(date.year)
        gen_months(year)
        i = 0
        nummes = 1
        while i < 12:
            month1 = returnmonth(shedule,year,nummes)
            list_weeks = calendar.monthcalendar(date.year,nummes)
            for i in list_weeks:
                ob_week = weeks(date.month)
                for a in i:
                    if date.day == a:
                        obday = days(datetime.weekday(date),date)
                        obday.list_activies.append(activies)
                        for e in obday.list_activities:
                            totaltime = (e.getEnd_time()-e.getStart_time())
                            totaltime = totaltime.seconds//60
                            obday.hours = obday.hours+totaltime
                        ob_week.list_days.append(obday)
                        month1.list_weeks.append(ob_week)  
                
                month1.list_weeks.append(ob_week)  
            year.list_months.append(month1)
            i = i+1
            nummes = nummes+1
            
                
                    
