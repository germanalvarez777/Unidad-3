import numpy as np
import csv
import re
from claseTallerCapacitacion import TallerCapacitacion
class ArrayTC:
    __cantidad = 0
    __incremento = 5
    __dimension = 0
    def __init__ (self, dim=5, inc=5):
        self.__incremento = inc
        self.__dimension = dim
        #self.__talleres = np.empty (self.__dimension, dtype=TallerCapacitacion)
        self.__cantidad = 0
    def agregarArrayTaller (self, unTaller):
        if (self.__cantidad == self.__dimension):
            self.__dimension += self.__incremento
            self.__talleres.resize (self.__dimension)
        self.__talleres[self.__cantidad] = unTaller
        self.__cantidad += 1
    def testListaTaller (self):
        archivo = open('Talleres.csv', 'r')
        Reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in Reader:
            if band:
                """salteamos cabecera"""
                cantidad = int(fila[0])                 #en 1era linea tenemos la cantidad de talleres
                self.__dimension = cantidad
                self.__talleres = np.empty (self.__dimension, dtype=TallerCapacitacion)
                print("La cantidad de talleres es: ", self.__dimension)
                band = not band 
            else:
                #fila[0] es idtaller, fila[1] es nombre, fila[2] es vacantes, fila[3] es monto
                if re.match ('^[\d]', fila[0]):         #nos aseguramos que empieze con numero decimal
                    idtaller = int(fila[0])
                    nombre = fila[1]
                    vac = int(fila[2])
                    monto = int(fila[3])
                    unTaller = TallerCapacitacion (idtaller, nombre, vac, monto)
                    self.agregarArrayTaller (unTaller)
                else:
                    print("Datos de un Taller de Capacitacion no validos\n")
        archivo.close ()
    
    def obtenerunTaller (self, idtaller):
        i = 0
        band = False
        while ((i < self.__cantidad) and (band == False)):
            if (self.__talleres[i].getIdTaller() == idtaller):
                band = True
            i += 1
        return self.__talleres[i-1]


    def inscribirPersona (self, unaPersona, manejaInsc):
        print("\nPersona: {}".format(unaPersona.getNombre()))
        print("\nLos talleres disponibles son:")

        #Para mostrar los id de taller disponibles
        for i in range(self.__cantidad):
            print("Id Taller: ", self.__talleres[i].getIdTaller(), end=' - ')
        
        idt = int(input("\nIngrese el numero de taller a inscribirse: "))
        unTaller = self.obtenerunTaller (idt)
        if (unTaller != None):
            unTaller.addInscripciones (unaPersona, manejaInsc, unTaller)

    def mostrarArrayTaller (self):
        print("\nMostramos la informacion de los talleres registrados:\n")
        for i in range(self.__cantidad):
            print("/".center(40,'/'))
            self.__talleres[i].mostrarTaller()
    
    #apartado 3
    def consultarIns (self):
        bandera = False         
        i = 0
        dni = (input("Ingrese el DNI de una persona: "))
        
        while ((i < self.__cantidad) and (bandera == False)):
            nombre = self.__talleres[i].getNombreTaller()
            monto = self.__talleres[i].getMontoIns()

            bandera = self.__talleres[i].buscarPersona (dni, nombre, monto)
            i += 1
            

    #apartado4

    def consultarInscriptos (self):
        print("\nLos talleres disponibles son:")
        for i in range(self.__cantidad):
            print("Id Taller: ", self.__talleres[i].getIdTaller(), end=' - ')

        idtaller = int(input("\nIngrese el Identificador de un Taller: "))
        for i in range(self.__cantidad):
            if (self.__talleres[i].getIdTaller() == idtaller):
                self.__talleres[i].inscriptosTaller(idtaller)
    #apartado5 
    def registrarPago (self, maneIns):
        band = False
        i = 0
        dni = input("Ingrese el DNI de una Persona: ")
        while ((i < (self.__cantidad)) and (band == False)):
            band = self.__talleres[i].pagoPersona(dni, maneIns)
            i += 1
        if band == True:
            print("Se ha registrado el pago de dicha persona\n")
        else:
            print("No se ha podido registrar el pago\n")
    