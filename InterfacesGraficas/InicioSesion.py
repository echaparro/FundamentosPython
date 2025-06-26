from tkinter import *
from tkinter import ttk


def ValidaSesion(*args):
    try:
        USER = "user"
        PASS = "123"
        if (currentUser.get() == USER and currentPass.get() == PASS):
            lblResult.set("Usuario Correcto !!!")
        else:
            lblResult.set("Usuario Incorrecto")

    except ValueError:
        pass


raiz = Tk()
raiz.title("Inicio de Sesión")

marcoPrincipal = ttk.Frame(raiz, padding="3 3 12 12")
marcoPrincipal.grid(column=0, row=0, sticky=(N, W, E, S))
marcoPrincipal.columnconfigure(0, weight=1)
marcoPrincipal.rowconfigure(0, weight=1)

currentUser = StringVar()
currentPass = StringVar()
lblResult = StringVar()

ttk.Label(marcoPrincipal, text="Usuario:").grid(column=1, row=1, sticky=W)
txtUser = ttk.Entry(marcoPrincipal, width=20, textvariable=currentUser)
txtUser.grid(column=2, row=1, sticky=(W, E))


ttk.Label(marcoPrincipal, text="Contraseña:").grid(column=1, row=2, sticky=W)
txtPass = ttk.Entry(marcoPrincipal,  show="*",
                    width=7, textvariable=currentPass)
txtPass.grid(column=2, row=2, sticky=(W, E))

ttk.Label(marcoPrincipal, textvariable=lblResult).grid(
    column=1, row=3, sticky=W)

ttk.Button(marcoPrincipal, text="Ingresar",
           command=ValidaSesion).grid(column=2, row=3, sticky=E)


for child in marcoPrincipal.winfo_children():
    child.grid_configure(padx=5, pady=5)

txtUser.focus()
raiz.bind('<Return>', ValidaSesion)

raiz.mainloop()


"""
Arbol de widgets
Tk (raiz)
└---- ttk.Frame (marcoPrincipal)
    ├---- ttk.Label (Etiqueta "Usuario:")
    ├---- ttk.Entry (Cuadro de texto: txtUser)
    ├---- ttk.Label (Etiqueta "Contraseña:")
    ├---- ttk.Entry (Cuadro de texto: txtPass)
    ├---- ttk.Label (Muestra lblResult)
    └---- ttk.Button (Botón "Ingresar")"""
