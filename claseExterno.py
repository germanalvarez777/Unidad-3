from claseEmpleado import Empleado
from claseFechaHora import FechaHora
class Externo (Empleado):
    __tarea = None
    __fechaInicio = None
    __fechaFin = None
    __viatico = 0.0
    __costoObra = 0.0
    __segurodeVida = 0.0
    def __init__ (self, nom, dni, direcc, telef, fechaIn, fechaFin,tarea='',viat=0.0, costoOb = 0.0, seguro=0.0):
        super().__init__(nom, dni, direcc, telef)
        self.__tarea = tarea.lower()
        self.__fechaInicio = fechaIn
        self.__fechaFin = fechaFin
        self.__viatico = viat
        self.__costoObra = costoOb
        self.__segurodeVida = seguro
    
    def getSueldo (self):
        #Sueldo = costo de la obra - viático- monto del seguro de vida
        return self.__costoObra - self.__viatico - self.__segurodeVida

    def getTarea (self):
        return self.__tarea
    def getViatico (self):
        return self.__viatico
    def getSeguroVida (self):
        return self.__segurodeVida
    def getCostoObra (self):
        return self.__costoObra
    
    def getFechaFinExt (self):
        return self.__fechaFin

    def mostrar (self):
        print("---Datos del Empleado---\n")
        super().mostrar()
        print("---Empleado Tipo Externo--\n")
        print("Fecha Inicio: {} - Fecha Cierre Contrato: {}\n".format(self.__fechaInicio.mostrarFecha(), self.__fechaFin.mostrarFecha()))
        print("Tarea: {}\nMonto Viatico: {:.2f} - Costo de la Obra: {:.2f}\nSeguro de Vida: {:.2f}".format(self.__tarea, self.__viatico, self.__costoObra, self.__segurodeVida))
        print("Sueldo Calculado a Cobrar: {:.2f}".format(self.getSueldo()))