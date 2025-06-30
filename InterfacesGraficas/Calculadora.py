from tkinter import *


def Calcular(parValue):
    try:
        if (parValue == "⌫"):
            res = txtCalc.get()[:-1]  # Quita el ultimo digito de la cadena
            txtCalc.set(res)
            return
        if (parValue == "+" or parValue == "-" or parValue == "/" or parValue == "*"):
            ultimoDigito = txtCalc.get()[-1] if txtCalc.get() else None
            if (ultimoDigito == None):  # Si el primer digito no es un numero no se mostrara
                return
            if (ultimoDigito == "+" or ultimoDigito == "-" or ultimoDigito == "/" or ultimoDigito == "*"):
                res = txtCalc.get()[:-1]  # Quita el ultimo digito de la cadena
                txtCalc.set(res)

        if parValue == 'C':
            txtCalc.set('')  # Limpiar
        elif parValue == '=':
            try:
                # eval evalua cadenas de texto y ejecuta como si fuera codigo python
                resultado = str(eval(txtCalc.get()))
                txtCalc.set(resultado)
            except:
                txtCalc.set("Error")
        else:

            # Concatenar lo que se va ingresando
            txtCalc.set(txtCalc.get() + parValue)
    except Exception as e:  # Captura cualquier otro error
        txtCalc.set("Error")
        print(f"Error inesperado: {type(e).__name__}: {e}")


raiz = Tk()
raiz.title("Calculadora")

txtCalc = StringVar()

# Caja de texto donde se muestra el resultado y la captura de numeros
entrada = Entry(raiz, textvariable=txtCalc, font=('Arial', 16),
                bd=10, insertwidth=2, width=15, borderwidth=4, justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Primer renglon de botones
boton7 = Button(raiz, text="7", width=5, height=2, font=(
    'Arial', 12, 'bold'), command=lambda: Calcular("7"))
boton7.grid(row=1, column=0)
boton8 = Button(raiz, text="8", width=5, height=2, font=(
    'Arial', 12, 'bold'), command=lambda: Calcular("8"))
boton8.grid(row=1, column=1)
boton9 = Button(raiz, text="9", width=5, height=2, font=(
    'Arial', 12, 'bold'), command=lambda: Calcular("9"))
boton9.grid(row=1, column=2)
botonBorrar = Button(raiz, text="⌫", width=5, height=2, font=(
    'Arial', 12, 'bold'), command=lambda: Calcular("⌫"))
botonBorrar.grid(row=1, column=3)

# Segunda linea de botones
boton4 = Button(raiz, text="4", width=5, height=2, font=(
    'Arial', 12, 'bold'), command=lambda: Calcular("4"))
boton4.grid(row=2, column=0)
boton5 = Button(raiz, text="5", width=5, height=2, font=(
    'Arial', 12, 'bold'), command=lambda: Calcular("5"))
boton5.grid(row=2, column=1)
boton6 = Button(raiz, text="6", width=5, height=2, font=(
    'Arial', 12, 'bold'), command=lambda: Calcular("6"))
boton6.grid(row=2, column=2)
botonDiv = Button(raiz, text="/", width=5, height=2, font=(
    'Arial', 12, 'bold'), command=lambda: Calcular("/"))
botonDiv.grid(row=2, column=3)

# Tercer linea de botones
boton1 = Button(raiz, text="1", width=5, height=2, font=(
    'Arial', 12, 'bold'), command=lambda: Calcular("1"))
boton1.grid(row=3, column=0)
boton2 = Button(raiz, text="2", width=5, height=2, font=(
    'Arial', 12, 'bold'), command=lambda: Calcular("2"))
boton2.grid(row=3, column=1)
boton3 = Button(raiz, text="3", width=5, height=2, font=(
    'Arial', 12, 'bold'), command=lambda: Calcular("3"))
boton3.grid(row=3, column=2)
botonMulti = Button(raiz, text="*", width=5, height=2, font=(
    'Arial', 12, 'bold'), command=lambda: Calcular("*"))
botonMulti.grid(row=3, column=3)

# Cuarta linea de botones
botonC = Button(raiz, text="C", width=5, height=2, font=(
    'Arial', 12, 'bold'), command=lambda: Calcular("C"))
botonC.grid(row=4, column=0)
boton0 = Button(raiz, text="0", width=5, height=2, font=(
    'Arial', 12, 'bold'), command=lambda: Calcular("0"))
boton0.grid(row=4, column=1)
botonMas = Button(raiz, text="+", width=5, height=2, font=(
    'Arial', 12, 'bold'), command=lambda: Calcular("+"))
botonMas.grid(row=4, column=2)
botonMenos = Button(raiz, text="-", width=5, height=2, font=(
    'Arial', 12, 'bold'), command=lambda: Calcular("-"))
botonMenos.grid(row=4, column=3)


botonIgual = Button(raiz, text="=", height=2, font=(
    'Arial', 12, 'bold'), command=lambda: Calcular("="))
botonIgual.grid(row=5, column=0, columnspan=4, sticky="we")


for child in raiz.winfo_children():
    child.grid_configure(padx=5, pady=5)

raiz.mainloop()
