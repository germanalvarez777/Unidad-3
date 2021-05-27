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
                print("Cont: {}, pos: {}, band: {}, y Persona: {}".format(cont, pos, band, aux.getDato().getNomApell()))
                if cont == pos:
                    band = True
                else:
                    aux = aux.getSiguiente()
                    cont += 1
            if (band == True):
                print("El elemento encontrado es: {}\n".format(aux.getTipo()))
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

    def generarListadoDI (self, carrera):
        """aux = self.__comienzo
        i = 0
        lista = []
        while ((aux != None) and (i < self.__tope)):
            if isinstance (aux.getDato(), DocInvestig):
                if (aux.getDato().getCarreraDoc() == carrera):
                    lista.append(aux.getDato())                     #contiene los objetos Docente-Investigador
            i += 1
            aux = aux.getSiguiente ()
        
        lista.sort()
        for doc_inv in lista:                       #ordenamos de forma ascendente por nombre
            doc_inv.mostrarDatos()"""
        
        #otra forma de ordenarlo
        nodo = self.__comienzo
        p = None
        k = None
        cota = None

        #solo es para mostrar el listado de nombres
        com = self.__comienzo                   
        i = 0
        while ((com != None) and (i < self.__tope)):            #para verificar el recorrido
            print("La componente es: ", com.getDato().getNombre())
            com = com.getSiguiente()
            i += 1

        #empieza el ordenamiento por burbuja
        while ((k != nodo)):  
            k = nodo
            p = nodo
            x = p.getSiguiente()
            anterior = p                        #para contener el comienzo de la lista
            
            while x != cota: 
                s = p.getSiguiente()
                
                #para evaluar si llego a none
                if (p == None or s == None):
                    x = None
                    """com = self.__comienzo                   
                    i = 0
                    while ((com != None) and (i < self.__tope)):                #muestro el recorrido de la primera pasada while
                        print("La componente es: ", com.getDato().getNombre())
                        com = com.getSiguiente()
                        i += 1"""
                else:
                    if (p.getDato().getNombre() > s.getDato().getNombre()):
                        aux= s             #resguarda el menor
                        aux1 = s.getSiguiente()

                        s = p               #apunta al mayor
                        p = aux           #apunta al menor
                                
                        p.setSiguiente(aux)
                        s.setSiguiente(aux1)       

                        anterior.setSiguiente(p)
                        print("Se realizo el intercambio")
                        #print("1)Ant: ", anterior.getDato().getNombre(), 'P: ', p.getDato().getNombre(), 'S: ', s.getDato().getNombre())
                        anterior = anterior.getSiguiente()
                                
                        p = p.getSiguiente()
                        s = s.getSiguiente()

                        k = p                       #guarda el cambio

                    else:
                        print("No se realizo el intercambio\n")
                        #print("2)Ant: ", anterior.getDato().getNombre(), 'P: ', p.getDato().getNombre(), 'S: ', s.getDato().getNombre())
                        #anterior = p
                        p = p.getSiguiente()
                    #print("3)Antsig: ", anterior.getDato().getNombre(), 'Psig: ', p.getDato().getNombre(), 'Ssig: ', s.getDato().getNombre())
                    #input("Pausa")
                    if p == None:
                        x = None
                    else:
                        x = p
            cota = k.getSiguiente()
        

        print("Mostramos la lista en forma ordenada por Nombre\n")
        aux = self.__comienzo
        i = 0
        while ((aux != None) and (i < self.__tope)):
            if isinstance (aux.getDato(), DocInvestig):
                if (aux.getDato().getCarreraDoc() == carrera):
                    aux.getDato().mostrarDatos()
            i += 1
            aux = aux.getSiguiente()


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

    #metodos para opcion 6
    def ordenarLista (self):                #ordenamos toda la lista, por metodo de burbuja
        nodo = self.__comienzo
        p = None
        k = None
        cota = None

        while ((k != nodo)):  
            k = nodo
            p = nodo
            
            x = p.getSiguiente()
            anterior = p
            while x != cota: 
                s = p.getSiguiente()
                if (p == None or s == None):
                    x = None
                    com = self.__comienzo
                    i = 0
                    while ((com != None) and (i < self.__tope)):            #para mostrar la comparacion
                        #print("Comp: ", com.getDato().getApellido())
                        com = com.getSiguiente()
                        i += 1
                else:
                    if (p.getDato().getApellido() > s.getDato().getApellido()):
                        aux = s             #resguarda el menor
                                   
                        s = p               #apunta al mayor
                        p = aux           #apunta al menor
                        
                        s.setSiguiente(p.getSiguiente())
                        p.setSiguiente(s)
                        
                        anterior.setSiguiente(p)
                        #print("Ant: ", anterior.getDato().getApellido(), 'P: ', p.getDato().getApellido(), 'S: ', s.getDato().getApellido())
                        anterior = anterior.getSiguiente()
                        
                        p = p.getSiguiente()
                        s = s.getSiguiente()
                        #print("AntSig: ", anterior.getDato().getApellido(), 'PSig: ', p.getDato().getApellido(), 'Ssig: ', s.getDato().getApellido())
                        k = p                       #guarda el cambio

                        #print("Se realizo el intercambio")
                    else:
                        #print("No se realizo el intercambio\n")
                        anterior = p
                        p = p.getSiguiente()

                    if p == None:
                        x = None
                    else:
                        x = p
            cota = k.getSiguiente()
            

    def generarListado (self):

        self.ordenarLista()             #lista ordenada por apellido, ahora se recorre
        aux = self.__comienzo
        i = 0
        print("Nombre y Apellido    Tipo de Agente      Sueldo\n")
        while ((aux != None) and (i < self.__tope)):
            print("{:8}      {:8}     {:.2f}\n".format(aux.getDato().getNomApell(), aux.getTipo(), aux.getDato().calcularSueldo()))
            i += 1
            aux = aux.getSiguiente()


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
