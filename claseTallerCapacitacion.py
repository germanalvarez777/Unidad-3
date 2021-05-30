from clasePersona import Persona
from claseInscripcion import Inscripcion
from datetime import date
#from ManejaInscripcion import ManejaInscripcion
class TallerCapacitacion:
    __idTaller = 0
    __nombre = ''
    __vacantes = 0
    __montoInscripcion = 0
    __inscripciones = []
    def __init__ (self, id=0, nom='', vac=0, monto=0):
        self.__idTaller = id
        self.__nombre = nom                     #ahi me fijo,  cualuier cosa le consulto
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

    def actualizarVacantes (self):
        self.__vacantes -= 1

    def addInscripciones (self, unaPersona, maneIns, taller):
        if (taller.getIdTaller() == self.__idTaller):
            fecha = date.today()                        #fecha de inscripcion es la fecha actual
            #print("La fecha de inscripcion es: {}".format(fecha))
            unaInsc = Inscripcion (unaPersona, taller,fecha)

            maneIns.agregarInscripcion (unaInsc)
            self.__inscripciones.append(unaInsc)
            self.actualizarVacantes()
    
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
        while ((i < len(self.__inscripciones)) and (band == False)):
            persona = self.__inscripciones[i].getPersonaIns()
            if ((doc == persona.getDni()) and (self.__inscripciones[i].getTallerIns() == nombreT)):     
                band = True    
            i += 1
        if band == True:    
            if (self.__inscripciones[i-1].getPago() == False):
                print("Persona: {}, inscripta en taller: {}\nMonto que adeuda: {}".format(persona.getNombre(),nombreT, montoT))
            else:
                print("Persona: {}, inscripta en el taller:{}\nNO adeuda un monto, pues ya lo pago!".format(persona.getNombre(),nombreT))
        return band                 #puedo hacer una condicion antes de entrar a este metodo, por el pago?

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
                maneIns.actualizarPago(dni)                     #es necesario actualizar el pago desde manejador de Inscriptos        
            i+= 1
        return band
        
