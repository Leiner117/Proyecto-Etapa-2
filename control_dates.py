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
        
        year = years(start_date.year)
        gen_months(year)
        shedule.append(year)
        
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
                            add_hours_weeks(obweek)
                            
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
                            add_hours_weeks(obweek)
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
                        add_hours_weeks(obweek)
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
def returnweek(shedule,year,day):
    for i in shedule:
        if i.date_year == year:
            for a in i.list_months:
                for b in a.list_weeks:
                    for c in b.list_days:
                        if c.date == day:
                            return b
def add_activities(shedule,activies):
    date = activies.date
    if search_year(date.year,shedule) == True:
        
        if search_month(shedule,date.month,date.year) == True:
            
            if search_day(shedule,date) == True:
                day = returndays(shedule,date)
                add_hours_weeks(returnweek(shedule,date.year,date))
                day.list_activities.append(activies)
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
                            position_day = i.index(a)
                            break
                for b in month.list_weeks:
                    if month.list_weeks.index(b) == position_week:
                        add_hours_weeks(b)
                        b.list_days.insert(position_day,obday)
                        break
    else:
        year = years(date.year)
        gen_months(year)
        shedule.append(year)
        h = 0
        nummes = 1
        while h < 12:
            month1 = returnmonth(shedule,year.date_year,nummes)
            list_weeks = calendar.monthcalendar(date.year,nummes)
            for i in list_weeks:
                ob_week = weeks(date.month)
                for a in i:

                    if date.day == a:
                        position_day = i.index(a)
                        obday = days(datetime.weekday(date),date)
                        obday.list_activities.append(activies)
                        for e in obday.list_activities:
                            totaltime = (e.getEnd_time()-e.getStart_time())
                            totaltime = totaltime.seconds//60
                            obday.hours = obday.hours+totaltime
                        ob_week.list_days.insert(position_day,obday)
                        add_hours_weeks(ob_week)
                        month1.list_weeks.append(ob_week)  
                
                month1.list_weeks.append(ob_week)  
            year.list_months.append(month1)
            h = h+1
            nummes = nummes+1
            
def add_hours_weeks(week):
    totalhours = 0
    for i in week.list_days:
        totalhours = totalhours+i.hours 
    week.hours_week = totalhours

