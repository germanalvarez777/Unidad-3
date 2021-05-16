class Sabor:
    #variable de clase (dato miembro estatico)
    numero = 0
    #variables de instancia
    __numero = 0
    __nombre = ''
    __descripcion = ''

    #funcion miembro estatica (metodo de variable de clase)
    @classmethod
    def getNumero (cls):
        cls.numero += 1
        return cls.numero
    def __init__ (self, nom='', desc=''):
        self.__numero = Sabor.getNumero()
        self.__nombre = nom
        self.__descripcion = desc
    def getNumeroSabor (self):
        return self.__numero
    def getNombre (self):
        return self.__nombre
    def getDescrip (self):
        return self.__descripcion

    @classmethod
    def setNumero (cls, valor):                   
        cls.numero = valor-1                            #le resto uno, pues la proxima vez que cree una instancia se incrementa automatic en 1

    def mostrarSabor (self):
        print("Numero Sabor: {}\nNombre: {}\nDescripcion: {}".format(self.__numero, self.__nombre, self.__descripcion))
    