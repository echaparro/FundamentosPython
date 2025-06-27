# Estructura basica de un try exception
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("División por cero!")


"""
# Excepciones mas comunes
ZeroDivisionError	División por cero
TypeError	        Operación con tipo incorrecto
ValueError	        Valor inapropiado (ej. int("a"))
FileNotFoundError	Archivo no encontrado
IndexError	        Índice fuera de rango
KeyError	        Clave no existe en diccionario
AttributeError	    Atributo no encontrado en objeto
"""

# Manejo multiple de excepciones
try:
    num = int(input("Ingrese un número: "))
    print(10 / num)
except ValueError:
    print("Debe ingresar un número válido")
except ZeroDivisionError:
    print("No puede dividir por cero")
except Exception as e:  # Captura cualquier otro error
    print(f"Error inesperado: {type(e).__name__}: {e}")


# Finally  siempre se ejecuta para liberar recursos Nota, el finally tambien puede tronar

"""try:
    archivo = open("datos.txt", "r")
except FileNotFoundError:
    print("Archivo no encontrado")
else:
    contenido = archivo.read()
    print(contenido)
finally:
    archivo.close()
"""

# Raise error  es como el throw exception en c#   raise ValueError("Error a lanzar")


def calcular_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    return f"Tienes {edad} años"


try:
    print(calcular_edad(-5))
except ValueError as e:
    print(e)


# Se pueden personalisar las excepciones

class MiErrorPersonalizado(Exception):  # Hereda de Exception
    pass


try:
    raise MiErrorPersonalizado("¡Algo salió mal!")
except MiErrorPersonalizado as e:
    print(f"Error personalizado: {e}")
