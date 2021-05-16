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

    def getLista (self):
        return self.__listaSabores

    def buscarNumero (self, nombre):
        for sabor in self.__listaSabores:
            if (sabor.getNombre() == nombre):
                return sabor.getNumeroSabor()

    def buscarDescrip (self, nombre):
        for sabor in self.__listaSabores:
            if (sabor.getNombre() == nombre):
                return sabor.getDescrip()

    def buscarNombreSabor (self, nro):
        for sabor in self.__listaSabores:
            if (sabor.getNumeroSabor() == nro):
                return sabor.getNombre()

    def mostrarSabores (self):
        for sabor in self.__listaSabores:
            print("-".center(40, '-'))
            sabor.mostrarSabor ()                

if __name__ == '__main__':
    ms = ManejaSabores()
    ms.testListaSabores()
    ms.mostrarSabores()