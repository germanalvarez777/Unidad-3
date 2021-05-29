from claseManejaEmpleados import ManejaEmpleados
from datetime import date
from claseFechaHora import FechaHora 

from zope.interface import Interface
from zope.interface import implementer
from claseIGerente import IGerente
from claseITesorero import ITesorero
@implementer(IGerente)
@implementer(ITesorero)

class MenuEmpleado:
    __switcher = None
    __Mempleados = None
    def __init__ (self, tamañoTeclado):
        self.__switcher = {
         '1':self.opcion1,
         '2':self.opcion2,
         '3':self.opcion3,
         '4':self.opcion4,
         '5':self.opcion5,
         '6':self.salir
        }
        self.__Mempleados = ManejaEmpleados(tamañoTeclado,5)
        self.__Mempleados.testEmpleadoPlanta()
        self.__Mempleados.testEmpleadoContratado()
        self.__Mempleados.testEmpleadoExterno()

    def opcion (self, op):
        func = self.__switcher.get (op, lambda:print("Opcion no valida"))
        func()
    
    def salir (self):
        print("Salida del programa")
    
    def opcion1 (self):
        print("Ha seleccionado la Opcion 1\nRegistrar horas de un empleado de Tipo Contratado\n")
        doc = int(input("Ingrese el DNI de un empleado: "))
        horas = int(input("Ingrese la cantidad de horas trabajadas por hoy:"))
        if (doc != None and horas != None):
            self.__Mempleados.incrementarHoras (doc, horas)
        else:
            print("Los datos ingresados no son validos\n")

    def opcion2 (self):
        print("Ha seleccionado la Opcion 2\nMostrar el monto a pagar de una tarea de Tipo Externo\n")
        tarea = input("Ingrese una tarea especifica a mostrar(Carpinteria-Electricidad-Plomeria):\n")
        dateHoy = str(date.today())
        print("La fecha actual es: ", dateHoy)
        i = dateHoy.find('-')                   #metodo find para buscar la posicion donde se encuentra la cadena o char def por param
        j = dateHoy.rfind('-')
        if i != None and j != None:
            anio = int(dateHoy[:i])
            mes = int(dateHoy[i+1:j])
            dia = int(dateHoy[j+1:])
            #print("1-dia:{} , mes: {}, anio: {}".format(dia, mes, anio))
            fActual = FechaHora (dia,mes,anio)
            fActual.validar()
        
        self.__Mempleados.mostrarTotalExterno(tarea, fActual)

    def opcion3 (self):
        print("Ha seleccionado la Opcion 3\nAyuda solidaria a empleados con sueldo inferior a $25000\n")
        #presupAyuda = float(input("Ingrese el presupuesto de ayuda: "))
        self.__Mempleados.ayudaEmpleados ()

    def opcion4 (self):
        print("Ha seleccionado la Opcion 4\nCalcular sueldo a cobrar de los empleados\n")
        self.__Mempleados.mostrarEmpleados()

    def gerente (self, manejadorEmp):
        manejadorEmp.mostrarDNIempleados()
        dni = int(input("Ingrese el DNI de algun empleado: "))
        if (dni != None):
            #desarrollamos un mini menu de opciones para el gerente
            salida = True
            while salida:
                print("1 - Modificar el sueldo básico de un empleado de planta.\n2 - Modificar el valor que se paga por hora de un empleado contratado\n3- Modificar valor que se paga por viático de un empleado externo.\n")
                op = input("Ingrese una opcion: ")
                if ((op != '1') and (op != '2') and (op != '3')):
                    salida = False
                    print("Salida del Menu Gerente\n")
                else:
                    if op == '1':
                        monto = float(input("Ingrese nuevo sueldo basico de empleado Planta: "))
                        manejadorEmp.modificarBasicoEPlanta(dni, monto)
                    elif op == '2':
                        nuevahora = int(input("Ingrese nuevo valor x hora de Emp Contratado: "))
                        manejadorEmp.modificarValorEPorHora(dni, nuevahora)
                    elif op == '3':
                        viatico = float(input("Ingrese el nuevo viatico de Externo: "))
                        manejadorEmp.modificarViaticoEExterno(dni, viatico)

        else:
            print("DNI ingresado no es valido\n")

    def tesorero (self, manejadorEmp):
        manejadorEmp.mostrarDNIempleados()
        dni = int(input("Ingrese el DNI de algun empleado: "))
        if (dni != None):
            manejadorEmp.gastosSueldoPorEmpleado(dni)
        else:
            print("DNI ingresado no es valido\n")

    def opcion5 (self):
        print("Ejecutamos la Opcion 5\nSeleccionar Usuario\n")
        usuario = input("Ingrese un usuario(uGerente/uTesorero): ")
        clave = input("Ingrese la clave (ufC77#!1/ag@74ck): ")
        if ((usuario.lower() == 'ugerente') and (clave.lower() == 'ufc77#!1')):
            self.gerente(IGerente(self.__Mempleados))               #restrinccion a metodos de Igerente
        elif ((usuario.lower() == 'utesorero') and (clave.lower() == 'ag@74ck')):
            self.tesorero (ITesorero(self.__Mempleados))            #restrinccion a metodos de Itesorero
        else:
            print("Usuario o clave ingresada no es valida\n")

