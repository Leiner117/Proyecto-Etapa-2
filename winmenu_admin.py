
from datetime import date, datetime
import tkinter as tk
from tkinter import ttk,messagebox
import tkinter.font as tkFont
import functions_admins
from obclass_time import hours_class
from datetime import datetime
import files
listdays = []
careers_list = []
cont = 0

#-----------MENU ADMINISTRADOR-----------#
def menu(i,win):
    winmenuadmin = tk.Toplevel()
    winmenuadmin.title("Menu administrativo")
    winmenuadmin.minsize(700,400)
    fontStyle = tkFont.Font(family="Lucida Grande", size=14)
    lb_name=tk.Label(winmenuadmin,text="Bienvenido: "+i.getName(),font=fontStyle).place(x=10, y=10)
    lb_checksave = tk.Label(winmenuadmin,text="Auto guardado",font=fontStyle).place(x= 400,y=10)
    sv_checksave = tk.IntVar()
    btn_checksave = tk.Checkbutton(winmenuadmin,variable=sv_checksave).place(x= 540,y =15)
    tk.Button(winmenuadmin, text="Cursos",font=fontStyle, command=lambda:winCourses(i,sv_checksave.get()),height=2,width=8).place(x=300, y=70)
    tk.Button(winmenuadmin, text="Carreras",font=fontStyle, command=lambda:menucareers(sv_checksave.get()),height=2,width=8).place(x=300, y=150)
    tk.Button(winmenuadmin, text="Guardar cambios",font=fontStyle, command=save_changes,height=2,width=15).place(x=300, y=230)
    tk.Button(winmenuadmin, text="Salir",font=fontStyle, command=lambda:[show(win),close(winmenuadmin)],height=2,width=8).place(x=300, y=310)
    winmenuadmin.mainloop()

def save_changes():
    files.create_file_courses()
    files.create_file_career()

#-----------FUNCIONES PARA OCULTAR/MOSTRAR VENTANAS-----------#
def hide(win):
    win.withdraw()
def show(win):
    win.deiconify()



#-----------SUBMENU CARRERAS-----------#
def menucareers(check):

    wincareers = tk.Toplevel()

    wincareers.title("Manejo de carreras")
    wincareers.minsize(700,400)
    
    
    
    

    #nombre
    lb_namecareer=tk.Label(wincareers,text="Nombre de la carrera:").place(x=10, y=40)
    sv_namecareer = tk.StringVar()
    e_namecareer= ttk.Entry(wincareers, textvariable = sv_namecareer, width=30).place(x=140, y=40)

    
    tk.Button(wincareers, text="Crear carrera",command=lambda:[add_career(sv_namecareer,wincareers,check),close(wincareers)],height=2,width=15).place(x=10, y=300)
    tk.Button(wincareers, text="modifica carrera",command=lambda:winModCareer(check),height=2,width=15).place(x=150, y=300)
    tk.Button(wincareers, text="Salir",command=lambda:close(wincareers),height=2,width=15).place(x=290, y=300)




    wincareers.mainloop()
def winModCareer(check):
    winmod = tk.Toplevel()
    winmod.title("Manejo de carreras")
    winmod.minsize(700,400)
    
    lb_namecareer=tk.Label(winmod,text="Nuevo nombre de la carrera:").place(x=10, y=40)
    sv_namecareer = tk.StringVar()
    e_namecareer= ttk.Entry(winmod, textvariable = sv_namecareer, width=30).place(x=145, y=40)
    
    list_careers = listcareers()
    lb_career= tk.Label(winmod,text="Carrera:").place(x=10, y=90)
    sv_career = tk.StringVar()
    combobox_career = ttk.Combobox(winmod,values =list_careers,textvariable=sv_career,state="readonly").place(x=110,y=90)
    
    tk.Button(winmod, text="modifica carrera",command=lambda:[mod_career(sv_career,sv_namecareer,check),close(winmod)],height=2,width=15).place(x=10, y=300)
    winmod.mainloop()
def add_career(name,win,check):
    name = name.get()
    functions_admins.add_careers(name,win)
    if check == 1:
        files.create_file_career()
def mod_career(name,new_name,check):
    name = name.get()
    obcourse = None
    for i in functions_admins.list_careers:
        if name == i.getName():
            obcourse = i
            break
    if obcourse != None:
        obcourse.setName(new_name.get())
    if check == 1:
        files.create_file_career()
    
#-----------SUBMENU CURSOS-----------#
def winCourses(i,check):
    if len(functions_admins.list_careers) > 0:
        winmenucourse = tk.Toplevel()
        winmenucourse.title("Manejo de cursos")
        winmenucourse.minsize(800,600)
        
        #nombre
        lb_name_course=tk.Label(winmenucourse,text="Nombre:").place(x=10, y=40)
        sv_name_course = tk.StringVar()
        e_name_course= ttk.Entry(winmenucourse, textvariable = sv_name_course, width=30).place(x=80, y=40)
        
        lb_credits=tk.Label(winmenucourse,text="creditos:").place(x=10, y=70)
        sv_credits = tk.StringVar()
        e_credits= ttk.Entry(winmenucourse, textvariable = sv_credits, width=30).place(x=80, y=70)
        
        lb_startdate=tk.Label(winmenucourse,text="Fecha de inicio('aaaa/mm/dd'):").place(x=10, y=100)
        sv_startdate = tk.StringVar()
        e_startdate= ttk.Entry(winmenucourse, textvariable = sv_startdate, width=30).place(x=190, y=100)
        
        lb_enddate=tk.Label(winmenucourse,text="Fecha de finalización('aaaa/mm/dd'):").place(x=10, y=130)
        sv_enddate = tk.StringVar()
        e_endate= ttk.Entry(winmenucourse, textvariable = sv_enddate, width=30).place(x=220, y=130)
        
        week = ["LUNES","MARTES","MIERCOLES","JUEVES","VIERNES","SABADO","DOMINGO"]
        lb_week= tk.Label(winmenucourse,text="Dia de la semana:").place(x=10, y=160)
        sv_week = tk.StringVar()
        combobox_week = ttk.Combobox(winmenucourse,values = week,textvariable=sv_week,state="readonly").place(x=110,y=160)
        
        lb_startime=tk.Label(winmenucourse,text="Hora de inicio(HH:MM):").place(x=10, y=190)
        sv_startime = tk.StringVar()
        e_startime= ttk.Entry(winmenucourse, textvariable = sv_startime, width=30).place(x=150, y=190)
        
        lb_endtime=tk.Label(winmenucourse,text="Hora de finalización(HH:MM):").place(x=10, y=220)
        sv_endtime = tk.StringVar()
        e_endtime= ttk.Entry(winmenucourse, textvariable = sv_endtime, width=30).place(x=180, y=220)
        tk.Button(winmenucourse, text="Agregar dia de clases",command=lambda:[create_hour(sv_week,sv_startime,sv_endtime,week),clear_setdays(sv_startime,sv_endtime,sv_week)],height=2,width=20).place(x=10, y=250)

        list_careers = listcareers()
        lb_career= tk.Label(winmenucourse,text="Carrera asociada:").place(x=10, y=300)
        sv_career = tk.StringVar()
        combobox_career = ttk.Combobox(winmenucourse,values =list_careers,textvariable=sv_career,state="readonly").place(x=110,y=300)

        tk.Button(winmenucourse, text="Asociar carrera",command=lambda:[create_listcareer(sv_career),clear_career(sv_career)],height=2,width=20).place(x=10, y=350)
        
        tk.Button(winmenucourse, text="Registrar curso",command=lambda:[add_course(sv_name_course.get(),sv_credits.get(),sv_startdate.get(),sv_enddate.get(),listdays,careers_list,check),clear_window(sv_name_course,sv_credits,sv_startdate,sv_enddate)],height=2,width=20).place(x=10, y=400)
        

        winmenucourse.mainloop()
    else:
        messagebox.showinfo("Agregar curso","No Existen carreras disponibles")
        

def add_course(name,credits,start_date,end_date,days,career_list,check):
    if len(days) > 0 and len(career_list) > 0:
        try:
            start_date = datetime.strptime(start_date, '%Y/%m/%d')
            end_date = datetime.strptime(end_date, '%Y/%m/%d')
            functions_admins.add_courses(name,credits,start_date,end_date,days,career_list)
            if check == 1:
                files.create_file_courses()
        except:
            
            messagebox.showinfo("Agregar curso","No ingreso el formato de la fecha correcto")
    else:
        messagebox.showerror("Agregar curso","Tienes que asociar dias de clases y una carrera al curso")
def create_listcareer(c):
    career = functions_admins.select_position_careers(c.get())
    careers_list.append(career)
def create_hour(day,starttime,endtime,week):
    day = functions_admins.selectday(day.get(),week)
    start_time = starttime.get()
    end_time = endtime.get()
    try:
       start_time = datetime.strptime(start_time, '%H:%M')
       end_time = datetime.strptime(end_time, '%H:%M')
       obhour = hours_class(day,start_time,end_time)
       listdays.append(obhour)
       
    except:
        messagebox.showinfo("Agregar curso","No ingreso el formato de hora correcto")
def listcareers():
    auxlist = []
    for i in functions_admins.list_careers:
        auxlist.append(i.getName())
    return auxlist
def clear_window(name,credits,start_date,end_date):
    global careers_list,listdays
    name.set('')
    credits.set('')
    start_date.set('')
    end_date.set('')
    listdays = []
    careers_list = []

#-----------LIMPIAR VENTANAS-----------#
def clear_setdays(start_time,end_time,week):
    start_time.set('')
    end_time.set('')
    week.set('')
def clear_career(career):
    career.set('')

#-----------FUNCION CERRAR VENTANA-----------#
def close(win):
    win.destroy()

