import abc
from abc import ABC
class Personal (ABC):
    __cuil = None
    __apellido = None
    __nombre = None
    __sueldoBasico = 0
    __antig = 0
    
    #atributos de docente y despues de investigador
    def __init__ (self, nombre, apellido, cuil, sueldoBasico, antig,carrera='', cargo='', catedra='', areaInv='', tipoInv=''):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cuil = cuil
        self.__sueldoBasico = sueldoBasico
        self.__antig = antig
    
    def getNomApell (self):
        return self.__nombre + ' '+ self.__apellido
    
    def getNombre (self):
        return self.__nombre
    def getApellido (self):
        return self.__apellido

    def getCuil (self):
        return self.__cuil
    
    def getSueldoBasico (self):
        return self.__sueldoBasico
    def getAntig (self):
        return self.__antig

    def mostrarDatos (self):
        print("----Datos del Personal Universitario----\n")
        print("Nombre: {}\nCUIL: {}\nSueldo Basico: {:.2f} - Antiguedad: {} años".format(self.getNomApell(), self.__cuil, self.__sueldoBasico, self.__antig))
    
    #metodo para ordenar por nombre, apartado 4
    def __gt__ (self, otroP):
        if (type(self) == type(otroP)):
            return self.__nombre > otroP.getNombre()

    @abc.abstractmethod
    def calcularSueldo (self):
        pass    

    def toJSON (self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict (
                nombre = self.__nombre,
                apellido = self.__apellido,
                cuil = self.__cuil,
                sueldoBasico = self.__sueldoBasico,
                antig = self.__antig
            )
        )
        return d