from zope.interface.interfaces import IElement
from claseDocente import Docente
from claseInvestigador import Investigador
from claseDocInvestig import DocInvestig
from PersonalApoyo import PersonalApoyo
from clasePersonal import Personal
from claseNodoPersonal import NodoPersonal

from zope.interface import Interface
from zope.interface import implementer
from claseIElemento import IElemento
@implementer(IElemento)

class ListaPersonalUniv:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
    def __iter__ (self):
        return self
    def __next__ (self):
        if self.__indice == self.__tope:
            self.__indice = 0
            self.__actual = self.__comienzo
            raise StopIteration
        else:
            if self.__actual == None:
                raise IndexError
            else:
                self.__indice += 1
                dato = self.__actual.getDato()
                self.__actual = self.__actual.getSiguiente()
                return dato
    
    def getTope (self):
        return self.__tope
    
    def getComienzo (self):
        return self.__comienzo
    

    def agregarElemento (self, unPersonal):                        #agregamos nuevo elemento al final de la lista 
        aux = self.__comienzo
        ant = aux
        if aux == None:                                             #lista vacia
            nodo = NodoPersonal (unPersonal)
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
                nodo = NodoPersonal (unPersonal)
                ant.setSiguiente(nodo)                      #insertamos nuevo nodo al final de la lista
                nodo.setSiguiente (aux)                     #nuevo nodo apunta a aux(none)   
                self.__tope += 1
             
        print("Se agrego un nuevo elemento\n")

    def insertarElemento (self, pos, unPersonal):
        aux = self.__comienzo
        band = False
        cont = 0
        ant = aux
        
        if (pos <= self.__tope):
            
            if cont == pos:                                                           #insertamos el elemento en la primera pos                
                if self.__comienzo == None:                                         #lista vacia
                    nodo = NodoPersonal (unPersonal)
                    nodo.setSiguiente (self.__comienzo)                
                    self.__comienzo = nodo
                    self.__actual = nodo                            
                    self.__tope += 1
                else:                                                       #lista no vacia
                    nodo = NodoPersonal (unPersonal)
                    
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
                    nodo = NodoPersonal (unPersonal)

                    ant.setSiguiente (nodo)                         #nodo anterior apunta al nuevo nodo a insertar
                    nodo.setSiguiente (aux)                         #nuevo nodo apunta al nodo que apuntaba antes el nodo ant
                    
                    self.__tope += 1
                    
        else:
            raise Exception("Posicion de la coleccion no es correcta\n")
    

    def mostrarElemento (self, pos):
        aux = self.__comienzo
        cont = 0
        band = False   
             
        if ((pos < self.__tope) and (pos != None)):                 
            while ((aux != None) and (band == False)):
                #print("Cont: {}, pos: {}, band: {}, y Persona: {}".format(cont, pos, band, aux.getDato().getNomApell()))
                if cont == pos:
                    band = True
                else:
                    aux = aux.getSiguiente()
                    cont += 1
            if (band == True):
                print("El elemento encontrado es de tipo: {}\n".format(aux.getTipo()))
            else:
                print("Se ha producido un eror\n")
        else:
            raise Exception("\nError en la posicion de la coleccion, no es valida!!")

    def toJSON (self):
        d = dict (
            __class__ = self.__class__.__name__,
            personal = [dato.toJSON() for dato in self]
        )
        return d

    #metodos de opcion 4
    def mostrarCarreras (self):
        aux = self.__comienzo
        i = 0
        print("Mostramos las carreras en las que se dicta clases: \n")
        while ((aux != None) and (i < self.__tope)):
            if isinstance (aux.getDato(), DocInvestig):
                print("Carrera: {}".format(aux.getDato().getCarreraDoc()))
            elif isinstance (aux.getDato(), Docente):                       #elif para que no se repitan las carreras
                print("Carrera: {}".format(aux.getDato().getCarreraDoc()))
            i += 1
            aux = aux.getSiguiente()

    def validarRepetido (self, unPersonal):
        aux = self.__comienzo
        cont = 0
        while aux != None:
            if ((unPersonal.getApellido() == aux.getDato().getApellido()) and (unPersonal.getNombre() == aux.getDato().getNombre())):
                if (unPersonal.getCuil() == aux.getDato().getCuil()):
                    cont += 1
            aux = aux.getSiguiente()
        
        if cont > 1:
            band = True
        else:
            band = False
        
        return band

    def generarListadoDI (self, carrera):
        nodo = self.__comienzo
        p = None
        while nodo != None:
            p = nodo.getSiguiente()
            while (p != None):

                if (nodo.getDato().getNombre() > p.getDato().getNombre()):
                    aux = nodo.getDato
                    nodo.getDato = p.getDato
                    p.getDato = aux

                p = p.getSiguiente()
            
            nodo = nodo.getSiguiente()
        
        print("Mostramos la lista ordenada por Nombre\n")
        unic = False                #para mostrar una unica vez el personal repetido
        for dato in self: 
            if isinstance (dato, DocInvestig):
                if (dato.getCarreraDoc() == carrera):
                    cond = self.validarRepetido(dato)
                    if cond == False:
                        dato.mostrarDatos()
                    else:
                        if unic == False:
                            dato.mostrarDatos()
                            unic = True             #como ya se mostro el personal repetido, cambiamos el valor para no volver a mostrarlo


    #metodos de opcion 5
    def mostrarAreasInv (self):
        aux = self.__comienzo
        i = 0
        print("Mostramos las areas de investigacion disponibles: \n")
        while ((aux != None) and (i < self.__tope)):
            if isinstance (aux.getDato(), DocInvestig):
                print("Area de Investigacion: {}".format(aux.getDato().getAreaInv()))
            elif isinstance (aux.getDato(), Investigador):                              #elif para que no se repitan las areas
                print("Area de Investigacion: {}".format(aux.getDato().getAreaInv()))
            aux = aux.getSiguiente()
            i += 1

    def contarDoc_Inv (self, area):
        aux = self.__comienzo
        i = 0
        contarDI = 0
        contarI = 0
        while ((aux != None) and (i < self.__tope)):
            if isinstance (aux.getDato(), DocInvestig):
                if (aux.getDato().getAreaInv() == area):
                    contarDI += 1
            
            if (type(aux.getDato()) == Investigador):                   #para no contar la subclase Docente-Invest
                if (aux.getDato().getAreaInv() == area):
                    contarI += 1
            i += 1
            aux = aux.getSiguiente()
        
        print("Cantidad de Docentes-Inv: {}\nCantidad de Investigadores: {}".format(contarDI, contarI))

    #metodo para opcion 6
    
    def ordenarLista (self):
        nodo = self.__comienzo
        p = None
        while nodo != None:                         #metodo de ordenamiento por burbuja
            p = nodo.getSiguiente()
            while (p != None):

                if (nodo.getDato().getApellido() > p.getDato().getApellido()):
                    aux = nodo.getDato
                    nodo.getDato = p.getDato                #no se colocan los parentesis
                    p.getDato = aux

                p = p.getSiguiente()
            
            nodo = nodo.getSiguiente()
        
        print("Mostramos la lista ordenada\n")
        print("Nombre y Apellido    Tipo de Agente      Sueldo\n")
        unic = False                #para mostrar una unica vez el personal repetido
        for dato in self:   
            cond = self.validarRepetido(dato)
            if cond == False:
                print("{:8}      {:8}     {:.2f}\n".format(dato.getNomApell(), dato.getTipoP(), dato.calcularSueldo()))
            else:
                if unic == False:
                    print("{:8}      {:8}     {:.2f}\n".format(dato.getNomApell(), dato.getTipoP(), dato.calcularSueldo()))
                    unic = True             #como ya se mostro el personal repetido, cambiamos el valor para no volver a mostrarlo


    #metodos para opcion 7
    def mostrarCatInv (self):
        aux = self.__comienzo
        i = 0
        print("Mostramos las categorias de investigacion disponibles: \n")
        while ((aux != None) and (i < self.__tope)):
            if isinstance (aux.getDato(), DocInvestig):
                print("Categoria de Investigacion: {}".format(aux.getDato().getCategInvest()))
            aux = aux.getSiguiente()
            i += 1
    
    def calcularTotalExtra (self, cat):
        aux = self.__comienzo
        i = 0
        acum = 0
        print("Apellido     Nombre      Importe Extra\n")
        while ((aux != None) and (i < self.__tope)):
            if isinstance (aux.getDato(), DocInvestig):
                if (aux.getDato().getCategInvest() == cat):
                    print("{:8}   {:8}   {:8}".format(aux.getDato().getApellido(), aux.getDato().getNombre(), aux.getDato().getImporteExtra()))
                    acum += aux.getDato().getImporteExtra()
            i += 1
            aux = aux.getSiguiente()
        
        print("\nTotal de Importe Extra a cobrar por la categoria solicitada: {:.2f}".format(acum))
