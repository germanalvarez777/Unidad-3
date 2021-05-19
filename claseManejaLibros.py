import csv
import re
from claseLibro import Libro
from claseCapitulo import Capitulo
class ManejaLibros:
    __listaLibros = None
    def __init__ (self):
        self.__listaLibros = []
    def agregarLibro (self, unLibro):
        self.__listaLibros.append(unLibro)

    def testListaLibros (self):
        archivo = open ('libros.csv', 'r')
        Reader = csv.reader(archivo, delimiter=',')
        for fila in Reader:
            if re.match ('^[0-9]', fila[0]):            #[0-9] o [\d]
                #fila[0] es idlibro, fila[1] es titulo, fila[2] es autor, fila[3] es editorial, fila[4] es isbn, fila[5] es cantcapi
                idlibro = int(fila[0])
                tit = fila[1]
                autor = fila[2]
                edit = fila[3]
                isbn = int(fila[4])
                cantCap = int(fila[5])
                unLibro = Libro (idlibro, tit, autor, edit, isbn, cantCap)
                self.agregarLibro(unLibro)
                #self.__listaLibros.insert(i,unLibro)
            else:
                #fila[0] es titulo del capitulo, fila[1] es cantidad de paginas
                titC = fila[0]
                cantpag = int(fila[1])
                unLibro.cargarCapitulos(titC, int(cantpag))

    def mostrarListaLibros (self):
        for libro in self.__listaLibros:
            print("=".center(40,'='))
            libro.mostrarLibro()

    def buscarLibro (self, identificador):
        i = 0
        acumulador = 0
        band = False
        while ((i < (len(self.__listaLibros))) and band == False):
            if (identificador == self.__listaLibros[i].getIdLibro()):
                band = True
                print("Titulo del Libro: {}".format(self.__listaLibros[i].getTitulo()))
                for cap in self.__listaLibros[i].getCapitulos():
                    print("-".center(30,'-'))
                    cap.mostrarCapitulo()
                    acumulador = cap.acumularPag(acumulador)
            i += 1
        print("Cantidad total de paginas es: {}".format(acumulador))

    def buscarPalabra (self, palabra):          #recorremos todo el manejador de libros con sus capitulos
        for libro in self.__listaLibros:
            if re.search (palabra, libro.getTitulo()):
                print("-----Se encontro coincidencia en libro-----")
                print("Titulo: {}\nAutor: {}\n".format(libro.getTitulo(), libro.getAutor()))
            #else:
            for cap in libro.getCapitulos():
                if re.search (palabra, cap.getTituloCap()):
                    print("\n----Se encontro coincidencia en capitulo----")
                    print("Titulo Libro: {}\nAutor: {}\nCapitulo: {}\n".format(libro.getTitulo(), libro.getAutor(), cap.getTituloCap()))
        