from claseManejaLibros import ManejaLibros
class MenuLibros:
    __switcher = None
    __manejadorL = None
    def __init__(self):
        self.__switcher = { 'a':self.opcion1,
            'b':self.opcion2,
            'c':self.salir
        }
        self.__manejadorL = ManejaLibros()
        self.__manejadorL.testListaLibros()
    
    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()
    
    def salir(self):
        print('Salida del Programa')

    def opcion1(self):
        print("Ejecutamos la Opcion 1\n")
        idl = int(input("Ingrese el identificador de un libro: "))
        self.__manejadorL.buscarLibro(idl)

    def opcion2(self):
        print("Ejecutamos la Opcion 2\n")
        palabra = input("Ingrese una palabra de algun libro o capitulo: \n")
        self.__manejadorL.buscarPalabra(palabra)
        