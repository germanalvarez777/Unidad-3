from clasePersonal import Personal
class PersonalApoyo (Personal):
    __categoria = None
    def __init__(self, nombre, apellido, cuil, sueldoBasico, antig, categoria = 0):
        super().__init__(nombre, apellido, cuil, sueldoBasico, antig)         
        self.__categoria = categoria

    def getCategPApoyo (self):
        return self.__categoria

    def calcularSueldo (self):
        importe = self.getSueldoBasico() + (self.getSueldoBasico() + (self.getSueldoBasico() * (self.getAntig() / 100)))
        if self.__categoria >= 1 and self.__categoria <= 10:
            importe += self.getSueldoBasico() * 0.10
        elif ((self.__categoria >= 11) and (self.__categoria <= 20)):
            importe += self.getSueldoBasico() * 0.20
        elif ((self.__categoria == 21) or (self.__categoria == 22)):
            importe += self.getSueldoBasico() * 0.30
        else:
            print("Categoria del Personal de Apoyo no es valida\n")
        
        return importe

    def mostrarDatos (self):
        super().mostrarDatos()
        print("----Datos del Personal de Apoyo----\n")
        print("Categoria: {} - Sueldo: {:.2f}\n".format(self.__categoria, self.calcularSueldo()))
    
    def toJSON (self):
        d = dict (
            __class__ = self.__class__.__name__,
            __atributos__ = dict (
                nombre = self.getNombre(),
                apellido = self.getApellido(),
                cuil = self.getCuil(),
                sueldoBasico = self.getSueldoBasico(),
                antig = self.getAntig(),
                categoria = self.__categoria
            )
        )
        return d