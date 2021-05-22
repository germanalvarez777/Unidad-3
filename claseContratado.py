from claseEmpleado import Empleado
from claseFechaHora import FechaHora
class Contratado (Empleado):
    valorXhora = 500                       #variable de clase
    __fechaInicio = None
    __fechaFin = None
    __cantHorastrab = 0
    def __init__ (self, nom, dni, direcc, telef, fechaIn, fechaFin, cantHoras=0):
        super().__init__(nom, dni, direcc, telef)
        self.__fechaInicio = fechaIn
        self.__fechaFin = fechaFin
        self.__cantHorastrab = cantHoras
    
    @classmethod
    def getValorXhora (cls):
        return cls.valorXhora
    
    def getcantHorasCont (self):
        return self.__cantHorastrab
    
    def setCantHoras (self, horas):
        self.__cantHorastrab += horas

    def getFechaIniCont (self):
        return self.__fechaInicio
    def getFechaFinCont (self):
        return self.__fechaFin
    
    def getSueldo (self):
        #Sueldo = cantidad de horas trabajadas * valor de la hora
        return self.__cantHorastrab * Contratado.getValorXhora()

    def mostrar (self):
        print("---Datos del Empleado---\n")
        super().mostrar()
        print("---Empleado Tipo Contratado---\n")
        print("Fecha Inicio Contrato: {} - Fecha Fin Contrato: {}\nCantidad de Horas: {}\nValor por Hora: {}".format(self.__fechaInicio.mostrarFecha(), self.__fechaFin.mostrarFecha(), self.__cantHorastrab, Contratado.getValorXhora()))
        print("Sueldo Calculado a Cobrar: {:.2f}".format(self.getSueldo()))
