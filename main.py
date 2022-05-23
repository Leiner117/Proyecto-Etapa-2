import tkinter as tk
from tkinter import ttk
import functions_admins
from obCareers import careers
import functions_students
from win_register import win_register_
import winmenu_admin,winmenu_student
import files


def load_files():
    files.load_courses()
    files.load_file_admins()
    files.load_file_career()
    files.load_file_students()
#Ventana principial
load_files()
ventana_principal = tk.Tk()
ventana_principal.title("Aplicación principal")
ventana_principal.minsize(800,600)
#nombre

lb_nombre=tk.Label(ventana_principal,text="Nombre:").place(x=10, y=40)
sv_nombre = tk.StringVar()
e_nombre = ttk.Entry(ventana_principal, textvariable = sv_nombre, width=50).place(x=80, y=40)

#password
lb_password=tk.Label(ventana_principal,text="Contraseña: ").place(x=10, y=70)
sv_password = tk.StringVar()
e_password = ttk.Entry(ventana_principal, textvariable = sv_password, width=20).place(x=80, y=70)

lb_rank= tk.Label(ventana_principal,text="Rango:").place(x=10, y=100)
sv_rank = tk.StringVar()
combobox_rank = ttk.Combobox(ventana_principal,values=["Administrativo","Estudiante"],textvariable=sv_rank,state="readonly").place(x=80,y=100)

def check_login():
    global sv_nombre,sv_rank,sv_password,ventana_principal
    name = sv_nombre.get()
    rank = sv_rank.get()
    password = sv_password.get()
    flag = False
    if rank == "Administrativo":
        for i in functions_admins.list_admins:
            if name == i.getName() and password == i.getPassword():
                flag = True
                ventana_principal.withdraw()
                winmenu_admin.menu(i,ventana_principal)
                break
        if flag == False:
            print("El usuario o la contraseña son incorrectos")
    elif rank == "Estudiante":
        for a in functions_students.list_students:
            if name == a.getName() and password == a.getPassword():
                ventana_principal.withdraw()
                winmenu_student.menu(a,ventana_principal)
                flag = True
                break
        if flag == False:
            print("El usuario o la contraseña son incorrectos")
        
#botónes de acción de la ventana

def close():
    ventana_principal.destroy()
tk.Button(ventana_principal, text="Iniciar Sesion", command=check_login).place(x=80, y=130)
tk.Button(ventana_principal, text="Registarse", command=win_register_).place(x=80, y=160)
tk.Button(ventana_principal, text="Salir", command=close).place(x=80, y=190)


ventana_principal.mainloop()