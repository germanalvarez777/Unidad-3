class Capitulo:
    __titulo = ''
    __cantidadPaginas = 0
    def __init__ (self, titulo='', cant=0):
        self.__titulo = titulo
        self.__cantidadPaginas = cant
    def getTituloCap (self):
        return self.__titulo
    def getCantidadPaginas (self):
        return self.__cantidadPaginas
    def mostrarCapitulo (self):
        print("Capitulo: {}\nCantidad Paginas: {}\n".format(self.__titulo, self.__cantidadPaginas))
    def acumularPag (self, acum):
        acum += self.__cantidadPaginas
        return acum