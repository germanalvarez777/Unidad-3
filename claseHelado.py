from claseSabor import Sabor
class Helado:
    __gramos = 0
    __sabores = None
    def __init__ (self, gramos):
        self.__gramos = gramos
        self.__sabores = []
    def addSabor (self, unSabor):
        self.__sabores.append(unSabor)

    def getSabores (self):
        return self.__sabores
    def getGramos (self):
        return self.__gramos
    
    def mostrarHelado (self):
        print("Tipo de Helado: {}gr".format(self.__gramos))
        print("Mostramos los sabores del Helado: ")
        if ((len(self.__sabores)) <= 4):                        #Un helado puede tener como maximo 4 sabores
            for sabor in self.__sabores:
                print("-".center(30,'-'))
                sabor.mostrarSabor()
        else:
            print("El helado excede los 4 sabores\n")