import pickle
import os

ruta_archivo = "./Archivos/archivoSerial.bin"

# Crear carpeta si no existe
if not os.path.exists(os.path.dirname(ruta_archivo)):
    os.makedirs(os.path.dirname(ruta_archivo))


lista=[5,6,3,7]
with open(ruta_archivo,"wb") as binFile:
    pickle.dump(lista,binFile)
print("Archivo binario escrito")

with open(ruta_archivo,"rb")  as file:
   lista = pickle.load(file)
   print(lista)
print("Archivo binario deserealizado")