import functions_admins
#from control_dates import shedule
import os
from datetime import datetime,time
from obStudents import students
from obActivities import activities
import control_dates
from obCourses import course
from obclass_time import hours_class
from obCareers import careers
from tkinter import messagebox
import files
list_students = []#Almacena todos los estudiantes
def register (name,email,career,password): 
    '''
    Registra estudiantes en un objeto y los almacena en una lista
    '''
    flag = False
    if len(list_students) != 0:
        for i in list_students:
            if i.getName() == name:
                flag = True
                break
    if flag == False:
        
        student = students(name,email,career,password)
        list_students.append(student)
    return flag 
            
    
def mod_careers(student):
    '''
    Recibe como parametro el objeto del estudiante que quiere cambiar la carrera
    Se llama a una funcion para elegir la nueva carrera
    Se selecciona la nueva carrrera
    se realiza el cambio en el objeto
    '''
    new_career = functions_admins.select_position_careers()
    new_career = functions_admins.careers[new_career]
    student.setCareer(new_career)
def assign_course(student,course,check):
    
    '''
    recorre la lista de estudiantes para verificar que no este el curso matriculado
    si no esta matriculado lo agrega al estudiante, carga las fechas de las clases en el calendario del estudiante
    '''
    if len(functions_admins.courses)>0:
        course = course.get()
        course = returncourse(course)
        flag = False
        for i in student.getCourses():
            if i.getName() == course.getName():
                messagebox.showerror("Matricula de curso","El curso ya se encuentra matriculado por el estudiante")
                flag = True
                break
        if flag == False:
            student.courses.append(course)
            control_dates.create_dates(course,student)
            messagebox.showinfo("Matricula de curso","El curso se matriculo con exito!.")
            if check == 1:
                files.create_file_students()

def add_activities(student,description,course,start_date,start_time,end_time,check):
    '''
    Se solicita la informacion de la actividad
    se compara las fechas y horas para evitar choques con otras actividades
    '''

    if course == '':
        course = "Recreacion"
   
    try:
        start_date = datetime.strptime(start_date, '%Y/%m/%d')
    except ValueError:
        messagebox.showerror("Agregar actividad","El formato de la fecha no es correcto")
        return
        
    try:
        start_time = datetime.strptime(start_time, '%H:%M')
        end_time = datetime.strptime(end_time, '%H:%M')
    except:
        messagebox.showerror("Agregar actividad","El formato de hora no es correcto")
        return
    result = compare_date(student,start_date,start_time,end_time)
    if result == 0:
        status = "En curso"
        new_activities = activities(description,course,start_date,start_time,end_time,status)
        student.activities.append(new_activities)
        control_dates.add_activities(student.shedule,new_activities)
        messagebox.showinfo("Agregar actividad","La actividad se agrego con exito!.")
        if check == 1:
            files.create_file_students()
    elif result == 1:
        messagebox.showerror("Agregar actividad","La actividad tiene un choque de horario.")
    elif result == 2:
         messagebox.showerror("Agregar actividad","La actividad supera las horas semanales.")
    elif result == 3:
        messagebox.showerror("Agregar actividad","La actividad supera las horas diarias.")

def compare_date(student,date,start_time,end_time):
    
    '''
    compara las fechas para averiguar si tiene choque, si tiene horas disponibles 
    '''
    result = 0
    shedule = student.shedule
    totaltime = (end_time.hour*60)-(start_time.hour*60)
    if totaltime <= 720:
        if control_dates.search_day(shedule,date) == True:
            day = control_dates.returndays(shedule,date)
            week = control_dates.returnweek(shedule,date.year,date)
            if week.hours_week <= 4320:
                if day.hours <= 720:
                    for i in day.list_activities:
                        if i.getStatus() == "En curso":
                            if ((i.getStart_time() > end_time or start_time > i.getEnd_time())):
                                result = 0# ya existe la fecha y no tiene problemas con los demas horarios
                            else:
                                result = 1# tiene choque de horario
                                break
                        else:
                            result = 0 #la fecha esta registrada pero los actividades ya se ejecutaron
                else:
                    result = 3#el dia no tiene horas disponibles 
            else:
                result = 2 #la semana no tiene horas disponibles
        else:
            result = 0 # La fecha no esta registrada
    else:
        result = 3
                    
    return result 
def returncourse(course):
    for i in functions_admins.courses:
        if course == i.getName():
            return i
    
def gen_reports(student,date,filter):
    date = date.get()
    filter = filter.get()
    try:
        date = datetime.strptime(date, '%Y/%m/%d')
        
    except:
        messagebox.showerror("Agregar actividad","El formato de fecha no es correcto")
        exit()
    if filter == "Semana":
        week= control_dates.returnweek(student.shedule,date.year,date)
        auxlist = []
        
        totalactivities = len(week.list_days)
        totalhours = week.hours_week
        totalhoursav = 4320-totalhours
        auxlist.append(totalactivities)
        auxlist.append(totalhours)
        auxlist.append(totalhoursav)
        return auxlist
            
    else: 
        day = control_dates.returndays(student.shedule,date)
        report = gen_reports_days(day)
        return report
def gen_reports_days(day):
    auxlist = []
    for i in day.list_activities:
        description = i.getDescripcion()
        course = i.getCourse()
        date = i.getDate()
        hours = i.end_time-i.start_time
        hoursav = (720 - ((i.end_time.second-i.start_time.second)//60))//60
        status = i.status
        auxlist2 = []
        auxlist2.append(description)
        auxlist2.append(course)
        auxlist2.append(date)
        auxlist2.append(hours)
        auxlist2.append(hoursav)
        auxlist2.append(status)
        auxlist.append(auxlist2)
        
    
