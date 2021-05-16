import numpy as np
import csv
from claseInscripcion import Inscripcion
class ManejaInscripcion:
    __cantidad = 0
    __incremento = 5
    __dimension = 0
    def __init__ (self, dim=0, inc=5):
        self.__cantidad = 0
        self.__incremento = inc
        self.__dimension = dim
        self.__inscripciones = np.empty (self.__dimension, dtype=Inscripcion)
    def agregarInscripcion (self, unaInsc):
        if (self.__cantidad == self.__dimension):
            self.__dimension += self.__incremento
            self.__inscripciones.resize(self.__dimension)
        self.__inscripciones[self.__cantidad] = unaInsc
        self.__cantidad += 1
    
    def mostrarArrayIns (self):
        print("\nMostramos el listado de Inscripciones\n")
        for i in range(self.__cantidad):
            print("-".center(34,'-'))
            self.__inscripciones[i].mostrarIns()
    
    def actualizarPago (self, dni):
        band = False
        i = 0
        #for i in range (self.__cantidad):
        while ((i < (self.__cantidad)) and (band == False)):
            if (self.__inscripciones[i].getDniPersIns() == dni):
                band = True
                if (band == True):
                    #self.__inscripciones[i].__pago = True
                    self.__inscripciones[i].setPago(True)
            i += 1
        
        if (band == True):
            print("Se actualizo el pago")
        else:
            print("No se actualizo el pago")
        
    #apartado 6
    def guardarInsCsv (self):
        archivo = open ('newInscripPago.csv', 'w')
        Writer = csv.writer (archivo, delimiter=';')
        lista = []
        for i in range(self.__cantidad):
            self.__inscripciones[i].crearNewArchivo (lista)
        
        print("Lista es: ", lista)
        Writer.writerows (lista)