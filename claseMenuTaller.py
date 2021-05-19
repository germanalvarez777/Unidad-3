from ArregloTallerCapac import ArrayTC
from ManejaPersona import ManejaPersona
from ManejaInscripcion import ManejaInscripcion
class MenuTaller:
    __switcher = None
    __Mpersonas = None
    __Mtalleres = None
    __Minscriptos = None
    def __init__ (self):
        self.__switcher = {
         '1':self.opcion1,
         '2':self.opcion2,
         '3':self.opcion3,
         '4':self.opcion4,
         '5':self.opcion5,
         '6':self.opcion6,
         '7':self.salir
        }
        self.__Mpersonas = ManejaPersona()
        self.__Mpersonas.testListaPersonas()

        self.__Mtalleres = ArrayTC(3,5)
        self.__Minscriptos = ManejaInscripcion(5,5)

    def salir (self):
        print("Salida del Programa\n")

    def opcion (self, opcion):
        func = self.__switcher.get (opcion, lambda: print("Opcion no valida"))
        func()

    def opcion1 (self):
        print("Ha seleccionado la Opcion 1\nCargamos los datos de los talleres\n")
        self.__Mtalleres.testListaTaller()
        
    def opcion2 (self):
        print("Ha seleccionado la Opcion 2\nInscribimos a las personas en los talleres\n")
        listaP = self.__Mpersonas.obtenerListaPers()
        for pers in listaP:
            self.__Mtalleres.inscribirPersona (pers, self.__Minscriptos)
        
        self.__Mtalleres.mostrarArrayTaller()
        self.__Minscriptos.mostrarArrayIns()

    def opcion3 (self):
        print("Ha seleccionado la Opcion 3\nConsultar Inscripcion de una persona\n")
        self.__Mtalleres.consultarIns()

    def opcion4 (self):
        print("Ha seleccionado la Opcion 4\nConsultar Inscriptos de un taller\n")
        self.__Mtalleres.consultarInscriptos()

    def opcion5 (self):
        print("Ha seleccionado la Opcion 5\nRegistrar el pago de una persona\n")
        self.__Mpersonas.mostrarPersonas()
        self.__Mtalleres.registrarPago(self.__Minscriptos)

    def opcion6 (self):
        print("Ha seleccionado la Opcion 6\nGuardar los datos de los inscriptos en un nuevo archivo\n")
        self.__Minscriptos.guardarInsCsv()
