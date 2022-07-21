import time

from models import Usuario
from utils import limpiarPantalla

ruta_archivo = "./archivos/usuarios.txt"


def crearUsuario():

    dni = input("DNI: ")
    password = input("Password: ")
    tipo = input("Tipo: ")
    nombres_apellidos = input("Nombres y Apellidos: ")
    direccion = input("Dirección: ")
    telefono = input("Telefono: ")
    email = input("E-mail: ")

    usuario = Usuario(
        dni, password, tipo, nombres_apellidos, direccion, telefono, email
    )

    archivoUsuario = open(ruta_archivo, "a")
    archivoUsuario.write(str(usuario))
    archivoUsuario.close


def BuscarUsuario(dni):
    archivoUsuarios = open(ruta_archivo, "r")
    for linea in archivoUsuarios.readlines():
        atributo = linea.split(";")

        if atributo[0] == dni:
            return True
    return False


def Acceso(dni, password):
    archivoUsuarios = open(ruta_archivo, "r")
    for linea in archivoUsuarios.readlines():
        linea = linea.split(";")
        if linea[0] == dni and linea[1] == password and linea[2] == "ADMIN":
            return True
        else:
            return False


def gestionUsuarios():
    while True:
        print("                                 ")
        print("|===============================|")
        print("|     GESTION DE USUARIOS       |")
        print("|===============================|")
        print("| 1. Crear nuevo usuario        |")
        print("| 2. Mostrar usuarios           |")
        print("| 3. Buscar usuario por DNI     |")
        print("| 4. regresar al menu principal |")
        print("|===============================|")
        print("                                 ")
        op = input("Ingrese una opcion: ")

        match (op):
            case "1":
                limpiarPantalla()
                crearUsuario()
            case "2":
                limpiarPantalla()
                archivoUsuarios = open(ruta_archivo, "r")
                print("==========================================================================================================================================")
                print("|DNI\t\t|Password\t|Tipo\t\t|Nombre y Apell.\t\t|Dirección\t\t|Telefono\t|E-mail")
                for linea in archivoUsuarios.readlines():
                    atributos = linea.split(";")
                    print("-------------------------------------------------------------------------------------------------------------------------------------------")
                    print(
                        "|{}\t|{}\t\t|{}\t|{}\t\t|{}\t|{}\t|{}".format(
                            atributos[0], atributos[1], atributos[2], atributos[3], atributos[4], atributos[5], atributos[6]
                        )
                    )

                archivoUsuarios.close()
            case "3":
                limpiarPantalla()
                print("buscar por DNI")
                dni = input("Ingrese DNI: ")
                if BuscarUsuario(dni):
                    print("Existe")
                else:
                    print("No existe")

            case "4":
                limpiarPantalla()
                print("Regresando ...")
                time.sleep(2)
                limpiarPantalla()
                break
            case _:
                print("opcion no disponible")
