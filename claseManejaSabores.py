import csv
import re
from claseSabor import Sabor
class ManejaSabores:
    __listaSabores = None
    def __init__ (self):
        self.__listaSabores = []
    def agregarSabor (self, unSabor):
        self.__listaSabores.append(unSabor)
    def testListaSabores (self):
        archivo = open ('sabores.csv', 'r')
        Reader = csv.reader (archivo, delimiter=';')
        bandera = True
        for fila in Reader:
            if bandera:
                """saltear cabecera"""
                bandera = not bandera
            else:
                #fila[0] es nombre del sabor, fila[1] es la descripcion
                if re.match ('^[\d]', fila[0]):                         #verifico que el nombre del sabor no sea numerico
                    print("Helado no valido")
                else:
                    nombre = fila[0]
                    descripcion = fila[1]
                    unSabor = Sabor (nombre, descripcion)
                    self.agregarSabor(unSabor)
        archivo.close()

    #metodo utilizado para definir las listas de sabores pedidos
    def getLista (self):
        return self.__listaSabores

    def buscarNumero (self, nombre):
        band = False
        i = 0
        while ((i < len(self.__listaSabores)) and (band == False)):
            if (self.__listaSabores[i].getNombre() == nombre):
                band = True
            i += 1        
        
        return self.__listaSabores[i-1].getNumeroSabor()

    def buscarDescrip (self, nombre):
        i = 0
        band = False
        while ((i < len(self.__listaSabores)) and (band == False)):
            if (self.__listaSabores[i].getNombre() == nombre):
                band = True
            i += 1        
        
        return self.__listaSabores[i-1].getDescrip()

    def buscarNombreSabor (self, nro):
        i = 0
        band = False
        while ((i < len(self.__listaSabores)) and (band == False)):
            if (self.__listaSabores[i].getNumeroSabor() == nro):
                band = True
            i += 1        
        
        return self.__listaSabores[i-1].getNombre()

    def mostrarSabores (self):
        for sabor in self.__listaSabores:
            print("-".center(40, '-'))
            sabor.mostrarSabor ()                
