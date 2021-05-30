from claseManejaEmpleados import ManejaEmpleados
from datetime import date
from claseFechaHora import FechaHora 

class MenuEmpleado:
    __switcher = None
    def __init__ (self, tamañoTeclado):
        self.__switcher = {
         '1':self.opcion1,
         '2':self.opcion2,
         '3':self.opcion3,
         '4':self.opcion4,
         '5':self.salir
        }

    def opcion (self, op, manejaEmp):
        func = self.__switcher.get (op, lambda:print("Opcion no valida"))
        func(manejaEmp)
    
    def salir (self, manejaEmp):
        print("Salida del programa")
    
    def opcion1 (self, manejaEmp):
        print("Ha seleccionado la Opcion 1\nRegistrar horas de un empleado de Tipo Contratado\n")
        doc = int(input("Ingrese el DNI de un empleado: "))
        horas = int(input("Ingrese la cantidad de horas trabajadas por hoy:"))
        if (doc != None and horas != None):
            manejaEmp.incrementarHoras (doc, horas)
        else:
            print("Los datos ingresados no son validos\n")

    def opcion2 (self, manejaEmp):
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
        
        manejaEmp.mostrarTotalExterno(tarea, fActual)

    def opcion3 (self, manejaEmp):
        print("Ha seleccionado la Opcion 3\nAyuda solidaria a empleados con sueldo inferior a $25000\n")
        #presupAyuda = float(input("Ingrese el presupuesto de ayuda: "))
        manejaEmp.ayudaEmpleados ()

    def opcion4 (self, manejaEmp):
        print("Ha seleccionado la Opcion 4\nCalcular sueldo a cobrar de los empleados\n")
        manejaEmp.mostrarEmpleados()


