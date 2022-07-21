
import getpass
import time

from utils import limpiarPantalla
from productos import gestionProducto
from usuarios import gestionUsuarios, Acceso


def run():
    while True:
        print("\033[91m" + "   LICORERIA MAESTRO ROSHI    " + "\033[91m")
        print("\033[0m")
        print("                             ")
        print("|===========================|")
        print("|     MENÚ PRINCIPAL        |")
        print("|===========================|")
        print("|1. Gestión de Productos    |")
        print("|2. Gestión de Usuarios     |")
        print("|3. Gestión de Ventas       |")
        print("|0. Salir                   |")
        print("|===========================|")
        print("                             ")
        op = int(input("Opción: "))

        match (op):
            case 1:
                limpiarPantalla()
                gestionProducto()

            case 2:
                limpiarPantalla()
                gestionUsuarios()

            case 3:
                limpiarPantalla()
                pass
                
            case 0:
                limpiarPantalla()
                print("Saliendo del sistema... hasta pronto")
                break

            case _:
                print("opción incorrecta")
                time.sleep(2)
                limpiarPantalla()


def main():
    acumulador = 0
    while True and acumulador != 3:

        user = input("Ingrese Usuario: ")
        passwd = getpass.getpass("Ingrese password: ")

        if Acceso(user, passwd):
            limpiarPantalla()
            run()
        else: 
            print("Usuario sin Permiso")
            acumulador += 1
            time.sleep(2)
            limpiarPantalla()
            

main()
