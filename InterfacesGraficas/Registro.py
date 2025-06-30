from tkinter import *
from tkinter import ttk
import csv
from tkinter import messagebox

ruta_archivo = "./InterfacesGraficas/registros.csv"
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

# Variables para los campos
nombre = StringVar()
apaterno = StringVar()
amaterno = StringVar()
correo = StringVar()
movil = StringVar()
situacion = StringVar(value="Estudiante")
leer = IntVar()
musica = IntVar()
videojuegos = IntVar()
estado = StringVar()

# Contenedor para el registro
marcoRegistro = ttk.LabelFrame(
    marcoPrincipal, text="Registro:", padding="3 3 12 12", relief="ridge")
marcoRegistro.grid(column=0, row=0, sticky=(N, W, E, S))
marcoRegistro.columnconfigure(0, weight=1)
marcoRegistro.rowconfigure(0, weight=1)

# Campos del formulario
ttk.Label(marcoRegistro, text="Nombre:").grid(
    row=0, column=0, sticky=W, pady=2)
ttk.Entry(marcoRegistro, textvariable=nombre, width=100).grid(
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

# Aficiones
marcoAficiones = ttk.LabelFrame(
    marcoPrincipal, text="Aficiones:", padding="10")
marcoAficiones.grid(column=0, row=2, sticky=(N, W, E, S))

chkButonLeer = ttk.Checkbutton(marcoAficiones, text="Leer", variable=leer)
chkButonLeer.grid(column=0, row=0, sticky=E)

chkButonMusica = ttk.Checkbutton(
    marcoAficiones, text="Música", variable=musica)
chkButonMusica.grid(column=1, row=0, sticky=E)

chkButonVideojuegos = ttk.Checkbutton(
    marcoAficiones, text="Videojuegos", variable=videojuegos)
chkButonVideojuegos.grid(column=2, row=0, sticky=E)

# Situación
marcoSituacion = ttk.Frame(marcoPrincipal, padding="3 3 12 12")
marcoSituacion.grid(column=2, row=0, sticky=(N, W, E, S))

rbEstudiante = ttk.Radiobutton(
    marcoSituacion, text="Estudiante", variable=situacion, value='Estudiante')
rbEstudiante.grid(column=0, row=0, sticky=(S, W))

rbEmpleado = ttk.Radiobutton(
    marcoSituacion, text="Empleado", variable=situacion, value='Empleado')
rbEmpleado.grid(column=0, row=1, sticky="W")

rbDesempleado = ttk.Radiobutton(
    marcoSituacion, text="Desempleado", variable=situacion, value='Desempleado')
rbDesempleado.grid(column=0, row=2, sticky=(N, W))

# Estados
comboEstado = ttk.Combobox(marcoPrincipal, textvariable=estado)
comboEstado.grid(column=2, row=2, sticky=(E))
comboEstado['values'] = estados
comboEstado.set(estados[0])

# Grid para mostrar los registros
treeRegistros = ttk.Treeview(marcoPrincipal, columns=(
    "Nombre", "A. Paterno", "A. Materno", "Correo", "Móvil", "Situación", "Aficiones", "Estado"), show="headings")
treeRegistros.grid(column=0, row=4, columnspan=3, sticky=(N, S, E, W))

# Configurar columnas
treeRegistros.heading("Nombre", text="Nombre")
treeRegistros.heading("A. Paterno", text="A. Paterno")
treeRegistros.heading("A. Materno", text="A. Materno")
treeRegistros.heading("Correo", text="Correo")
treeRegistros.heading("Móvil", text="Móvil")
treeRegistros.heading("Situación", text="Situación")
treeRegistros.heading("Aficiones", text="Aficiones")
treeRegistros.heading("Estado", text="Estado")

# Ajustar columnas
for col in treeRegistros["columns"]:
    treeRegistros.column(col, width=100, anchor=CENTER)


def GuardarCSV():
    aficiones = []
    if leer.get() == 1:
        aficiones.append("Leer")
    if musica.get() == 1:
        aficiones.append("Música")
    if videojuegos.get() == 1:
        aficiones.append("Videojuegos")
    aficion = ", ".join(aficiones)  # Se crea el string con la , inicial

    datos = [
        nombre.get(),
        apaterno.get(),
        amaterno.get(),
        correo.get(),
        movil.get(),
        situacion.get(),
        aficion,
        estado.get()
    ]  # Se arma el array de datos para grabarlo en el csv

    # Validar campos obligatorios
    if not nombre.get() or not apaterno.get() or not correo.get() or estado.get() == "Estados (32)":
        messagebox.showerror(
            "Error", "Los campos Nombre, Apellido Paterno Correo y Estado son obligatorios")
        return

    try:
        # print("Ruta-------------")
        # print(ruta_archivo)
        with open(ruta_archivo, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Si el archivo está vacío, escribir encabezados
            if file.tell() == 0:
                writer.writerow(["Nombre", "Apellido Paterno", "Apellido Materno",
                                "Correo", "Móvil", "Situación", "Aficiones", "Estado"])
            writer.writerow(datos)

        # Actualizar el grid de registros
        updateGrid()
        messagebox.showinfo("Éxito", "Datos guardados correctamente")

        # Limpiar campos
        cancelar()  # Se reutiliza el boton de cancelar
    except Exception as e:
        messagebox.showerror(
            "Error", f"No se pudo guardar el archivo: {str(e)}")


# Función para actualizar el grid de los registros
def updateGrid():
    # Limpiar el treeRegistrosview
    for item in treeRegistros.get_children():
        treeRegistros.delete(item)

    try:
        with open(ruta_archivo, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar encabezados
            for i, row in enumerate(reader, 1):
                # print("-----------")
                # print(row)
                # print(i)
                treeRegistros.insert("", "end", values=row)
    except FileNotFoundError:
        pass


# Función para cancelar limpia los registros del formulario
def cancelar():
    nombre.set("")
    apaterno.set("")
    amaterno.set("")
    correo.set("")
    movil.set("")
    situacion.set("Estudiante")
    leer.set(0)
    musica.set(0)
    videojuegos.set(0)
    estado.set(estados[0])


# Botones
botonSave = ttk.Button(marcoPrincipal, text="Guardar", command=GuardarCSV)
botonSave.grid(column=0, row=3, sticky=(W))

botonCancel = ttk.Button(marcoPrincipal, text="Cancelar", command=cancelar)
botonCancel.grid(column=0, row=3, sticky=(E))

# Cargar datos existentes al iniciar
updateGrid()

for child in marcoPrincipal.winfo_children():
    child.grid_configure(padx=5, pady=5)

raiz.mainloop()


"""
Arbol de widgets
Tk (raiz)
└---- ttk.Frame (marcoPrincipal)
    ├---- ttk.LabelFrame (marcoRegistro)
    │   ├---- ttk.Label "Nombre:"
    │   ├---- ttk.Entry nombre
    │   ├---- ttk.Label "A. Paterno:"
    │   ├---- ttk.Entry apaterno
    │   ├---- ttk.Label "A. Materno:"
    │   ├---- ttk.Entry amaterno
    │   ├---- ttk.Label "Correo:"
    │   ├---- ttk.Entry correo
    │   ├---- ttk.Label "Móvil:"
    │   └---- ttk.Entry movil
    │
    ├---- ttk.LabelFrame (marcoAficiones)
    │   ├---- ttk.Checkbutton "Leer"
    │   ├---- ttk.Checkbutton "Música"
    │   └---- ttk.Checkbutton "Videojuegos"
    │
    ├---- ttk.Frame (marcoSituacion)
    │   ├---- ttk.Radiobutton "Estudiante"
    │   ├---- ttk.Radiobutton "Empleado"
    │   └---- ttk.Radiobutton "Desempleado"
    │
    ├---- ttk.Combobox (comboEstado)
    │
    ├---- ttk.Treeview (treeRegistros)
    │   ├---- Column "Nombre"
    │   ├---- Column "A. Paterno"
    │   ├---- Column "A. Materno"
    │   ├---- Column "Correo"
    │   ├---- Column "Móvil"
    │   ├---- Column "Situación"
    │   ├---- Column "Aficiones"
    │   └---- Column "Estado"
    │
    ├---- ttk.Button "Guardar"
    └---- ttk.Button "Cancelar" 
    
    """
