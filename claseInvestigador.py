from clasePersonal import Personal
class Investigador (Personal):
    __areaInv = None
    __tipoInv = None
    def __init__(self, nombre, apellido, cuil, sueldoBasico, antig, areaInv, tipoInv, carrera='', cargo='', catedra=''):
        super().__init__(nombre, apellido, cuil, sueldoBasico, antig, carrera, cargo, catedra, areaInv, tipoInv)      #mismo orden que clase base (personal)
        self.__areaInv = areaInv
        self.__tipoInv = tipoInv

    def getAreaInv (self):
        return self.__areaInv
    def getTipoInv (self):
        return self.__tipoInv

    def calcularSueldo (self):
        importe = self.getSueldoBasico() + (self.getSueldoBasico() + (self.getSueldoBasico() * (self.getAntig() / 100)))
        return importe

    def mostrarDatos (self):
        super().mostrarDatos()
        print("----Datos del Investigador----\n") 
        print("Area de Investigacion: {}\nTipo de INvestigacion: {}\nSueldo: {:.2f}".format(self.__areaInv, self.__tipoInv, self.calcularSueldo()))
        

    def toJSON (self):
        d = dict (
            __class__ = self.__class__.__name__,
            __atributos__ = dict (
                nombre = self.getNombre(),
                apellido = self.getApellido(),
                cuil = self.getCuil(),
                sueldoBasico = self.getSueldoBasico(),
                antig = self.getAntig(),
                areaInv = self.__areaInv,
                tipoInv = self.__tipoInv,
                carrera = '',
                cargo = '',
                catedra = ''
            )
        )
        return d