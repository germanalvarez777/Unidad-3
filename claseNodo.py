from claseVehiculo import Vehiculo
import json
class Nodo:
    __vehiculo = None
    __siguiente = None
    def __init__ (self, unVehic):
        if isinstance (unVehic, Vehiculo):              #detecta subclases
            self.__vehiculo = unVehic
            
        self.__siguiente = None
    
    def setSiguiente (self, siguienteNodo):
        self.__siguiente = siguienteNodo
    
    def getSiguiente (self):
        return self.__siguiente
    
    def getDato (self):
        return self.__vehiculo
    
    """def toJSON (self):
        d = dict(
            __class__= self.__class__.__name__,
            __atributos__= dict (
                vehiculo = dict(self.__vehiculo.toJSON()),
                siguiente = self.__siguiente
            )
        )
        return d"""