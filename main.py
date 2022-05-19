import tkinter as tk
from tkinter import ttk
import functions_admins
from obCareers import careers
import functions_students
from win_register import win_register_

carrera1 = careers("computacion")
carrera2 = careers("Fisica")
carrera3 = careers("Ingenieria")
functions_admins.list_careers.append(carrera1)
functions_admins.list_careers.append(carrera2)
functions_admins.list_careers.append(carrera3)


#Ventana principial
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
    global sv_nombre,sv_rank,sv_password
    name = sv_nombre.get()
    rank = sv_rank.get()
    password = sv_password.get()
    flag = False
    if rank == "Administrativo":
        for i in functions_admins.admins:
            if name == i.getName() and password == i.getPassword():
                flag = True
                #menu admins
                break
        if flag == False:
            print("El usuario o la contraseña son incorrectos")
    elif rank == "Estudiante":
        for a in functions_students.students:
            if name == a.getName() and password == a.getPassword():
                #menu estudiantes
                flag = True
                break
        if flag == False:
            print("El usuario o la contraseña son incorrectos")
#botónes de acción de la ventana
tk.Button(ventana_principal, text="Iniciar Sesion", command=check_login).place(x=80, y=130)
tk.Button(ventana_principal, text="Registarse", command=win_register_).place(x=80, y=160)
tk.Button(ventana_principal, text="Salir", command=None).place(x=80, y=190)

ventana_principal.mainloop()

