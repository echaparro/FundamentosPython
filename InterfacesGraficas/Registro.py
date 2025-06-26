from tkinter import *
from tkinter import ttk

# Estados
estados = ("Estados (32)",
           "Aguascalientes", "Baja California", "Baja California Sur", "Campeche",
           "Chiapas", "Chihuahua", "Coahuila", "Colima", "Ciudad de México", "Durango",
           "Estado de México", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco",
           "Michoacán", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla",
           "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora",
           "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas"
           )


# Configuración principal
raiz = Tk()
raiz.title("Ejercicio -- Registro")

marcoPrincipal = ttk.Frame(raiz, padding="3 3 12 12")
marcoPrincipal.grid(column=0, row=0, sticky=(N, W, E, S))
marcoPrincipal.columnconfigure(0, weight=1)
marcoPrincipal.rowconfigure(0, weight=1)

# Contenedor para el registro
marcoRegistro = ttk.LabelFrame(
    marcoPrincipal, text="Registro:", padding="3 3 12 12", relief="ridge")
marcoRegistro.grid(column=0, row=0, sticky=(N, W, E, S))
marcoRegistro.columnconfigure(0, weight=1)
marcoRegistro.rowconfigure(0, weight=1)

nombre = StringVar()
apaterno = StringVar()
amaterno = StringVar()
correo = StringVar()
movil = StringVar()

ttk.Label(marcoRegistro, text="Nombre:").grid(
    row=0, column=0, sticky=W, pady=2)
ttk.Entry(marcoRegistro, textvariable=nombre).grid(
    row=0, column=1, sticky=EW, pady=2)

ttk.Label(marcoRegistro, text="A. Paterno:").grid(
    row=1, column=0, sticky=W, pady=2)
ttk.Entry(marcoRegistro, textvariable=apaterno).grid(
    row=1, column=1, sticky=EW, pady=2)

ttk.Label(marcoRegistro, text="A. Materno:").grid(
    row=2, column=0, sticky=W, pady=2)
ttk.Entry(marcoRegistro, textvariable=amaterno).grid(
    row=2, column=1, sticky=EW, pady=2)

ttk.Label(marcoRegistro, text="Correo:").grid(
    row=3, column=0, sticky=W, pady=2)
ttk.Entry(marcoRegistro, textvariable=correo).grid(
    row=3, column=1, sticky=EW, pady=2)

ttk.Label(marcoRegistro, text="Móvil:").grid(row=4, column=0, sticky=W, pady=2)
ttk.Entry(marcoRegistro, textvariable=movil).grid(
    row=4, column=1, sticky=EW, pady=2)


# ---Contenedor para las aficiones
marcoAficiones = ttk.LabelFrame(
    marcoPrincipal, text="Aficiones:", padding="10")
marcoAficiones.grid(column=0, row=2, sticky=(N, W, E, S))
marcoAficiones.columnconfigure(0, weight=1)
marcoAficiones.rowconfigure(0, weight=1)

chkButonLeer = ttk.Checkbutton(marcoAficiones, text="Leer")
chkButonLeer.grid(column=0, row=0, sticky=E)

chkButonMusica = ttk.Checkbutton(marcoAficiones, text="Música")
chkButonMusica.grid(column=1, row=0, sticky=E)

chkButonVideojuegos = ttk.Checkbutton(marcoAficiones, text="Videojuegos")
chkButonVideojuegos.grid(column=2, row=0, sticky=E)


# Ccontenedor de Radios
marcoSituacion = ttk.Frame(marcoPrincipal, padding="3 3 12 12")
marcoSituacion.grid(column=2, row=0, sticky=(N, W, E, S))
marcoSituacion.columnconfigure(0, weight=1)
marcoSituacion.rowconfigure(0, weight=1)
marcoSituacion.rowconfigure(1, weight=1)
marcoSituacion.rowconfigure(2, weight=1)

situacion = StringVar(value="Estudiante")  # Valor por defecto

rbEstudiante = ttk.Radiobutton(
    marcoSituacion, text="Estudiante", value='Estudiante')
rbEstudiante.grid(column=0, row=0, sticky=(S, W))

rbEmpleado = ttk.Radiobutton(marcoSituacion, text="Empleado", value='Empleado')
rbEmpleado.grid(column=0, row=1, sticky="W")

rbDesempleado = ttk.Radiobutton(
    marcoSituacion, text="Desempleado", value='Desempleado')
rbDesempleado.grid(column=0, row=2, sticky=(N, W))

# Estados

estado = StringVar()
comboEstado = ttk.Combobox(marcoPrincipal, textvariable=estado)
comboEstado.grid(column=2, row=2, sticky=(E))
comboEstado['values'] = estados
comboEstado.set(estados[0])

# Botones

botonSave = ttk.Button(marcoPrincipal, text="Guardar")
botonSave.grid(column=0, row=3, sticky=(W))

botonCancel = ttk.Button(marcoPrincipal, text="Cancelar")
botonCancel.grid(column=0, row=3, sticky=(E))

for child in marcoPrincipal.winfo_children():
    child.grid_configure(padx=5, pady=5)

raiz.mainloop()



"""
Arbol de widgets

Tk (raiz)
└---- ttk.Frame (marcoPrincipal)
    ├---- ttk.LabelFrame (marcoRegistro)
    │   ├---- ttk.Label (text="Nombre:")
    │   ├---- ttk.Entry (variable=nombre)
    │   ├---- ttk.Label (text="A. Paterno:")
    │   ├---- ttk.Entry (variable=apaterno)
    │   ├---- ttk.Label (text="A. Materno:")
    │   ├---- ttk.Entry (variable=amaterno)
    │   ├---- ttk.Label (text="Correo:")
    │   ├---- ttk.Entry (variable=correo)
    │   ├---- ttk.Label (text="Móvil:")
    │   └---- ttk.Entry (variable=movil)
    │
    ├---- ttk.LabelFrame (marcoAficiones)
    │   ├---- ttk.Checkbutton (text="Leer")
    │   ├---- ttk.Checkbutton (text="Música")
    │   └---- ttk.Checkbutton (text="Videojuegos")
    │
    ├---- ttk.Frame (marcoSituacion)
    │   ├---- ttk.Radiobutton (text="Estudiante", value='Estudiante')
    │   ├---- ttk.Radiobutton (text="Empleado", value='Empleado')
    │   └---- ttk.Radiobutton (text="Desempleado", value='Desempleado')
    │
    ├---- ttk.Combobox (comboEstado)
    ├---- ttk.Button (text="Guardar")
    └---- ttk.Button (text="Cancelar")"""