from claseManejaSabores import ManejaSabores
from claseManejaHelados import ManejaHelados
from claseMenuHelados import MenuHelados
import os

def testPrueba ():
    ms = ManejaSabores()
    ms.testListaSabores()
    mh = ManejaHelados()
    s = True
    while s:
        carg = input("Desea cargar una instancia?(s/n): ")
        if carg.lower() == 's':
            mh.unaInstanciaH(ms)
        elif carg.lower() == 'n':
            s = False
        else:
            print("Selecciono una opcion incorrecta\n")
            s = False

    mh.mostrarHelados()

if __name__ == '__main__':
    
    ejec = input("Desea ejecutar el test de prueba?(s/n): ")
    if ejec.lower() == 's':
        testPrueba()
        input("El testeo de datos ha finalizado, presione una tecla: ")

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