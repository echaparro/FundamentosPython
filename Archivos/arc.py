ruta_archivo = "./Archivos/ArchivoTest.txt"

file = open(ruta_archivo,"w")
file.write("Test escritura"+ "\n")
file.close()

lista=["Fresa","Mango", "Melon"]

with open(ruta_archivo,"a") as file:
    for item in lista:
        file.write(item+ "\n")
print("lista escrita en el archivo")

lista2=["A","B", "C"]
with open(ruta_archivo,"a") as file:
    file.writelines(lista2)

print("lista escrita en el archivo 2")

print("------Lectura--------------")
#Este bloque lee un archivo
with open(ruta_archivo,"r") as file:
    print(file.read())

print("--------------------")

with open(ruta_archivo,"r") as file:
    print(file.readline())  
    print(file.readline())  
    print(file.readline(1))  

print("--------Almacenar contenido en una lista------------")
with open(ruta_archivo,"r") as file:
   contenido= file.readlines()
   print(contenido) 
   print(contenido[-1]) #Imprime el ultimo elemento