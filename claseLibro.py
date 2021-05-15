from claseCapitulo import Capitulo
class Libro:
    __idLibro = 0
    __titulo = ''
    __autor = ''
    __editorial = ''
    __isbn = 0
    __cantidadCapitulos = 0
    __capitulos = None
    def __init__ (self, id=0, tit='', autor='', edit='', isbn=0, cant=0):
        self.__idLibro = id
        self.__titulo = tit
        self.__autor = autor
        self.__editorial = edit
        self.__isbn = isbn
        self.__cantidadCapitulos = cant
        self.__capitulos = []
    def getTitulo (self):
        return self.__titulo
    def getAutor (self):
        return self.__autor
    def getEditorial (self):
        return self.__editorial
    def getIdLibro (self):
        return self.__idLibro

    def cargarCapitulos (self, tit, cantPag):
        #for cap in self.__cantidadCapitulos:
        cap = Capitulo (tit, cantPag)
        self.__capitulos.append(cap)

    def getCapitulos (self):
        return self.__capitulos

    def mostrarLibro (self):
        print("Id Libro: {}\nTitulo: {}\nAutor: {}\nEditorial: {}\nISBN: {}\nCantidad Capitulos: {}\n".format(self.__idLibro, self.__titulo, self.__autor, self.__editorial, self.__isbn, self.__cantidadCapitulos))
        print("\n-----nMostramos la informacion de cada capitulo-----")
        if (self.__cantidadCapitulos == (len(self.__capitulos))):
            for cap in self.__capitulos:
                cap.mostrarCapitulo()
    
    def __del__ (self):
        print("Se eliminan sus capitulos...")
        del self.__capitulos