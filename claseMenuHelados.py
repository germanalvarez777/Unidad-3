from claseManejaSabores import ManejaSabores
from claseManejaHelados import ManejaHelados
class MenuHelados:
    __switcher = None
    __manejadorH = None
    __manejadorS = None
    def __init__ (self):
        self.__switcher = {
         '1':self.opcion1,
         '2':self.opcion2,
         '3':self.opcion3,
         '4':self.opcion4,
         '5':self.salir   
        }
        self.__manejadorS = ManejaSabores()
        self.__manejadorS.testListaSabores()
        self.__manejadorH = ManejaHelados()
        self.__manejadorH.testListaHelados(self.__manejadorS)
        print("Mostramos el listado de Helados: ")
        self.__manejadorH.mostrarHelados()

    def getSwitcher(self):
        return self.__switcher
    
    def opcion (self, op):
        func = self.__switcher.get(op, lambda: print("Opcion no valida"))
        func()
    
    def salir (self):
        print("Salida del Programa")

    def opcion1 (self):
        print("Ejecutamos la Opcion 1 - Registrar una Instancia de Helado\n")
        self.__manejadorH.unaInstanciaH (self.__manejadorS)
        print("Mostramos el listado de Helados con nueva instancia: ")
        self.__manejadorH.mostrarHelados()

    def opcion2 (self):
        cont = 0
        maximo = 0
        indice = 0
        print("Ejecutamos la Opcion 2 - Mostramos el nombre de los 5 sabores mas pedidos\n")
        lista_pe = self.__manejadorH.saboresMasPedidos(self.__manejadorS)
        lista_nros = [0 for i in range(len(lista_pe))]                      #lista que almacena los nros de sabores
        for i in range (len(lista_pe) - 1):
            maximo = i
            j = i+1
            while j < (len(lista_pe)):
                if (lista_pe[j] > lista_pe[maximo]):
                    maximo = j
                j += 1
            aux = lista_pe[i]
            lista_pe[i] = lista_pe[maximo]
            if (lista_pe[i] > 0):
                lista_nros[i] = maximo + 1                          #en nueva lista guardamos el indice del mayor
            lista_pe[maximo] = aux

        #print("Lista Pe Ordenada: ", lista_pe)
        #print("Lista Nros Ordenada: ", lista_nros)
        print("Mostramos los 5 sabores de Helados mas Pedidos\n")
        for k in range(5):
            print("Nombre Sabor: {} - Pedidos: {}".format(self.__manejadorS.buscarNombreSabor(lista_nros[k]), lista_pe[k]))



    def opcion3 (self):
        print("Ejecutamos la Opcion 3\n")
        nrosabor = int(input("Ingrese un numero de sabor: "))
        acum = self.__manejadorH.totalGrVendidos (nrosabor)
        print("El total de gramos vendidos es: {}".format(acum))

    def opcion4 (self):
        print("Ejecutamos la Opcion 4\n")
        tipoh = int(input("Ingrese un tipo de Helado(100-150-250-500-1000gr)\n"))
        self.__manejadorH.saboresVendidos (tipoh)