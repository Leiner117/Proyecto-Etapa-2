
from datetime import date, datetime
import tkinter as tk
from tkinter import ttk,messagebox
import tkinter.font as tkFont
import functions_admins
from obStudents import students
from obCareers import careers
from obclass_time import hours_class
from obCourses import course
from datetime import datetime
import functions_students
import files
cont = 0

'''
- Cambiar de carrera
- Matricular cursos
- Agregar actividad
- Modificar cursos
- actvidades
- reportes
- Salir
-

'''

#-----------MENU ESTUDIANTES-----------#
def menu(student,win):
    winmenustudent = tk.Toplevel()
    winmenustudent.title("Menu Estudiantes")
    winmenustudent.minsize(700,400)
    fontStyle = tkFont.Font(family="Lucida Grande", size=12)
    lb_name=tk.Label(winmenustudent,text="Bienvenido: "+student.getName(),font=fontStyle).place(x=10, y=10)
    lb_checksave = tk.Label(winmenustudent,text="Auto guardado",font=fontStyle).place(x= 400,y=10)
    sv_checksave = tk.IntVar()
    btn_checksave = tk.Checkbutton(winmenustudent,variable=sv_checksave).place(x= 530,y =10)
    tk.Button(winmenustudent, text="Cambiar carrera",font=fontStyle, command=None,height=2,width=14).place(x=150, y=70)
    tk.Button(winmenustudent, text="Matricular cursos",font=fontStyle, command=lambda:menuaddcourse(student,sv_checksave.get()),height=2,width=14).place(x=300, y=70)
    tk.Button(winmenustudent, text="Agregar actividad",font=fontStyle, command=lambda:menuaddactivities(student,sv_checksave.get()),height=2,width=14).place(x=450, y=70)
    tk.Button(winmenustudent, text="actividades",font=fontStyle, command=lambda:printactivities(student,sv_checksave.get()),height=2,width=14).place(x=300, y=150)
    tk.Button(winmenustudent, text="Guardar cambios",font=fontStyle, command=save_change,height=2,width=14).place(x=150, y=150)
    tk.Button(winmenustudent, text="Reportes",font=fontStyle, command=lambda:menureports(student),height=2,width=14).place(x=450, y=150)
    tk.Button(winmenustudent, text="Salir",font=fontStyle, command=lambda:[show(win),close(winmenustudent)],height=2,width=14).place(x=300, y=220)
    
    winmenustudent.mainloop()
def save_change():
    files.create_file_students()
#-----------FUNCION MOSTRAR VENTANA-----------#
def show(win):
    win.deiconify()
    
#-----------MENU CAMBIO DE CARRERA-----------#
def menuchangecareer():
    pass

#-----------MENU MATRICULAR CURSOS-----------#
def menuaddcourse(student,check):
    winmenucourse = tk.Toplevel()
    winmenucourse.title("Matricular cursos")
    winmenucourse.minsize(700,400)
    fontStyle = tkFont.Font(family="Lucida Grande", size=12)
    listcourses = gencourses(student)
    
    lb_course= tk.Label(winmenucourse,text="Curso:").place(x=10, y=40)
    sv_course = tk.StringVar()
    combobox_course = ttk.Combobox(winmenucourse,values =listcourses,textvariable=sv_course,state="readonly").place(x=80,y=40)
    tk.Button(winmenucourse, text="Matricular",font=fontStyle, command=lambda:functions_students.assign_course(student,sv_course,check),height=2,width=14).place(x=300, y=220)
    tk.Button(winmenucourse, text="Salir",font=fontStyle, command=lambda:close(winmenucourse),height=2,width=14).place(x=450, y=220)
    
def gencourses(student):
    auxlist = []
    for i in functions_admins.courses:
        for a in i.careers_belong:
            if student.getCareer().getName() == a.getName():
                auxlist.append(i.getName())
    return auxlist
    
    


#-----------MENU AGREGAR ACTIVIDADES-----------#
def menuaddactivities(student,check):
    winmenuactivities = tk.Toplevel()
    winmenuactivities.title("Agregar actividad")
    winmenuactivities.minsize(800,600)
    fontStyle = tkFont.Font(family="Lucida Grande", size=12)
    listcourses = coursestudent(student)
    
    lb_name_acti=tk.Label(winmenuactivities,text="Descripcion de la actividad:").place(x=10, y=40)
    sv_name_acti = tk.StringVar()
    e_name_acti= ttk.Entry(winmenuactivities, textvariable = sv_name_acti, width=30).place(x=165, y=40)
    
    lb_course= tk.Label(winmenuactivities,text="Asociar curso(opcional):").place(x=10, y=70)
    sv_course = tk.StringVar()
    combobox_course = ttk.Combobox(winmenuactivities,values =listcourses,textvariable=sv_course,state="readonly").place(x=150,y=70)
    
    lb_date=tk.Label(winmenuactivities,text="Fecha(aaaa/mm/dd):").place(x=10, y=100)
    sv_date = tk.StringVar()
    e_date= ttk.Entry(winmenuactivities, textvariable = sv_date, width=30).place(x=130, y=100)
    
    lb_startime=tk.Label(winmenuactivities,text="Hora de inicio(HH:MM):").place(x=10, y=130)
    sv_startime = tk.StringVar()
    e_startime= ttk.Entry(winmenuactivities, textvariable = sv_startime, width=30).place(x=150, y=130)
        
    lb_endtime=tk.Label(winmenuactivities,text="Hora de finalización(HH:MM):").place(x=10, y=160)
    sv_endtime = tk.StringVar()
    e_endtime= ttk.Entry(winmenuactivities, textvariable = sv_endtime, width=30).place(x=180, y=160)
    
    tk.Button(winmenuactivities, text="Agregar actividad",font=fontStyle, command=lambda:add_activities(student,sv_name_acti,sv_course,sv_date,sv_startime,sv_endtime,check),height=2,width=14).place(x=300, y=220)
    tk.Button(winmenuactivities, text="Salir",font=fontStyle, command=lambda:winmenuactivities.destroy(),height=2,width=14).place(x=450, y=220)
    
    
    winmenuactivities.mainloop()
def add_activities(student,name,course,date,start_time,end_time,check):
    strname = name.get()
    strcourse = course.get()
    strdate = date.get()
    strstart_time = start_time.get()
    strend_time = end_time.get()
    functions_students.add_activities(student,strname,strcourse,strdate,strstart_time,strend_time,check)
    clearwin(name,course,date,start_time,end_time)
    
    
        
def coursestudent(student):
    auxlist = []
    for i in student.courses:
        if i.status == "En curso":
            auxlist.append(i.getName())
    return auxlist

#-----------FUNCION CAMBIAR ESTADO ACTIVIDADES-----------#
def printactivities(student,check):
    winmenuactivities = tk.Toplevel()
    winmenuactivities.title("Cambiar estado de actividades")
    winmenuactivities.minsize(700,400)
    fontStyle = tkFont.Font(family="Lucida Grande", size=12)
    listac = list_activities(student)
    lb_activities= tk.Label(winmenuactivities,text="Actividad:").place(x=10, y=40)
    sv_activities = tk.StringVar()
    combobox_activities = ttk.Combobox(winmenuactivities,values =listac,textvariable=sv_activities,state="readonly").place(x=80,y=40)
    
    lb_status= tk.Label(winmenuactivities,text="Estado:").place(x=10, y=70)
    sv_status = tk.StringVar()
    combobox_status = ttk.Combobox(winmenuactivities,values =["Realizada"],textvariable=sv_status,state="readonly").place(x=80,y=70)
    
    tk.Button(winmenuactivities, text="Realizar el cambio",font=fontStyle, command=lambda:[mod_activities(sv_status,sv_activities,check,student)],height=2,width=14).place(x=85, y=130)
    tk.Button(winmenuactivities, text="Salir",font=fontStyle, command=lambda:close(winmenuactivities),height=2,width=14).place(x=85, y=210)
    
    winmenuactivities.mainloop()
def list_activities(student):
    auxlist = []
    for i in student.activities:
        if i.status == "En curso":
            des = i.getDescripcion()
            course = i.course
            ac = str(des)+"/"+str(course)
            auxlist.append(ac)
    return auxlist
def mod_activities(status,ac,check,student):
        ac = ac.get()
        ac = ac.split("/")
        status = status.get()
        for i in student.activities:
            if i.getDescripcion() == ac[0] and i.getCourse() == ac[1]:
                i.setStatus(status)
                messagebox.showinfo("Actividades","Su actividad cambio con exito de estado")
                break
                
            if check == 1:
                files.create_file_students()
#-----------MENU REPORTES-----------#
def menureports(student):
    winmenureports = tk.Toplevel()
    winmenureports.title("Reportes")
    winmenureports.minsize(700,400)
    fontStyle = tkFont.Font(family="Lucida Grande", size=12)
    
    lb_date=tk.Label(winmenureports,text="Fecha de actividad:").place(x=10, y=40)
    sv_date = tk.StringVar()
    e_date= ttk.Entry(winmenureports, textvariable = sv_date, width=30).place(x=165, y=40)
    
    
    lb_filter= tk.Label(winmenureports,text="Seleccione si desea generar el reporte del dia o la semana:").place(x=10, y=70)
    sv_filter = tk.StringVar()
    combobox_filter = ttk.Combobox(winmenureports,values =["Dia","Semana"],textvariable=sv_filter,state="readonly").place(x=300,y=70)
    
    tk.Button(winmenureports, text="Generar reporte",font=fontStyle, command=lambda:gen_report(student,sv_date,sv_filter,winmenureports),height=2,width=14).place(x=300, y=220)
    tk.Button(winmenureports, text="Salir",font=fontStyle, command=lambda:close(winmenureports),height=2,width=14).place(x=450, y=220)
    
def gen_report(student,date,filter,win):

    if filter != '':
        report = functions_students.gen_reports(student,date,filter)
        if filter == "Dia":
            i = 0
            fontStyle = tkFont.Font(family="Lucida Grande", size=12)
            while len(report) > cont:
                descripcion = report[cont][0]
                Curso = report[cont][1]
                Fecha = report[cont][2]
                Horas = report[cont][3]
                estado = report[cont][5]
                lb_date=tk.Label(win,text="Reporte:").place(x=10, y=100)
                listbox = tk.Listbox(win).place(x=10,y=130)
                listbox.insert(0,descripcion)
                listbox.insert(1,Curso)
                listbox.insert(2,Fecha)
                listbox.insert(3,Horas)
                listbox.insert(4,estado)

                


                
               

    else:
        messagebox.showerror("Reportes","Tiene que ingresar si desea generar el reporte semanal o diario")

#-----------FUNCION LIMPIAR VENTANA PRINCIPAL-----------#
def clearwin(name,course,date,start_time,end_time):
    name.set('')
    course.set('')
    date.set('')
    start_time.set('')
    end_time.set('')
    

#-----------FUNCION CERRAR VENTANAS-----------#
def close(win):
    win.destroy()


