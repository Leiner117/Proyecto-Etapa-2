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
list_students = []#Almacena todos los estudiantes
def register (): 
    '''
    Registra estudiantes en una lista, ingresando los datos solicitados 
    Se utiliza una lista indexadas para almacenar los estudiantes 
    '''
    courses = []
    name = input("Ingrese su nombre: ")
    email =  input("porfavor introduce tu gmail: ")   
    career = functions_admins.select_position_careers()
    career = functions_admins.list_careers[career]
    password = input("porfavor introduce una contraseña: ")
    student = students(name,email,career,password,courses)
    list_students.append(student)
    print("Te has registrado con exito!!! ")
def mod_careers(student):
    '''
    Recibe como parametro el nombre del estudiante que quiere cambiar la carrera
    Se llama a una funcion para elegir la nueva carrera
    Se selecciona la nueva carrrera
    se realiza el cambio en la lista indexada
    '''
    new_career = functions_admins.select_position_careers()
    new_career = functions_admins.careers[new_career]
    student.setCareer(new_career)
def assign_course(student):
    '''
    Se recorre la lista de estudiantes para obtener el indice del estudiante que desea realizar la matricula
    se imprime la lista de cursos que estan disponibles en la carrera del estudiante
    se utiliza un diccionario para almacenar los datos 
    se llama una funcion para asignar los dias de clases del curso matriculado
    '''
    if len(functions_admins.courses)>0:
        career = ""
        aux_dic = {}
        b = 0
        course = functions_admins.select_course()
        course = functions_admins.courses[course]
        flag = False
        for i in student.getCourses():
            if i.getName() == course.getName():
                print("El curso ya esta matriculado")
                flag = True
                break
        if flag == False:
            student.courses.append(course)
            print("El curso se matriculo con exito!.")
            control_dates.create_dates(course,student)
    else:
        #mensaje de error
        print("No hay cursos creados")

def add_activities(student):
    '''
    Se genera el indice del estudiante 
    Se solicita la informacion de la actividad
    se compara las fechas y horas para evitar choques con otras actividades
    se utiliza un diccionario indexado para almacenar las actividades
    '''

    description = str(input("Ingrese la descripcion de la actividad: "))
    print("La actividad esta asociada a un curso?\n1.Si\n2.No")
    opselect = int(input("-->"))
    if opselect == 1:
        course = course_activities(student)
    elif opselect == 2:
        course = "Recreacion"
    start_date = input("fecha de la actividad'aaaa/mm/dd': ")
   
    try:
        start_date = datetime.strptime(start_date, '%Y/%m/%d')
    except ValueError:
        print("\n No ha ingresado una fecha correcta...")
        add_activities()
    start_time = input("Ingrese la hora de inicio de la actividad: ")
    start_time = datetime.strptime(start_time, '%H:%M')
    end_time = input("Ingrese la hora de conclusion de la actividad: ")
    end_time = datetime.strptime(end_time, '%H:%M')
    result = compare_date(student,start_date,start_time,end_time)
    if result == True:
        status = "En curso"
        new_activities = activities(description,course,start_date,start_time,end_time,status)
        control_dates.add_activities(student.shedule,new_activities)
        print("La actividad se agrego con exito")
    else:
        print("Tienes un choque en tu horario, no puedes agregar esta actividad.")
def course_activities(student):
    '''
    Imprime la lista de cursos matriculados y en curso para asociar alguna actividad
    '''
    e = 0
    
    for i in student.courses:
        e = e+1
        if i.status == "En curso":
            print("-"+i.getName())
    course = (input("Ingrese el curso que desea: "))
    for a in student.courses:
        if course == a.getName():
            return a
    else:
        print("El curso ingresado no esta matriculado por el estudiante")
def compare_date(student,date,start_time,end_time):
    '''
    recorre el diccionario indexado de actividades
    compara las fechas con la fecha que se quiere agregar
    compara el estado la actividad almacenada para averiguar si tiene algun choque
    se comparan las horas de la actividad para evitar choques de horarios
    se retorna un True o False dependiendo de si hay o no choque
    '''
    result = True
    shedule = student.shedule
    if control_dates.search_day(shedule,date) == True:
        day = control_dates.returndays(shedule,date)
        for i in day.list_activities:
            if i.getStatus() == "En curso":
                if ((i.getStart_time() > end_time or start_time > i.getEnd_time())):
                    result = True# ya existe la fecha y no tiene problemas con los demas horarios
                else:
                    result = False# tiene choque de horario
                    break
            else:
                result = True #la fecha esta registrada pero los actividades ya se ejecutaron
    else:
        result = True # La fecha no esta registrada
                
    result = True
    for i in student.getActivities():
        if i.date == date:
            
            if i.getStatus() == "En curso":
               if ((i.getStart_time() > end_time or start_time > i.getEnd_time())):
                   result = True# ya existe la fecha y no tiene problemas con los demas horarios
               else:
                   result = False# tiene choque de horario
                   break
            else:
               result = True #la fecha esta registrada pero los actividades ya se ejecutaron
        else:
            result = True # La fecha no esta registrada
    return result


start_date = datetime.strptime("2022/01/01", '%Y/%m/%d')
end_date = datetime.strptime("2022/04/01", '%Y/%m/%d')
start_time = datetime.strptime("9:00", '%H:%M')
end_time = datetime.strptime("11:00", '%H:%M')

start_date2 = datetime.strptime("2022/11/01", '%Y/%m/%d')
end_date2 = datetime.strptime("2023/02/01", '%Y/%m/%d')
start_time2 = datetime.strptime("9:00", '%H:%M')
end_time2 = datetime.strptime("11:00", '%H:%M')

carrera = careers("computacion")
horario = hours_class(2,start_time,end_time)
horario2 = hours_class(3,start_time,end_time)
auxlist = []
auxlist.append(horario2)
auxlist.append(horario)
curso1 = course("Progra",4,12,start_date,end_date,auxlist,carrera,"En curso")
curso2 = course("mate",4,12,start_date2,end_date2,auxlist,carrera,"En curso")
functions_admins.list_careers.append(carrera)
functions_admins.courses.append(curso1)
functions_admins.courses.append(curso2)
estudiante = students("leiner","gergr",carrera,"rgrg",[])
list_students.append(estudiante)
assign_course(list_students[0])
assign_course(list_students[0])

description = "estudiar"
name_course = "Recreacion"
date1 = datetime.strptime("2022/11/05", '%Y/%m/%d')
status = "En curso"
new_activities = activities(description,name_course,date1,start_time,end_time,status)
control_dates.add_activities(list_students[0].shedule,new_activities)
for i in list_students[0].shedule:
    print("ano "+str(i.date_year))
    for a in i.list_months:
        print("mes "+str(a.num_months))
        for b in a.list_weeks:
            for c in b.list_days:
                print("dia "+str(c.date))
                print("tiempo consumido"+str(c.hours))
                for j in c.list_activities:
                    print("curso "+str(j.course))
                    
            
        
