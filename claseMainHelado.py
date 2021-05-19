from claseManejaSabores import ManejaSabores
from claseManejaHelados import ManejaHelados
from claseMenuHelados import MenuHelados
import os
if __name__ == '__main__':
    salir = True
    menu = MenuHelados()
    while salir:
        print("""
        ==============================================================
        1 - Registrar un helado vendido.
        2 - Mostrar los 5 sabores mas pedidos.
        3 - Calcular el total de gr de un sabor.
        4 - Mostrar todos los sabores vendidos de un tipo de Helado.
        ==============================================================
        """)
        opcion = input("\nIngrese una opcion a ejecutar: ")
        os.system('clear')
        if ((opcion != '1') and (opcion != '2') and (opcion != '3') and (opcion != '4') and (opcion != '5')):
            print("Opcion no valida\n")
            salir = False
        else:
            if (opcion == '5'):
                menu.salir()
                salir = False
            else:
                menu.opcion(opcion)