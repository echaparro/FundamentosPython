
# -------------- Encapsulamiento--------------------------
#  Por convención, se usa un guion bajo _ para indicar que un atributo/método es "privado" (aunque técnicamente sigue siendo accesible).

#  Con doble guion bajo __, Python aplica name mangling (cambia el nombre del atributo para dificultar su acceso desde fuera).
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo "privado" (name mangling)

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def obtener_saldo(self):  # Método público para acceder al saldo
        return self.__saldo

# -------------------Herencia--------------------
# La herencia es pasar atributos y funciones a clases inferiores, en este ejemplo CocheGas hereda de vehiculo y por eso ya contiene la funicion arrancar


class Vehiculo:
    def arrancar(self):
        return "Vehículo arrancado"


class CocheGas(Vehiculo):
    def acelerarGas(self):
        return "Acelerando Gas"


class CocheElectrico(Vehiculo):
    def acelerarElectrico(self):
        return "Acelerando Electrico"


# Hereda de Coche (que hereda de Vehiculo)
class CocheHibrido(CocheGas, CocheElectrico):
    def cargar_bateria(self):
        return "Batería cargada"


# ---------------------------Reutilizacion------------------------------
# La reutilizacion es una practica esencial en programación que permite evitar la duplicacion y mantener un codigo mas limpio y escalable
# La reutilización se puede lograr con funciones, modulos

def saludar(nombre):
    return f"Hola, {nombre}!"


print(saludar("Juan"))  # Hola, Juan!
print(saludar("Ana"))   # Hola, Ana!

# Estamos reutilizando una función, nos evita tener que repetir codigo, lo mismo pasa con los modulos


# ---------------------------Polimorfizmo------------------------------
# Es un cconcepto que permite que objetos de diferentes clases respondan de una manera distinta a un mismo metodo o funcion
class Animal:
    def hacer_sonido(self):
        return "Sonido genérico"


class Perro(Animal):
    def hacer_sonido(self):  # Sobrescritura
        return "¡Guau!"


class Gato(Animal):
    def hacer_sonido(self):  # Sobrescritura
        return "¡Miau!"


# Uso polimórfico
animales = [Perro(), Gato()]
for animal in animales:
    print(animal.hacer_sonido())

# El perro y gato tienen la misma funcion de hacer_sonido pero el resultado es diferente, se comportan diferente a la misma función


# ---------------------------Sobrecarga de operadores------------------------------
# Permite definir el comportamiento de operadores +,-,*,/ etc para objetos de clases personalizadas para hacer que el codigo sea mas intuitivo,
# Es basicamente encapsular el operador en una funcion
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):  # Sobrecarga de '+'
        return Vector(self.x + otro.x, self.y + otro.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(1, 4)
# Equivale a v1.__add__(v2),. que es la encapsulación del operador +
resultado = v1 + v2
print(resultado)      # Vector(3, 7)


# ---------------------------Sobrecarga de funciones------------------------------
# En python no existe la sobrecarga de funciones, para simular esto se pueden utilizar los parametros opcionales


if __name__ == "__main__":

    # Encapsulamiento
    cuenta = CuentaBancaria(1000)
    cuenta.depositar(500)
    print(cuenta.obtener_saldo())  # ✅ Correcto (1500)

    # ⚠️ Acceso "no recomendado" (pero posible en Python):
    # 1500 (pero rompe el encapsulamiento)
    print(cuenta._CuentaBancaria__saldo)

    # Herencia
    tesla = CocheHibrido()
    print(tesla.arrancar())       # "Vehículo arrancado" (de Vehiculo)
    print(tesla.acelerarGas())  # "Acelerando Gas"    (de CocheGas)
    # "Acelerando Electrico"    (de CocheElectrico)
    print(tesla.acelerarElectrico())
    print(tesla.cargar_bateria())  # "Batería cargada"    (nuevo método)
