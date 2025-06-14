def tema(parTema):
    print(f"\n----- {parTema} -----\n")

def datos_enteros():
    tema("Enteros")
    w= 105
    x= 615161165168168
    y= -59
    z= 0b0010101
    h= 0xFF

    print(w,type(w))
    print(x,type(x))
    print(y,type(y))
    print(z,type(z))
    print(h,type(h))

def listasEjemplos():
    tema("Listas")

    lista_vacia = []

    # Lista con elementos
    frutas = ["manzana", "banana", "naranja", "kiwi"]
    numeros = [9, 25, 3, 4, 50, 60, 23,15]
    mezclada = [1, "texto", True, 3.14] 
    frutas.append("uva")        # Añade al final
    frutas.insert(1, "pera")    # Inserta en posición específica

    # Eliminar elementos
    frutas.remove("banana")     # Elimina por valor
    eliminado = frutas.pop(2)   # Elimina por índice y retorna el valor
    print(frutas.index("naranja"))

    # Longitud de la lista
    print(len(frutas))          # 5

    # Ordenar
    numeros.sort()              # Orden ascendente
    print(numeros)
    numeros.sort(reverse=True)  # Orden descendente
    print(numeros)

    ultimo_mayor_20 = next(x for x in numeros if x > 20)  # 30
    print("Ultimo mayor: ",ultimo_mayor_20)

    # Where (filtrar elementos)
    mayores_20 = [x for x in numeros if x > 20] 
    print("Mayores a 20: ",mayores_20)

    # Select (transformar elementos)
    doblados = [x*2 for x in numeros]  
    print("Duplicados: ",doblados)

    # Any (verificar si algún elemento cumple condición)
    hay_mayores_30 = any(x > 300 for x in numeros) 
    print("Cumple condicion: ",hay_mayores_30)

    # All (verificar si todos cumplen condición)
    todos_mayores_5 = all(x > 5 for x in numeros)  
    print("Cumplen todos condicion: ",todos_mayores_5)



def tuplasEjemplos():
    tema("Tuplas")
    # Tupla vacía
    tupla_vacia = ()
    # Tupla con un elemento (necesita coma al final)
    tupla_un_elemento = (42,)  # ¡La coma es importante!
    # Tupla con múltiples elementos
    coordenadas = (10, 20)
    colores = ("rojo", "verde", "azul")
    mezclada = (1, "dos", True, 3.14)

    # Sin paréntesis (empaquetado implícito)
    tupla_implicita = 4, 5, 6
    print(coordenadas[0])  # 10 (primer elemento)
    print(colores[-1])    # "azul" (último elemento)
    print(mezclada[1:3])  # ("dos", True) (slicing)
    # Longitud
    print(len(colores))  # 3

    # Concatenación
    nueva_tupla = coordenadas + (30, 40)  # (10, 20, 30, 40)

    # Repetición
    tupla_repetida = ("Hola",) * 3  # ("Hola", "Hola", "Hola")

    # Comprobar existencia
    print("rojo" in colores)  # True
    
    #Conversiones
    # Lista a tupla
    lista = [1, 2, 3]
    tupla_desde_lista = tuple(lista)  # (1, 2, 3)
    print(tupla_desde_lista)

    # Tupla a lista
    tupla = ('a', 'b', 'c')
    lista_desde_tupla = list(tupla)  # ['a', 'b', 'c']
    print(lista_desde_tupla)

def Conjuntos_Ejemplos():
    tema("Conjuntos")
    # Conjunto vacío (usamos set() porque {} crea un diccionario)
    conjunto_vacio = set()

    # Conjunto con elementos
    frutas = {"manzana", "banana", "naranja"}
    numeros = {1, 2, 3, 4, 5}

    # Crear conjunto desde una lista (elimina duplicados)
    lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
    conjunto_sin_duplicados = set(lista_con_duplicados)  # {1, 2, 3, 4, 5}
    # Añadir elementos
    frutas.add("kiwi")          # Añade un elemento
    frutas.update(["uva", "pera"])  # Añade múltiples elementos

    # Eliminar elementos
    frutas.remove("banana")     # Elimina (error si no existe)
    frutas.discard("melón")     # Elimina si existe (sin error)
    elemento = frutas.pop()     # Elimina y retorna un elemento aleatorio

    # Tamaño del conjunto
    print(len(frutas))          # Número de elementos

    # Verificar pertenencia
    print("manzana" in frutas)  # True

    # Copiar un conjunto
    copia_frutas = frutas.copy()

    # Limpiar todo el conjunto
    frutas.clear()

    # Convertir a lista
    lista_frutas = list(frutas)

    # Eliminar duplicados de una lista
    lista = [1, 2, 2, 3, 4, 4, 5]
    lista_unica = list(set(lista))  # [1, 2, 3, 4, 5] (el orden puede variar)

    # Encontrar elementos comunes entre listas
    lista1 = [1, 2, 3, 4]
    lista2 = [3, 4, 5, 6]
    comunes = set(lista1) & set(lista2)  # {3, 4}
    print(comunes)

    # Contar vocales únicas en un texto
    texto = "programación en Python"
    vocales = {c for c in texto.lower() if c in 'aeiou'}  # {'a', 'e', 'i', 'o', 'ó'}
    print (vocales)

def Diccionarios_Ejemplos():
    tema("Diccionarios")
    # Diccionario vacío
    dic_vacio = {}
    dic_vacio_alt = dict()

    # Diccionario con elementos
    estudiante = {
        "nombre": "María",
        "edad": 22,
        "carrera": "Ingeniería"
    }

    # Usando constructor dict()
    otro_dic = dict(nombre="Juan", edad=25)  # {'nombre': 'Juan', 'edad': 25}

    # Desde lista de tuplas
    pares = [("a", 1), ("b", 2)]
    dic_desde_tupla = dict(pares)  # {'a': 1, 'b': 2}

    print(estudiante["nombre"])  # "María" (error si no existe)
    print(estudiante.get("edad"))  # 22 (retorna None si no existe)
    print(estudiante.get("nota", 0))  # 0 (valor por defecto si no existe)

    # Añadir/modificar elementos
    estudiante["nota"] = 8.5  # Añade nueva clave
    estudiante["edad"] = 23   # Modifica valor existente

    # Eliminar elementos
    del estudiante["carrera"]  # Elimina clave-valor
    valor = estudiante.pop("edad")  # Elimina y retorna el valor
    estudiante.clear()  # Vacía el diccionario

    # Verificar existencia
    print("nombre" in estudiante)  # True

    # Tamaño del diccionario
    print(len(estudiante))  # Número de pares clave-valor

    # Obtener todas las claves
    claves = estudiante.keys()  # dict_keys(['nombre', 'edad'])

    # Obtener todos los valores
    valores = estudiante.values()  # dict_values(['María', 22])

    # Obtener pares clave-valor
    items = estudiante.items()  # dict_items([('nombre', 'María'), ('edad', 22)])

    # Copiar diccionario
    copia = estudiante.copy()

    # Por claves
    for clave in estudiante:
        print(clave, estudiante[clave])

    # Por items (clave-valor)
    for clave, valor in estudiante.items():
        print(f"{clave}: {valor}")

    universidad = {
        "estudiantes": {
            "001": {"nombre": "Ana", "edad": 20},
            "002": {"nombre": "Luis", "edad": 22}
        },
        "cursos": ["Matemáticas", "Programación"]
    }

    # Acceso a elementos anidados
    print(universidad["estudiantes"]["001"]["nombre"])  # "Ana"

def Cadenas_Ejemplos():
    tema("Cadenas")

    # Comillas simples
    cad1 = 'Hola mundo'

    # Comillas dobles
    cad2 = "Python es genial"

    # Comillas triples (multilínea)
    cad3 = """Esto es
    una cadena
    multilínea"""

    # Caracteres especiales
    cad4 = "Línea 1\nLínea 2\tTabulación"

    # Concatenación
    saludo = "Hola" + " " + "Python"  # "Hola Python"

    # Repetición
    risas = "ja" * 3  # "jajaja"

    # Longitud
    longitud = len("Python")  # 6

    # Acceso a caracteres
    lenguaje = "Python"
    primer_caracter = lenguaje[0]  # 'P'
    ultimo_caracter = lenguaje[-1]  # 'n'

    # Mayúsculas/minúsculas
    texto = "Python"
    print(texto.upper())  # "PYTHON"
    print(texto.lower())  # "python"
    print(texto.capitalize())  # "Python"

    # Búsqueda
    frase = "Aprendiendo Python"
    print(frase.find("Python"))  # 12 (posición)
    print("Python" in frase)  # True

    # Reemplazo
    nueva_frase = frase.replace("Python", "programación")  # "Aprendiendo programación"

    # División y unión
    palabras = "Python,Java,C++".split(",")  # ['Python', 'Java', 'C++']
    unido = "-".join(palabras)  # "Python-Java-C++"

    # Eliminar espacios
    cadena = "  hola  "
    print(cadena.strip())  # "hola"
    print(cadena.lstrip())  # "hola  "
    print(cadena.rstrip())  # "  hola"

    cad = "Python3"

    print(cad.isalpha())  # False (contiene número)
    print(cad.isalnum())  # True
    print(cad.isdigit())  # False
    print(cad.startswith("Py"))  # True
    print(cad.endswith("3"))  # True

#--------------Llamadas a funciones----------------
#datos_enteros()
#listasEjemplos()
#tuplasEjemplos()
#Conjuntos_Ejemplos()
#Diccionarios_Ejemplos()