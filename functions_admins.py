from datetime import datetime,time
from obAdmins import admins
from obCourses import course
from obCareers import careers
from obclass_time import hours_class
from tkinter import messagebox
import control_dates
admin = admins("admin","12345",10101)
list_admins = [admin]
courses = []
list_careers = []

'''
Crea el objeto admins con sus respectivos datos
'''
def add_admins():
    
    name = input("Ingrese su nombre completo: ")
    password = input("Ingrese una contraseña: ")
    phone_number = int(input("Ingrese su numero de telefono: "))
    admin1 = admins(name,password,phone_number)
    list_admins.append(admin1)


def add_courses(name_course,credit,start_date,end_date,days,careers):
    '''
    convierte la tupla de cursos en lista
    solicita los datos necesarios para crear un curso 
    se almacenan en un objeto
    se almacenan en una lista
    '''
    try:
        credit = int(credit)
    except:
        messagebox.showerror("Agregar curso","Tiene que ingresar los creditos en formato numero")
        exit()
    check = False  
    global courses
    courses = list(courses)
    for c in courses:
        if name_course == c.name:
            check = True
            break
    if check == False:
        
        status = "En curso"
        new_course = course(name_course,credit,start_date,end_date,status)
        for a in days:
            new_course.class_time.append(a)
        for b in careers:
            new_course.careers_belong.append(b)
        courses.append(new_course)
        messagebox.showinfo("Agregar curso","El curso se agrego con exito")
    else:
            #poner mensaje de error
        messagebox.showerror("Agregar curso","El curso ya existe")
        
        #control_dates.load_dates(courses)
        courses = tuple(courses)
def selectday(day,week):
    for i in week:
        if i == day:
            return week.index(i)
def add_careers(career,win):
    '''
    convierte la tupla de carreras en lista
    ingresa los datos necesarios 
    los almacenan en un objeto y despues lo agrega a la lista
    '''
    global list_careers
    check = False
    list_careers = list(list_careers)
    
    for i in list_careers:
        if career == i.name:
            check = True
            break
    if check == False:
        
        new_career = careers(career)
        list_careers.append(new_career)
        list_careers = tuple(list_careers)
        messagebox.showinfo("Agregar carrera","La carrera se agrego con exito!.",parent =win)
    else:
        messagebox.showerror("Agregar carrera","La carrera ya existe")
        

def select_position_careers(name):
    
    
    '''
    imprime la lista de carreras
    retorna el indice de la carreras seleccionada
    '''
    global careers
    for i in list_careers:
        if i.getName() == name:
            select = i
            return select

    
    
