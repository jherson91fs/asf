
from models import Producto
#from productos import BuscarProducto

ruta_archivo ="./archivos/producto.txt"

#def buscarProducto(codigo):
    #archivoProducto = open(ruta_archivo, "r")
    #for linea in archivoProducto.readlines():
        #atributos = linea.split(";")
        
        #if atributos[0] == codigo:
            #atributos = atributos(atributos[0], atributos[1], atributos[2], atributos[3], atributos[4])
        #if atributos[0] == codigo:
        #    producto = producto(atributos[0], atributos[1], atributos[2], atributos[3], atributos[4])
    
            break
    archivoProducto.close()

def editarDato(ruta, filas, columna, nuevo_dato):
    contenido = list()
    with open(ruta, "r+") as archivo:
        contenido = archivo.readlines()
        for fila in filas:
            columnas = contenido[fila - 1].split(";")
            columnas[columna] = nuevo_dato
            contenido[fila - 1] = ";".join(columnas) + "\n"
    with open(ruta, "w") as archivo:
        archivo.writelines(contenido)


#imprimirRegistro(ruta_archivo)

print("_"*20)

codigo = input("Codigo: ")
fila = (buscarProducto(codigo))
print(f"{fila}")

print("_"*20)
output = fila.split(";")

print("_"*20)
print(output)

nPrecio = input("Ingrese nuevo precio: ")

nFila = int(input("ingrese fila de registro: "))

etiqueta = int(input("que columna quieres cambiar: "))

nFila = list(map(int, str(nFila)))

print(type[nFila])

editarDato(ruta_archivo, nFila, 6, nPrecio)


#imprimirRegistro(ruta_archivo)
