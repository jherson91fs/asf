import time

from utils import limpiarPantalla
from models import Producto
#from editar import editarDato, buscarProducto

ruta_archivo = "./archivos/producto.txt"


def crearProducto():
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    detalle = input("Detalle: ")
    tipo = input("Tipo: ")
    precio = input("Precio: ")

    producto = Producto(codigo, nombre, detalle, tipo, precio)

    archivoProducto = open(ruta_archivo, "a")
    archivoProducto.write(str(producto))
    archivoProducto.close()

def buscarProducto(codigo):
    archivoProducto = open(ruta_archivo, "r")
    for linea in archivoProducto.readlines():
        atributos = linea.split(";")
        
        if atributos[0] == codigo:
            atributos = atributos(atributos[0], atributos[1], atributos[2], atributos[3], atributos[4])
            break
    archivoProducto.close()



    
def imprimirRegistro(ruta):
    archivoProducto = open(ruta_archivo, "r")
    print("código\tNombre\t\tDetalle\t\tTipo\tPrecio")
    for linea in archivoProducto.readlines():
        atributo = linea.split(";")
        print(
            "{}\t{}\t{}\t\t{}\t{}".format(
                atributo[0], atributo[1], atributo[2], atributo[3], atributo[4],
            )
        )
    archivoProducto.close()

def gestionProducto():
    limpiarPantalla()
    while True:
        print("                                 ")
        print("|===============================|")
        print("|      GESTION DE PRODUCTOS     |")
        print("|===============================|")
        print("| 1. Ingresar Producto Nuevo    |")
        print("| 2. Mostrar Productos          |")
        print("| 3. Busca Producto             |")
        print("| 4. Editar Producto            |")
        print("| 5. Volver al menú principal   |")
        print("|_______________________________|")
        print("                                 ")
        op = int(input("Opción: "))

        match (op):
            case 1:
                limpiarPantalla()
                crearProducto()
                print("Creado Correctamente!!!")
            case 2:
                limpiarPantalla()
                archivoProducto = open(ruta_archivo, "r")
                print("==============================================================")
                print("|Código\t|Nombre\t\t|Detalle\t\t|Tipo\t\t|Precio")
                for linea in archivoProducto.readlines():
                    atributos = linea.split(";")
                    print("----------------------------------------------------------------")
                    print(
                        "|{}|\t|{}\t\t|{}\t\t|{}\t\t|{}".format(
                            atributos[0], atributos[1], atributos[2], atributos[3], atributos[4]
                        )
                    )
                archivoProducto.close()

            case 3:
                limpiarPantalla()
                codigo = input("Ingrese código del producto: ")
                fila = str(buscarProducto(codigo))
                if buscarProducto(codigo):

                    print(atributos)
                else:
                    print("Codigo no existente")
                
                

            case 4:
                limpiarPantalla()
                #editarDato(ruta, filas, columna, nuevo_dato)

            case 5:
                limpiarPantalla()
                print("Regresando...")
                time.sleep(2)
                limpiarPantalla()
                break
            case _:
                print("opción incorrecta")
                time.sleep(2)
                limpiarPantalla()
