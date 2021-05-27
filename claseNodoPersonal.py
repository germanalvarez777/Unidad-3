from clasePersonal import Personal
from claseDocente import Docente
from claseInvestigador import Investigador
from claseDocInvestig import DocInvestig
from PersonalApoyo import PersonalApoyo

class NodoPersonal:
    __personal = None
    __siguiente = None
    def __init__(self, unaPersona):
        if isinstance (unaPersona, Personal):               #admite subclases
            self.__personal = unaPersona
        if isinstance (unaPersona, DocInvestig):
            self.__personal = unaPersona
        self.__siguiente = None
    
    def setSiguiente (self, sigPersona):
        self.__siguiente = sigPersona
    def getSiguiente (self):
        return self.__siguiente
    
    def getDato (self):
        return self.__personal
    
    def getTipo (self):
        tipo = None
        if isinstance (self.__personal, DocInvestig):               #1ero evaluo si es de la subclase con herencia multiple
            tipo = 'Docente e Investigador'
        elif isinstance (self.__personal, Investigador):
            tipo = 'Investigador'
        elif isinstance (self.__personal, Docente):
            tipo = 'Docente'
        elif isinstance (self.__personal, PersonalApoyo):
            tipo = 'Personal de Apoyo'
        
        return tipo
    
