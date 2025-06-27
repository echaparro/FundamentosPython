import numpy as np


def InspectArray(parArray):
    if not isinstance(parArray, np.ndarray):  # ndarray es la clase de np.array
        print("No es un array de numpy")
        return

    print("Shape: ", parArray.shape)
    print("Size: ", parArray.size)
    print("NDim: ", parArray.ndim)
    print("NBytes: ", parArray.nbytes)
    print("DType: ", parArray.dtype)


array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

InspectArray([1, 2, 3, 4])  # No es un array de nuympy
InspectArray(array)  # Si se inicializo como array de numpy


# Crear Arreglos

arreglo1 = np.array([1, 2, 3])
tupla = (4, 5, 6)
arreglo2 = np.array(tupla)  # Se convierte a arreglo la tupla
arreglo3 = np.array(range(1, 11))
arreglo4 = np.array(range(10, 50, 3))
arreglo5 = np.array(range(200, 50, -5))
arreglo6 = np.array(100)

print(arreglo1)
print("-------------")
print(arreglo2)
print("-------------")
print(arreglo3)
print("-------------")
print(arreglo4)
print("-------------")
print(arreglo5)
print("-------------")
print(arreglo6)
print("-------------")

# np.ones() permite crear un arreglo lleno con el numero 1

A = np.ones(10)
B = np.ones((4, 4))
C = np.ones((3, 2), dtype=float)

print(A)
print("-----------------")
print(B)
print("-----------------")
print(C)
print("-----------------")

A = np.zeros(10)
B = np.zeros((4, 4))
C = np.zeros((3, 2))

print(A)
print("-----------------")
print(B)
print("-----------------")
print(C)
print("-----------------")


# LLenado de unamatris con un valor definido
A = np.full(shape=(10), fill_value=5, dtype=float)
B = np.full(shape=(4, 4), fill_value=-5, dtype=float)
C = np.full(shape=(3, 3), fill_value=3, dtype=int)
D = np.full(shape=(10, 10), fill_value=50, dtype=int)

print(A)
print("-----------------")
print(B)
print("-----------------")
print(C)
print("-----------------")
print(D)
print("-----------------")


# np.nan setea un valor que no es un numero(como null) np.innan(verifica si no es un numero)
K = np.array([
    [np.nan, 1, 10, 0],
    [np.nan, np.nan, np.nan, np.nan],
    [100, 50, np.nan, -25],
    [30, np.nan, np.nan, np.nan]])

print(np.isnan(K))
print(f'Hay {np.isnan(K).sum()} datos perdidos en K.')


# linspace retorna un arreglo del rando que le das y separado por el numero que le solicitas ej del 1 - 21 de 5 en 5
A = np.linspace(1, 21, 5)
print(A)


# El reshape cambia la forma del arreglo, en lugar de ser 1X10  lo cambia a 5X2
A = np.logspace(1, 51, 10)
B = A.reshape(5, 2)
print(A)
print(B)

# Diag crea una diagonal con los en rango de datos que le indiquemos
a = np.diag(range(1, 11, 2))
b = np.diag(range(5, 31, 5), 4)  # Traslada la diagonal 4 columnas
c = np.diag(range(5, 31, 5), -1)  # Traslada la diagonal 1 fila
print(a)
print("--------------")
print(b)
print("--------------")
print(c)

# Crean una matris identity
eye = np.eye(5)
identity = np.identity(5)
print(eye)
print(identity)

# array.sum() suma todos los elementos del arreglo
array1 = np.arange(1, 11)
array2 = np.linspace(1, 50, 10)
array3 = np.array(range(51))
array4 = np.logspace(1, 10, 5)
array5 = np.diag(range(5, 31, 5))
arrays = [array1, array2, array3, array4, array5]

for e in arrays:
    print(e)
    print("---------------")

for index, array in enumerate(arrays, start=1):
    print(f"Suma de los elementos del arreglo{index}: ", array.sum())

# Random con numpy, suma total, por columna y por linea

matriz = np.array(np.random.randint(1, 100, 15)).reshape(5, 3)
print(matriz)
print("Suma total de la matriz:", matriz.sum())
print("Suma  de las lineas:", matriz.sum(axis=1))
print("Suma de las columnas:", matriz.sum(axis=0))

#Maximos y minimos en un arreglo
array1 = np.array([-1, 10, 3, 4, 7, 27])
array2 = np.random.randint(-100, 300, 30)
array3 = np.random.randn(10)
array4 = np.array(range(50, 10, -2))
arrays = [array1, array2, array3, array4]

for index, array in enumerate(arrays, start = 1):
  print(f"Arreglo {index}")
  print(f"Valor máximo: ", array.max(), "indice", array.argmax())
  print(f"Valor mínimo: ", array.min(), "indice", array.argmin())
  print()