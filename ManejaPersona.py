import csv
import re
from clasePersona import Persona
class ManejaPersona:
    __listaPersonas = []
    def __init__ (self):
        self.__listaPersonas = []
    def agregarPersona (self, unaPersona):
        self.__listaPersonas.append(unaPersona)
    def testListaPersonas (self):
        archivo = open ('personas.csv', 'r')
        Reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in Reader:
            #fila[0] es nombre, fila[1] es direccion, fila[2] es dni
            if band:
                """saltear cabecera"""
                band = not band
            else:
                if re.match ('^[\d]', fila[0]):
                    print("Persona con datos no validos\n")
                else:
                    nom = fila[0]
                    direccion = fila[1]
                    dni = fila[2]
                    unaPersona = Persona (nom, direccion, dni)
                    self.agregarPersona(unaPersona)
        archivo.close()
    
    def obtenerListaPers (self):
        return self.__listaPersonas

    """def getPersona (self, indice):
        return self.__listaPersonas[indice]"""

    def mostrarPersonas (self):
        print("Mostramos el listado de personas: \n")
        for pers in self.__listaPersonas:
            print("-".center(40, '-'))
            pers.mostrarPersona()

        