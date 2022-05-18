import tkinter as tk
from tkinter import N, ttk
#Ventana principial
win1 = tk.Tk()
win1.geometry('600x400')
win1.title('Proyecto 1')
def login():
    win2 = tk.Tk()
    win2.geometry('600x400')
    win2.title('Login')
    
    
label1 = ttk.Label(win1,text = "Administracion del tiempo")
button1 = ttk.Button(win1,text="Iniciar sesion",command=login)
button2 = ttk.Button(win1,text="Registrarse")
button3 = ttk.Button(win1,text="Salir")

button1.pack()
button2.pack()
button3.pack()
win1.mainloop()