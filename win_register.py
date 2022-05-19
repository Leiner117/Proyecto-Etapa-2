from ast import Lambda
import tkinter as tk
from tkinter import ttk,messagebox
import functions_admins
from obCareers import careers

import functions_students

def win_register_():
    if len(functions_admins.list_careers) > 0:
        winregister = tk.Toplevel()
        winregister.title("Registro estudiantes")
        winregister.minsize(800,600)
        #nombre
        lb_name_student=tk.Label(winregister,text="Nombre:").place(x=10, y=40)
        sv_name_student = tk.StringVar()
        e_name_student= ttk.Entry(winregister, textvariable = sv_name_student, width=50).place(x=80, y=40)
        
        #password
        
        lb_password_student=tk.Label(winregister,text="Contraseña: ").place(x=10, y=70)
        sv_password_student = tk.StringVar()
        e_password_student = ttk.Entry(winregister, textvariable = sv_password_student, width=20).place(x=80, y=70)   
        #email
        lb_email_student=tk.Label(winregister,text="Email:").place(x=10, y=100)
        sv_email_student = tk.StringVar()
        e_email_student = ttk.Entry(winregister, textvariable = sv_email_student, width=50).place(x=80, y=100)
        
        
        #lista de carreras
        list_careers = chargecareers()
        lb_careers= tk.Label(winregister,text="Carrera:").place(x=10, y=130)
        sv_career = tk.StringVar()
        combobox_career = ttk.Combobox(winregister,values=list_careers,textvariable=sv_career,state="readonly").place(x=80,y=130)
        
        tk.Button(winregister, text="Registrar", command=lambda:register_student(sv_name_student,sv_email_student,sv_career,sv_password_student)).place(x=80, y=160)
        tk.Button(winregister, text="Salir", command=lambda:close(winregister)).place(x=80, y=190)
        winregister.mainloop()
    else:
        messagebox.showinfo("Registro","No hay carreras disponibles")
        
def chargecareers():
    auxlist = []
    for i in functions_admins.list_careers:
        auxlist.append(i.getName())
    return auxlist

def register_student(name,email,career,password): 
    strname = name.get()
    stremail = email.get()
    strpassword = password.get()
    strcareer = career.get()
    career = functions_admins.select_position_careers(strcareer)
    register = functions_students.register(strname,stremail,career,strpassword)
    if register == False:
        messagebox.showinfo("Registro","Te has registrado con exito!!! ")
    else:
        messagebox.showinfo("Registro","Error, El usuario ya se encuentra registrado!!. ")
        
def close(win):
    win.destroy()
