from clasePersona import Persona
#from claseTallerCapacitacion import TallerCapacitacion          #para evitar la referencia ciclica
class Inscripcion:
    __fechaInscripcion = None
    __pago = False
    __persona = None
    __taller = None
    
    def __init__ (self,persona, taller, fecha):            #como es el unico parametro que se le asigna un valor, lo colocamos al final
        self.__fechaInscripcion = fecha
        self.__pago = False
        self.__persona = persona
        self.__taller = taller

    def getFechaIns (self):
        return self.__fechaInscripcion
    def getPago (self):
        return self.__pago

    def getPersonaIns (self):
        return self.__persona
    
    def getDniPersIns (self):
        return self.__persona.getDni()

    def setPago(self, valor):
        self.__pago = valor             #valor puede ser true o false

    def getTallerIns (self):
        return self.__taller.getNombreTaller()

    def getIdTallerIns (self):
        return self.__taller.getIdTaller()

    def mostrarIns (self):
        print("Fecha Inscripcion: {} - Pago: {}".format(self.__fechaInscripcion, self.__pago))
        print("Persona: {} - Taller: {}".format(self.__persona.getNombre(), self.__taller.getNombreTaller()))
    

    
    """def crearNewArchivo (self, Lista):
        fila = [self.__persona.getDni(), self.__taller.getIdTaller(), self.__fechaInscripcion, self.__pago]
        Lista.append(fila)"""