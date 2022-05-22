import email
from unicodedata import name
import functions_students
import functions_admins
from obCareers import careers
from obclass_time import hours_class
from obCourses import course
from datetime import datetime
from tkinter import messagebox
from obActivities import activities
from obStudents import students
#-----------Escritura/lectura cursos-----------#

def create_file_courses():
    
    try:
        filecourses = open("courses.txt","w")
        for i in functions_admins.courses:
            name = i.getName()
            credits= i.getCredits()
            
            start_date= i.getStart_date()
            start_date = datetime.strftime(start_date,'%Y/%m/%d')
            end_date= i.getEnd_date()
            end_date = datetime.strftime(end_date,'%Y/%m/%d')
            class_time = list_days(i)
            list_careers= genlist_careers(i)
            status = i.getStatus()
            filecourses.write(str(name)+"-"+str(credits)+"-"+str(start_date)+"-"+str(end_date)+"-"+str(class_time)+"-"+str(list_careers)+"-"+str(status)+"\n")
        filecourses.close()
    except:
        messagebox.showerror("Archivos","Hay un problema con la escritura del archivo")
def load_courses():
    lista = []
    try:
        filecourses = open("courses.txt","r")
        flag = True
        while flag == True:
            line = filecourses.readline()
            if line != '':
                line = line.split("-")
                name = line[0]
                credits = int(line[1])
                start_date = datetime.strptime(line[2], '%Y/%m/%d')
                end_date = datetime.strptime(line[3], '%Y/%m/%d')
                class_time = load_list_classtime(eval(line[4]))
                list_career = load_list_career(eval(line[5]))
                status = line[6].replace("\n",'')
                ob = course(name,credits,start_date,end_date,status)
                ob.careers_belong = list_career
                ob.class_time = class_time
                lista.append(ob)
            else:
                functions_admins.courses = lista
                flag = False
        
                
                
                    
                
    except:
        messagebox.showerror("Archivos","Hay un problema con la lectura del archivo")
def load_list_career(list_career):
    aux = []
    for i in list_career:
        ob = careers(i)
        aux.append(ob)
    return aux
def load_list_classtime(list_classtime):
    aux = []
    for i in list_classtime:
        day = i[0]
        starttime = datetime.strptime(i[1], '%H:%M')
        endtime =datetime.strptime(i[2], '%H:%M')
        ob = hours_class(day,starttime,endtime)
        aux.append(ob)
    return aux
            
def genlist_careers(i):
    aux = []
    for a in i.careers_belong:
        aux.append(a.name)
    return aux
def list_days(i):
    auxlist = []
    for o in i.class_time:
        starttime = datetime.strftime(o.getStart_time(),'%H:%M')
        endtime =datetime.strftime(o.getEnd_time(),'%H:%M')
        auxlist2 = []
        auxlist2.append(o.getDay())
        auxlist2.append(starttime)
        auxlist2.append(endtime)
        auxlist.append(auxlist2)
    return auxlist


#-----------Escritura/lectura carreras-----------#

def create_file_career():
    try:
        filecareers = open("careers.txt","w")
        for i in functions_admins.list_careers:
            name = i.getName()
            filecareers.write(name+"\n")
    except:
        messagebox.showerror("Escritura de archivos","Error en la escritura del archivo externo")
def load_file_career():
    try:
        filecareers = open("careers.txt","r")
        lista = list(functions_admins.list_careers)
        Flag = True
        while Flag == True:
            career = filecareers.readline().replace("\n","")
            if career != '':
                new = careers(career)
                lista.append(new)
            else:
            
                Flag = False
        functions_admins.list_careers = lista
        print(functions_admins.list_careers)
    except:
        messagebox.showerror("Lectura de archivos","Error en la lectura del archivo externo")
#-----------Escritura/lectura admins-----------#
def create_file_admins():
    pass


#-----------Escritura/lectura estudiantes-----------#
def create_file_students():
    try:
        filecourses = open("students.txt","w")
        for i in functions_students.list_students:
            name = i.getName()
            email = i.getEmail()
            career = i.career.name
            password = i.password
            name_courses = create_namecourses(i)
            shedule = create_activities(i)
            filecourses.write(str(name)+"-"+str(email)+"-"+str(career)+"-"+str(password)+"-"+str(name_courses)+"-"+str(shedule)+"\n")
            
    except:
        messagebox.showerror("Escritura de archivos","Error en la escritura del archivo externo")

def create_namecourses(i):
    auxlist = []
    for a in i.courses:
        auxlist.append(a.name)
    return auxlist
def create_activities(i):
    auxlist = []
    for a in i.activities:
        description = a.getDescripcion()
        course = a.getCourse()
        date = datetime.strftime(a.getDate(),'%Y/%m/%d')
        start_time = datetime.strftime(a.getStart_time(),'%H:%M')
        end_time = datetime.strftime(a.getEnd_time(),'%H:%M')
        status = a.getStatus()
        auxlist2 = []
        auxlist2.append(description)
        auxlist2.append(course)
        auxlist2.append(date)
        auxlist2.append(start_time)
        auxlist2.append(end_time)
        auxlist2.append(status)
        auxlist.append(auxlist2)
    return auxlist
        
def load_file_students():
    try:
        filecourse = open("students.txt","r")
        flag = True
        while flag == True:
            line = filecourse.readline()
            if line != '':
                line = line.split("-")
                name = line[0]
                email = line[1]
                career = line[2]
                password = line[3]
                name_courses = eval(line[4])
                shedule = eval(line[5])
                
    except:
        messagebox.showerror("Lectura de archivos","Error en la lectura del archivo")
#----------------------# 
start_date2 = datetime.strptime("2022/11/01", '%Y/%m/%d')
end_date2 = datetime.strptime("2023/02/01", '%Y/%m/%d')
start_time2 = datetime.strptime("9:00", '%H:%M')
end_time2 = datetime.strptime("11:00", '%H:%M')

carrera = careers("computacion")
horario = hours_class(2,start_time2,end_time2)
horario2 = hours_class(3,start_time2,end_time2)
auxlist = []
auxlist.append(horario2)
auxlist.append(horario)
curso1 = course("comu",4,start_date2,end_date2,"En curso")
curso1.careers_belong.append(carrera)
curso1.class_time.append(horario)
curso1.class_time.append(horario2)
functions_admins.courses.append(curso1)

estudiante = students("leiner","gergr",carrera,"rgrg")


description = "estudiar"
name_course = "Recreacion"
date1 = datetime.strptime("2022/11/23", '%Y/%m/%d')
status = "En curso"
start_time2 = datetime.strptime("10:00", '%H:%M')
end_time2 = datetime.strptime("20:00", '%H:%M')
new_activities = activities(description,name_course,date1,start_time2,end_time2,status)
estudiante = students("leiner","gergr",carrera,"rgrg")
estudiante.activities.append(new_activities)
estudiante.courses.append(curso1)
functions_students.list_students.append(estudiante)
create_file_students()