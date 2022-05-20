
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
def menu(student):
    winmenustudent = tk.Toplevel()
    winmenustudent.title("Menu Estudiantes")
    winmenustudent.minsize(700,400)
    fontStyle = tkFont.Font(family="Lucida Grande", size=12)
    lb_name=tk.Label(winmenustudent,text="Bienvenido: "+student.getName(),font=fontStyle).place(x=10, y=10)
    
    tk.Button(winmenustudent, text="Cambiar carrera",font=fontStyle, command=None,height=2,width=14).place(x=150, y=70)
    tk.Button(winmenustudent, text="Matricular cursos",font=fontStyle, command=lambda:menuaddcourse(student),height=2,width=14).place(x=300, y=70)
    tk.Button(winmenustudent, text="Agregar actividad",font=fontStyle, command=None,height=2,width=14).place(x=450, y=70)
    tk.Button(winmenustudent, text="Modificar curso",font=fontStyle, command=None,height=2,width=14).place(x=150, y=150)
    tk.Button(winmenustudent, text="actividades",font=fontStyle, command=None,height=2,width=14).place(x=300, y=150)
    tk.Button(winmenustudent, text="Reportes",font=fontStyle, command=None,height=2,width=14).place(x=450, y=150)
    tk.Button(winmenustudent, text="Salir",font=fontStyle, command=None,height=2,width=14).place(x=300, y=220)
    
    winmenustudent.mainloop()
def menuchangecareer():
    pass

def menuaddcourse(student):
    winmenucourse = tk.Toplevel()
    winmenucourse.title("Matricular cursos")
    winmenucourse.minsize(700,400)
    fontStyle = tkFont.Font(family="Lucida Grande", size=12)
    listcourses = gencourses(student)
    
    lb_course= tk.Label(winmenucourse,text="Curso:").place(x=10, y=40)
    sv_course = tk.StringVar()
    combobox_course = ttk.Combobox(winmenucourse,values =listcourses,textvariable=sv_course,state="readonly").place(x=80,y=40)
    tk.Button(winmenucourse, text="Matricular",font=fontStyle, command=lambda:functions_students.assign_course(student,sv_course),height=2,width=14).place(x=300, y=220)
    tk.Button(winmenucourse, text="Salir",font=fontStyle, command=None,height=2,width=14).place(x=450, y=220)
    
def gencourses(student):
    auxlist = []
    for i in functions_admins.courses:
        for a in i.careers_belong:
            if student.getCareer().getName() == a.getName():
                auxlist.append(i.getName())
    return auxlist
    
    




def menuaddactivities():
    
    pass
def menumodcourse():
    pass
def printactivities():
    pass
def menureports():
    pass



def close(win):
    win.destroy()

