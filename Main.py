from claseMenuEmpleado import MenuEmpleado
from claseManejaEmpleados import ManejaEmpleados
import os
def test():
    print("Realizamos el testeo de datos: ")
    tamañoTeclado = int(input("Ingrese el tamaño del arreglo: "))
    me = ManejaEmpleados(tamañoTeclado, 5)
    me.testEmpleadoPlanta()
    me.testEmpleadoContratado()
    me.testEmpleadoExterno()
    me.mostrarEmpleados()

if __name__ == '__main__':
    prueba = input("Desea realizar el testeo de datos?(s/n): ")
    if (prueba.lower() == 's'):
        test ()
    
    salir = True
    tamañoTeclado = int(input("Ingrese el tamaño del arreglo: "))
    menu = MenuEmpleado(tamañoTeclado)
    while salir:
        print("""
        1 - Registrar Horas.
        2 - Total de Tarea.
        3 - Ayuda.
        4 - Calcular sueldo.
        5 - Salir.  
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