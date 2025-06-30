import numpy as np


# Muestra la información de un array de numpy
def InfoArray(parArray):
    try:
        if not isinstance(parArray, np.ndarray):  # ndarray es la clase de np.array
            print("No es un array de numpy")
            return

        maximo = np.max(parArray)
        maximoColumna = np.max(parArray, axis=0)
        maximoFila = np.max(parArray, axis=1)
        print("Valor máximo de la matriz: ", maximo)
        print("Valor máximo por columna: ", maximoColumna)
        print("Valor máximo por fila: ", maximoFila)

        minimo = np.min(parArray)
        minimoColumna = np.min(parArray, axis=0)
        minimoFila = np.min(parArray, axis=1)
        print("Valor minimo de la matriz: ", minimo)
        print("Valor minimo por columna: ", minimoColumna)
        print("Valor minimo por fila: ", minimoFila)
    except Exception as e:
        print(f"Error inesperado: {type(e).__name__}: {e}")


# Muestra informacion de un array con info deportiva
def InfoArrayDepo(parArray):
    try:
        if not isinstance(parArray, np.ndarray):  # ndarray es la clase de np.array
            print("No es un array de numpy")
            return

        maximo = np.max(parArray)
        minimo = np.max(parArray, axis=0)
        promedio = np.mean(parArray)
        mediana = np.median(parArray)
        varianza = np.var(parArray)
        desviacionEst = np.std(parArray)
        print("Valor máximo de la matriz: ", maximo)
        print("Valor minimo de la matriz: ", minimo)
        print("Valor promedio de la matriz: ", promedio)
        print("Valor mediana de la matriz: ", mediana)
        print("Valor varianza de la matriz: ", varianza)
        print("Valor desviación estandar de la matriz: ", desviacionEst)

    except Exception as e:
        print(f"Error inesperado: {type(e).__name__}: {e}")


def InfoArray3(parArray1, parArray2):
    try:
        # ndarray es la clase de np.array
        if not isinstance(parArray1, np.ndarray) or not isinstance(parArray2, np.ndarray):
            print("No es un array de numpy")
            return

        # Primero, terccero y ultimo de cada elemento
        arrayResult = np.array([
            parArray1[0],  # 1
            parArray1[2],  # 3
            parArray1[-1],  # ultimo
            parArray2[0],  # 1
            parArray2[2],  # 3
            parArray2[-1]  # ultimo
        ])
        arrayInvertido = arrayResult[::-1]
        print("Array coon los 3 elementos de cada arreglo:", arrayResult)
        print("Array invertido:", arrayInvertido)

        # Toma los elementos 20 de cada arreglo y sumalos, muestra el resultado
        res = parArray1[19] + parArray2[19]
        print("Suma de los dos elementos 20:", res)

    except Exception as e:
        print(f"Error inesperado: {type(e).__name__}: {e}")


# Accede a los numeros 5,9,3,21
def InfoArray4(parArray1):
    try:
        if not isinstance(parArray1, np.ndarray):  # ndarray es la clase de np.array
            print("No es un array de numpy")
            return

        a = matrizE[0, 2]  # 5
        b = matrizE[1, 3]  # 9
        c = matrizE[2, 1]  # 3
        d = matrizE[3, 2]  # 21

        print(a, b, c, d)

    except Exception as e:
        print(f"Error inesperado: {type(e).__name__}: {e}")


# Obten los indices del 2 al 6
def InfoArray5(parArray1):
    try:
        if not isinstance(parArray1, np.ndarray):  # ndarray es la clase de np.array
            print("No es un array de numpy")
            return

        elementos = matrizF[2:7]  # Obten los indices del 2 al 6
        print(elementos)

    except Exception as e:
        print(f"Error inesperado: {type(e).__name__}: {e}")


matriz = np.array(np.random.randint(-1000, 1000, 50)).reshape(10, 5)
InfoArray(matriz)

matrizDepo = np.array([-57, 65, 32, 89, 54])
InfoArrayDepo(matrizDepo)

matriz1 = np.array([65, 32, 98, 59])
matriz2 = np.array([98, 32, 54, 87, 65, 35, 68, 15, 46, 29])
InfoArray3(matriz1, matriz2)

matrizE = np.array([[1, 1, 5, 1], [1, 1, 1, 9], [1, 3, 1, 1], [1, 1, 21, 1]])
InfoArray4(matrizE)

matrizF = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
InfoArray5(matrizF)
