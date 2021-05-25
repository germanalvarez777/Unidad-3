import json
from claseNodo import Nodo
from claseVehiculo import Vehiculo

from claseVehiculoNuevo import VehiculoNuevo
from claseVehiculoUsado import VehiculoUsado

from zope.interface import Interface
from zope.interface import implementer
from claseIElemento import IElemento
@implementer(IElemento)

class ListaVehiculos:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__ (self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
    
    def __iter__ (self):                #metodo iterador
        return self

    def agregarElemento (self, unVehic):                        #agregamos nuevo elemento al final de la lista 
        aux = self.__comienzo
        ant = aux
        if aux == None:                                             #lista vacia
            nodo = Nodo (unVehic)
            nodo.setSiguiente(self.__comienzo)                              #nuevo nodo apunta al comienzo(none)
            self.__actual = nodo
            self.__comienzo = nodo
            self.__tope += 1
        else:
            i = 0
            while ((aux != None) and (i < self.__tope)):
                ant = aux
                aux = aux.getSiguiente()
                i += 1

            if ant != None:                 
                nodo = Nodo (unVehic)
                ant.setSiguiente(nodo)                      #insertamos nuevo nodo al final de la lista
                nodo.setSiguiente (aux)                     #nuevo nodo apunta a aux(none)   
                self.__tope += 1
             
        print("Se agrego un nuevo elemento\n")

    def insertarElemento (self, pos, unVehic):
        aux = self.__comienzo
        band = False
        cont = 0
        ant = aux
        
        if (pos <= self.__tope):
            
            if cont == pos:                                                           #insertamos el elemento en la primera pos                
                if self.__comienzo == None:                                         #lista vacia
                    nodo = Nodo (unVehic)
                    nodo.setSiguiente (self.__comienzo)                
                    self.__comienzo = nodo
                    self.__actual = nodo                            
                    self.__tope += 1
                else:                                                       #lista no vacia
                    nodo = Nodo (unVehic)
                    
                    nodo.setSiguiente (aux)                                 #nuevo elem apunta al aux

                    aux.setSiguiente (aux.getSiguiente())                         

                    self.__comienzo = nodo

                    self.__tope += 1
                    
            else:
                ant = aux
                while ((aux != None) and (band == False)):
                    if (cont == pos):
                        band = True
                    else:
                        cont += 1
                        ant = aux
                        aux = aux.getSiguiente()

                if (cont == pos):                   #igual condicion a band == true
                    nodo = Nodo (unVehic)

                    ant.setSiguiente (nodo)                         #nodo anterior apunta al nuevo nodo a insertar
                    nodo.setSiguiente (aux)                         #nuevo nodo apunta al nodo que apuntaba antes el nodo ant
                    
                    self.__tope += 1
                    
        else:
            raise Exception("Posicion de la coleccion no es correcta\n")
            #insertamos al final dicho nodo con posicion incorrecta
            #self.agregarElemento (unVehic)

    def __next__ (self):                    #recorre en el iterador el sig elemento
        if (self.__indice == self.__tope):
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            if self.__actual == None:
                raise IndexError
            else:
                self.__indice += 1
                dato = self.__actual.getDato()
                self.__actual = self.__actual.getSiguiente()
                return dato
    
    def mostrarElemento (self, pos):
        aux = self.__comienzo
        cont = 0
        band = False   
             
        if ((pos < self.__tope) and (pos != None)):                 
            while ((aux != None) and (band == False)):
                #print("Cont: {}, pos: {}, band: {}, y auto: {}".format(cont, pos, band, aux.getDato().obtenerVehiculo()))
                if cont == pos:
                    band = True
                else:
                    aux = aux.getSiguiente()
                    cont += 1
            if (band == True):
                print("El elemento encontrado es: {}\n".format(aux.getDato().obtenerVehiculo()))
            else:
                print("Se ha producido un eror\n")
        else:
            raise Exception("\nError en la posicion de la coleccion, no es valida!!")
    
    #metodo opcional - recorrido de la lista por while
    def mostrarVehiculos (self):
        i = 0
        aux = self.__comienzo
        while ((aux != None) and (i < self.__tope)):
            print("=".center(40,'='))
            print(aux.getDato().mostrarVehiculo())
            i += 1
            aux = aux.getSiguiente()

    def toJSON (self):
        d = dict (
            __class__ = self.__class__.__name__,
            comienzo = [dato.toJSON() for dato in self]                       #contiene el primer vehiculo, el sig vehiculo, etc.
        )
        return d
    
    #metodos para opcion4
    def mostrarPatentesUsad (self):
        aux = self.__comienzo
        i = 0
        while ((aux != None) and (i < self.__tope)):
            vehic = aux.getDato()
            if isinstance (vehic, VehiculoUsado):                       #tiene que ser de tipo usado
                print("Patente: {}".format(vehic.getPatente()))
            aux = aux.getSiguiente()
            i += 1

    def modificarPrecioBase (self, pat):
        aux = self.__comienzo
        band = False
        while ((aux != None) and (band == False)):
            vehic = aux.getDato()
            if isinstance (vehic, VehiculoUsado):
                if (pat == vehic.getPatente()):
                    band = True
                    monto = float(input("Ingrese el nuevo precio base: "))
                    vehic.setPrecioBase(monto)
                    imp = vehic.getImporteVenta()
            aux = aux.getSiguiente()
        
        if (pat == vehic.getPatente()):                             #o puedo colocar band == true, pero si aux = none y sig elemento es la patente buscada
            print("El nuevo Importe de venta es: {}".format(imp))

    #metodo para opcion 5
    def autoEconomico (self):
        aux = self.__comienzo
        min = 100000000                 #le asignamos un valor alto
        i = 0
        while ((aux != None) and (i < self.__tope)):
            vehic = aux.getDato()
            if min > vehic.getImporteVenta():
                min = vehic.getImporteVenta()
                auto = vehic
            aux = aux.getSiguiente()
            i += 1
        
        print("Mostramos el vehiculo mas Economico\n")
        print(auto.mostrarVehiculo())
        #return auto

    def mostrarVehiculos (self):
        i = 0
        aux = self.__comienzo
        while ((aux != None) and (i < self.__tope)):
            print("=".center(40,'='))
            print(aux.getDato().mostrarVehiculo())
            i += 1
            aux = aux.getSiguiente()
