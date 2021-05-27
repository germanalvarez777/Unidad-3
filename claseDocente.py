from clasePersonal import Personal
class Docente (Personal):
    __carrera = None
    __cargo = None
    __catedra = None

    def __init__(self, nombre, apellido, cuil, sueldoBasico, antig,carrera, cargo, catedra, areaInv='', tipoInv=''):
        super().__init__(nombre, apellido, cuil, sueldoBasico, antig, areaInv, tipoInv, carrera, cargo, catedra)        #mismo orden que clase base (personal)
        self.__carrera = carrera
        self.__cargo = cargo.lower()
        self.__catedra = catedra

    def getCarreraDoc (self):
        return self.__carrera

    def getCargoDoc (self):
        return self.__cargo
    def getCatedraDoc (self):
        return self.__catedra
    
    def calcularSueldo (self):
        importe = self.getSueldoBasico() + (self.getSueldoBasico()+ (self.getSueldoBasico() * (self.getAntig() / 100)))
        if (self.__cargo == 'simple'):
            importe += (self.getSueldoBasico() * 0.10)
        elif self.__cargo == 'semiexclusivo':
            importe += (self.getSueldoBasico() * 0.20)
        elif self.__cargo == 'exclusivo':
            importe += (self.getSueldoBasico() * 0.30)
        else:
            print("Cargo del Docente no es valido\n")
        
        return importe 

    def mostrarDatos (self):
        super().mostrarDatos()
        print("----Datos del Docente----\n")
        print("Carrera: {}\nCargo: {}\nCatedra: {}\nSueldo: {:.2f}".format(self.__carrera, self.__cargo, self.__catedra, self.calcularSueldo()))

    def toJSON (self):
        d = dict (
            __class__ = self.__class__.__name__,
            __atributos__ = dict (
                nombre = self.getNombre(),
                apellido = self.getApellido(),
                cuil = self.getCuil(),
                sueldoBasico = self.getSueldoBasico(),
                antig = self.getAntig(),
                carrera = self.__carrera,
                cargo = self.__cargo,
                catedra = self.__catedra,
                areaInv = '',
                tipoInv = ''
            )
        )
        return d