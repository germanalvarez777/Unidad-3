from clasePersona import Persona
from claseInscripcion import Inscripcion
#from ManejaInscripcion import ManejaInscripcion
class TallerCapacitacion:
    __idTaller = 0
    __nombre = ''
    __vacantes = 0
    __montoInscripcion = 0
    __inscripciones = []
    def __init__ (self, id=0, nom='', vac=0, monto=0):
        self.__idTaller = id
        self.__nombre = nom
        self.__vacantes = vac
        self.__montoInscripcion = monto
    def getIdTaller (self):
        return self.__idTaller
    def getNombreTaller (self):
        return self.__nombre
    def getVacantes (self):
        return self.__vacantes
    def getMontoIns (self):
        return self.__montoInscripcion

    def actualizarVacantes (self, cant):
        self.__vacantes = self.__vacantes - cant

    def addInscripciones (self, unaPersona, maneIns, taller):
        if (taller.getIdTaller() == self.__idTaller):
            fecha = input("Ingrese la fecha de la inscripcion: ")
            unaInsc = Inscripcion (unaPersona, taller,fecha)

            maneIns.agregarInscripcion (unaInsc)
            #if (taller.getIdTaller() == self.__idTaller):
            self.__inscripciones.append(unaInsc)
            self.actualizarVacantes(1)
    
    def mostrarTaller (self):
        print("Id Taller: {}\nNombre: {}\nVacantes: {}\nMonto de Inscripcion: {}".format(self.__idTaller, self.__nombre, self.__vacantes, self.__montoInscripcion))
        for insc in self.__inscripciones:
            if (insc.getTallerIns() == self.__nombre):
                print('='.center(30,'='))
                insc.mostrarIns()

    #apartado 3
    def buscarPersona (self, doc, nombreT, montoT):
        i = 0
        band = False
        #for insc in self.__inscripciones:
        while ((i < len(self.__inscripciones)) and (band == False)):
            persona = self.__inscripciones[i].getPersonaIns()
            if ((doc == persona.getDni()) and (self.__inscripciones[i].getTallerIns() == nombreT)):
                band = True    
            i += 1
        if band == True:    
            print("Persona: {}, inscripta en taller: {}\nMonto que adeuda: {}".format(persona.getNombre(),nombreT, montoT))

    #apartado 4
    def inscriptosTaller (self, idtaller):
        for insc in self.__inscripciones:
            if (insc.getIdTallerIns() == idtaller):
                persona = insc.getPersonaIns()
                persona.mostrarPersona()

    #apartado 5
    def pagoPersona (self, dni, maneIns):
        band = False
        i = 0
        while ((i < len(self.__inscripciones)) and (band == False)):
            persona = self.__inscripciones[i].getPersonaIns()
            if (dni == persona.getDni()):
                self.__inscripciones[i].setPago(True)
                band = True
                maneIns.actualizarPago(dni)             
            i+= 1
        return band
        
