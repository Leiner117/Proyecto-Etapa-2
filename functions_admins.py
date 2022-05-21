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
#week = ["LUNES","MARTES","MIERCOLES","JUEVES","VIERNES","SABADO","DOMINGO"]

def add_admins():
    ''' Agrega administradoreas a la lista, guardando los datos solicitados en una lista anidada'''
    name = input("Ingrese su nombre completo: ")
    password = input("Ingrese una contraseña: ")
    phone_number = int(input("Ingrese su numero de telefono: "))
    admin1 = admins(name,password,phone_number)
    list_admins.append(admin1)


def add_courses(name_course,credit,start_date,end_date,days,careers):
    '''
    convierte la tupla de cursos en lista
    solicita los datos necesarios para crear un curso 
    se almacenan en una lista indexada
    se cargan todos los dias correspondientes a la actividades de clases al estudiante
    
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
    los almacenan en una lista y despues se convierte denuevo en tupla
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
        print("La carrera se agrego con exito!.")
        messagebox.showinfo("Agregar carrera","La carrera se agrego con exito!.",parent =win)
    else:
        messagebox.showerror("Agregar carrera","La carrera ya existe")
        
        
        
def select_career():
    '''
    Recorre la lista de carreras
    crea una lista para las carreras asociadas al curso correspondiente
    retorna la lista con el nombre de las carreras
    
    '''
    global list_careers
    careers_list = []
    b = 0
    while b == 0:
        print("Seleccione las carrera que desea:")
        a = 1
        for i in list_careers:
            
            print(str(a)+"-"+i.getName())
            a = a+1
        select = int(input("---->"))
        if select > len(list_careers):
            print("La carrera seleccionada no existe")
            select_career()
        else:
            careers_list.append(list_careers[select-1])
            print("Desea asociar mas carreras a este curso?:")
            print("1. Si\n2. No")
            opselect = int(input("---> "))
            if opselect == 2:
                b = 1
                return careers_list
def select_course():
    '''
    Imprime la lista de cursos
    retorna el indice del curso seleccionado
    '''
    global courses
    
    print("Seleccione el curso que desea:")
    a = 1
    for i in courses:
        print(str(a)+"-"+i.getName())
        a = a+1
    select = int(input("---->"))
    if select > len(courses):
        print("El curso seleccionado no existe.")
        select_course()
    else:
        return (select-1)
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

    

def mod_courses():
    '''
    Imprime el menu para la modificacion de datos de los cursos
    '''
    course = select_course()
    while True:
        print("1. Nombre de curso\n2. creditos\n3. fecha de inicio\n4. fecha de finalizacion\n5. Horario\n6.carreras asociadas\n7.Salir")
        opselect = int(input("Ingrese la opcion que desea: "))
        if opselect == 1:
            mod_nameCourse(course)
                
        elif opselect == 2:
            mod_credits(course)
        elif opselect == 3:
            mod_start_date(course)
        elif opselect == 4:
            mod_end_date(course)
        elif opselect == 5:
            mod_class_times(course)
        elif opselect == 6:
            mod_careers(course)
        elif opselect == 7:
            break
def mod_nameCourse(course):
    '''
    Modifica el nombre del curso
    '''
    check = False
    new_name = input("Ingrese el nuevo nombre del curso: ")
    global courses
    for c in courses:
        if new_name == c.name:
            check = True
            break
    if check == False:
        courses = list(courses)
        courses[course].setName(new_name)
        courses = tuple(courses)
def mod_credits(course):
    '''
    modifica el numero de creditos del curso
    '''
    global courses
    courses = list(courses)
    new_credits = int(input("Ingrese la nueva cantidad de creditos: "))
    new_school_hours = new_credits*3
    courses[course].setCredits(new_credits)
    courses[course].setCredits(new_school_hours)
    courses = tuple(courses)
def mod_start_date(course):
    '''
    modifica la fecha de inicio del curso
    '''
    global courses
    courses = list(courses)
    start_date = input("fecha de inicio del curso'aaaa/mm/dd': ")
    try:
        start_date = datetime.strptime(start_date, '%Y/%m/%d').strftime('%Y/%m/%d')
        courses[course].Start_date(start_date)
        courses = tuple(courses)
    except ValueError:
        print("\n No ha ingresado una fecha correcta...")
        mod_courses()
    
def mod_end_date(course):
    '''
    modifica la fecha de conclusion del curso
    '''
    global courses
    courses = list(courses)
    end_date = input("fecha de finalización del curso'aaaa/mm/dd': ") 
    try:
        end_date = datetime.strptime(end_date, '%Y/%m/%d').strftime('%Y/%m/%d')
    except ValueError:
        print("\n No ha ingresado una fecha correcta...")
        mod_courses()
    courses[course].setEnd_date(end_date)
    courses = tuple(courses)
def mod_class_times(course):
    '''
    modifica las horas de clase del curso
    '''
    global courses
    courses = list(courses)

    courses = tuple(courses)
def mod_careers(course):
    '''
    modifica las carreras asociadas al curso
    '''
    global courses
    courses = list(courses)
    new_careers = select_career()
    courses[course].setCareers_belong(new_careers)
    courses = tuple(courses)
def mod_careers_general():
    '''
    modifica el nombre de la carrera seleccionada
    '''
    career = select_position_careers()
    new_careers = input("Ingrese el nuevo nombre de la carrera: ")
    list_careers[career].setName(new_careers)

    
    
