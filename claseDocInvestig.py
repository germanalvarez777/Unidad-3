from claseDocente import Docente
from claseInvestigador import Investigador

class DocInvestig (Docente, Investigador):
    __categInvestigacion = None
    __importeExtra = 0.0                              #1ero atributos de investig, despues de docente (regla del diamante)
    def __init__(self, nombre, apellido, cuil, sueldoBasico, antig,areaInv, tipoInv, carrera, cargo, catedra, categInvestigacion='', importeExtra=0.0):
        super().__init__(nombre, apellido, cuil, sueldoBasico, antig, carrera, cargo, catedra, areaInv, tipoInv)            #mismo orden que clase base (personal)
        self.__categInvestigacion = categInvestigacion
        self.__importeExtra = importeExtra

    def getCategInvest (self):
        return self.__categInvestigacion
    def getImporteExtra (self):
        return self.__importeExtra
    
    def calcularSueldo (self):
        importe = Docente.calcularSueldo(self) + self.__importeExtra               #sueldo de docente
        return importe

    def mostrarDatos (self):
        super().mostrarDatos()
        print("----Datos del Docente/Investigador----\n") 
        print("Categoria de Investigacion: {}\nImporte Extra: {:.2f}\nSueldo: {:.2f}".format(self.__categInvestigacion, self.__importeExtra, self.calcularSueldo()))

    def toJSON (self):
        d = dict (
            __class__ = self.__class__.__name__,
            __atributos__ = dict (
                nombre = self.getNombre(),
                apellido = self.getApellido(),
                cuil = self.getCuil(),
                sueldoBasico = self.getSueldoBasico(),
                antig = self.getAntig(),
                areaInv = self.getAreaInv (),
                tipoInv = self.getTipoInv (),
                carrera = self.getCarreraDoc(),
                cargo = self.getCargoDoc(),
                catedra = self.getCatedraDoc(),
                categInvestigacion = self.__categInvestigacion,
                importeExtra = self.__importeExtra
            )
        )
        return d