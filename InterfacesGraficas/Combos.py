from tkinter import *
from tkinter import ttk

raiz= Tk()

estado = StringVar()

comboEstado = ttk.Combobox(raiz, textvariable=estado)
comboEstado.grid()
comboEstado['values']=("Jalisco", "Nayarit", "Colima", "CDMX")

raiz.mainloop()