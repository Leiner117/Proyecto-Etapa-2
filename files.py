
import functions_students
import functions_admins
from obCareers import careers
from obclass_time import hours_class
from obCourses import course
from datetime import date, datetime
from tkinter import messagebox
from obActivities import activities
from obStudents import students
import control_dates
from obAdmins import admins
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
    except FileNotFoundError:
        create_file_courses()
        return
    try:
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
        messagebox.showerror("Lectura de archivo","Error en la lectura de archivo externo")     
    

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
        filecareers.close()
    except:
        messagebox.showerror("Escritura de archivos","Error en la escritura del archivo externo")
def load_file_career():
    try:
        filecareers = open("careers.txt","r")
    except FileNotFoundError:
        create_file_career()
        return
    try:
        
        lista = list(functions_admins.list_careers)
        Flag = True
        while Flag == True:
            career = filecareers.readline().replace("\n","")
            if career != '':
                new = careers(career)
                lista.append(new)
            else:
            
                Flag = False
        filecareers.close()
        functions_admins.list_careers = lista
    except:
        messagebox.showerror("Lectura de archivos","Error en la lectura del archivo externo")


#-----------Escritura/lectura admins-----------#
def create_file_admins():
    try:
        fileadmins = open("admins.txt","w")
        for i in functions_admins.list_admins:
            name = i.getName()
            password = i.getPassword()
            phone = i.getPhone()
            fileadmins.write(str(name)+"-"+str(password)+"-"+str(phone)+"\n")
            
        fileadmins.close()
            
    except:
        messagebox.showerror("Archivos","Hay un problema con la escritura del archivo")
def load_file_admins():
    try:
        fileadmins = open("admins.txt","r")
    except FileNotFoundError:
        create_file_admins()
        return
    try:
        flag = True
        while flag == True:
            line = fileadmins.readline()
            if line != '':
                line = line.split("-")
                name= line[0]
                password = line[1]
                phone = line[2]
                phone = phone.replace("\n",'')
                new_admin = admins(name,password,phone)
            else:
                flag = False
            
    except:
        messagebox.showerror("Lectura de archivos","Error en la lectura del archivo externo")

        
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
        filecourses.close()
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
    except FileNotFoundError:
        create_file_students()
        return
    try:
        
        flag = True
        while flag == True:
            line = filecourse.readline()
            if line != '':
                line = line.split("-")
                name = line[0]
                email = line[1]
                career = functions_admins.select_position_careers(line[2])
                password = line[3]
                
                ob = students(name,email,career,password)
                name_courses = load_listcourses(eval(line[4]),ob)
                shedule = load_activities(eval(line[5]),ob)
                ob.courses = name_courses
                ob.activities = shedule
                functions_students.list_students.append(ob)
            else:
                flag = False
        filecourse.close()
    except:
        messagebox.showerror("Lectura de archivos","Error en la lectura del archivo")
def load_listcourses(list_courses,ob):
    auxlist = []
    for a in functions_admins.courses:
        for i in list_courses:
            if i == a.getName():
                auxlist.append(a)
    for b in auxlist:
        control_dates.create_dates(b,ob)
    return auxlist
def load_activities(list_shedule,ob):
    aux = []
    for i in list_shedule:
        description = i[0]
        course = i[1]
        date = datetime.strptime(i[2], '%Y/%m/%d')
        start_time = datetime.strptime(i[3], '%H:%M')
        end_time = datetime.strptime(i[4], '%H:%M')
        status = i[5]
        new_acti = activities(description,course,date,start_time,end_time,status)
        aux.append(new_acti)
    for b in aux:
        control_dates.add_activities(ob.shedule,b)
    return aux
        
        
#----------------------# 