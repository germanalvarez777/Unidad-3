import abc
from abc import ABC
class Vehiculo (ABC):
    __modelo = None
    __cantPuertas = 0
    __color = None
    __precioBaseV = 0.0
    
    def __init__ (self, modelo='', cantPuertas=0, color='', precioBaseV=0.0):
        self.__modelo = modelo
        self.__cantPuertas = cantPuertas
        self.__color = color
        self.__precioBaseV = precioBaseV
        
    def getModelo (self):
        return self.__modelo
    def getCantPuertas (self):
        return self.__cantPuertas
    def getColor (self):
        return self.__color
    def getPrecioBase (self):
        return self.__precioBaseV

    def setPrecioBase (self, monto):
        self.__precioBaseV = monto
        print("El nuevo Precio de Base es; {}".format(self.__precioBaseV))

    def mostrarVehiculo (self):             #metodo de ligadura dinamica
        print("Modelo: {}\nCantidad de Puertas: {} - Color: {}\nPrecio Base de Venta: {:.2f}".format(self.__modelo, self.__cantPuertas, self.__color, self.__precioBaseV))
        #return 'Modelo:'+self.__modelo + '\nCantidad de Puertas:' + str(self.__cantPuertas)+ '\nColor:'+ self.__color + '\nPrecio de Base:'+ str(self.__precioBaseV)

    #metodo abstracto
    @abc.abstractmethod
    def getImporteVenta (self):
        pass

    @abc.abstractmethod
    def obtenerVehiculo (self):
        pass

    def toJSON (self):
        d = dict (
            __class__ = self.__class__.__name__,
            __atributos__ = dict (
                modelo = self.modelo,
                cantPuertas = self.__cantPuertas,
                color = self.__color,
                precioBaseV = self.__precioBaseV
            )
        )
        return d