from tkinter import *
from tkinter import ttk
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "logoPython.png")


raiz = Tk()
boton = ttk.Button(raiz, text="Botón solo texto")
boton.grid()
imagen = PhotoImage()

if os.path.exists(image_path):
    imagen = PhotoImage(file=image_path)
else:
    print("No existe imagen")

btnImage = ttk.Button(raiz)
btnImage.grid()
btnImage['image'] = imagen

btnCombinada = ttk.Button(raiz, text="Boton Combinado", compound="center")
btnCombinada.grid()
btnCombinada['image'] = imagen

chkButon = ttk.Checkbutton(raiz, text="Option 1")
chkButon.grid()

raiz.mainloop()
