from tkinter import *
from tkinter import ttk
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "logoPython.png")


raiz = Tk()
etqTexto = ttk.Label(raiz, text="Etiqueta solo texto")
etqTexto.grid()
imagen = PhotoImage()

if os.path.exists(image_path):
    imagen = PhotoImage(file=image_path)
else:
    print("No existe imagen")

etqImagen = ttk.Label(raiz)
etqImagen.grid()
etqImagen['image'] = imagen

etqCombinada = ttk.Label(raiz, text="EtqCombinada", compound="center")
etqCombinada.grid()
etqCombinada['image'] = imagen

raiz.mainloop()
