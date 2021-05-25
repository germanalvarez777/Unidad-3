from claseVehiculo import Vehiculo
from claseVehiculoNuevo import VehiculoNuevo
from claseVehiculoUsado import VehiculoUsado
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
    
    def getTipo (self):
        tipo = None
        if isinstance (self.__vehiculo, VehiculoNuevo):
            tipo = 'Vehiculo Nuevo'
        elif isinstance (self.__vehiculo, VehiculoUsado):
            tipo = 'Vehiculo Usado'

        return tipo