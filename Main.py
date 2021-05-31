from claseMenuEmpleado import MenuEmpleado
from claseManejaEmpleados import ManejaEmpleados
import os

from zope.interface import Interface
from zope.interface import implementer
from claseIGerente import IGerente
from claseITesorero import ITesorero
@implementer(IGerente)
@implementer(ITesorero)

def test():
    print("Realizamos el testeo de datos: ")
    tamañoTeclado = int(input("Ingrese el tamaño del arreglo: "))
    me = ManejaEmpleados(tamañoTeclado, 5)
    me.testEmpleadoPlanta()
    me.testEmpleadoContratado()
    me.testEmpleadoExterno()
    me.mostrarEmpleados()

def gerente (manejadorEmp):
        #desarrollamos un mini menu de opciones para el gerente
        salida = True
        while salida:
            print("\n1 - Modificar el sueldo básico de un empleado de planta.\n2 - Modificar el valor que se paga por hora de un empleado contratado\n3- Modificar valor que se paga por viático de un empleado externo.\n")
            op = input("Ingrese una opcion: ")
            os.system('clear')
            if ((op != '1') and (op != '2') and (op != '3')):
                salida = False
                print("Salida del Menu Gerente\n")
            else:
                if op == '1':
                    manejadorEmp.mostrarDNIempleados()
                    dni = int(input("Ingrese el DNI de algun empleado de Planta: "))
                    if (dni != None):
                        monto = float(input("Ingrese nuevo sueldo basico de empleado Planta: "))
                        manejadorEmp.modificarBasicoEPlanta(dni, monto)
                    else:
                        print("DNI ingresado para empleado de planta no es valido!\n")

                elif op == '2':
                    manejadorEmp.mostrarDNIempleados()
                    dni = int(input("Ingrese el DNI de algun empleado Contratado: "))
                    if  (dni != None):
                        nuevahora = int(input("Ingrese nuevo valor x hora de Emp Contratado: "))
                        manejadorEmp.modificarValorEPorHora(dni, nuevahora)
                    else:
                        print("DNI ingresado para empleado de tipo Contratado no es valido!\n")

                elif op == '3':
                    manejadorEmp.mostrarDNIempleados()
                    dni = int(input("Ingrese el DNI de algun empleado Externo: "))
                    if (dni != None):
                        viatico = float(input("Ingrese el nuevo viatico de Externo: "))
                        manejadorEmp.modificarViaticoEExterno(dni, viatico)
                    else:
                        print("DNI ingresado para empleado de tipo Externo no es valido!\n")


def tesorero (manejadorEmp):
    manejadorEmp.mostrarDNIempleados()
    dni = int(input("Ingrese el DNI de algun empleado: "))
    if (dni != None):
        manejadorEmp.gastosSueldoPorEmpleado(dni)
    else:
        print("DNI ingresado no es valido\n")


if __name__ == '__main__':
    prueba = input("Desea realizar el testeo de datos?(s/n): ")
    if (prueba.lower() == 's'):
        test ()
        input("El testeo de datos ha finalizado, presione una tecla..")
    
    tamañoTeclado = int(input("Ingrese el tamaño del arreglo: "))
    menu = MenuEmpleado(tamañoTeclado)
    
    manejaEmp = ManejaEmpleados(tamañoTeclado, 5)
    manejaEmp.testEmpleadoPlanta()
    manejaEmp.testEmpleadoContratado()
    manejaEmp.testEmpleadoExterno()
           
    ejec = True
    while ejec:
        print("""
        ------------------------------------------------------
        1 - Ejecutar Menu de Usuario General, Ejercicio 4.
        2 - Ingresar Usuario (Gerente/Tesorero).
        ------------------------------------------------------\n
        """)
        s = input("Ingrese una opcion a ejecutar(1/2): ")
        os.system('clear')
        if (s == '1'):

            salir = True
            while salir:
                print("""
                ====================================================
                1 - Registrar Horas.
                2 - Total de Tarea.
                3 - Ayuda.
                4 - Calcular sueldo.
                5 - Salir.  
                ====================================================\n
                """)
                opcion = input("\nIngrese una opcion a ejecutar: ")
                os.system('clear')
                if ((opcion != '1') and (opcion != '2') and (opcion != '3') and (opcion != '4') and (opcion != '5')):
                    print("Opcion no valida\n")
                    salir = False
                else:
                    if (opcion == '5'):
                        menu.salir(manejaEmp)
                        salir = False
                    else:
                        menu.opcion(opcion, manejaEmp)

        elif s == '2':
            
            usuario = input("Ingrese un usuario(uGerente/uTesorero): ")
            clave = input("Ingrese la clave (ufC77#!1/ag@74ck): ")
            if ((usuario.lower() == 'ugerente') and (clave.lower() == 'ufc77#!1')):
                
                gerente(IGerente(manejaEmp))               #restrinccion a metodos de Igerente
            
            elif ((usuario.lower() == 'utesorero') and (clave.lower() == 'ag@74ck')):
                
                tesorero (ITesorero(manejaEmp))            #restrinccion a metodos de Itesorero
            else:
                print("Usuario o clave ingresada no es valida\n")

        else:
            print("Opcion seleccionada no es valida\n")
            ejec = False
        
        
