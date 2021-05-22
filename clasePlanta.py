from claseEmpleado import Empleado
class Planta (Empleado):
    __sueldoBasico=0.0
    __antiguedad = 0
    def __init__ (self, nom, dni, direcc, telef, sueldoB = 0.0, antig=0):
        super().__init__(nom, dni, direcc, telef)
        self.__sueldoBasico = sueldoB
        self.__antiguedad = antig

    def getSueldoBasic (self):
        return self.__sueldoBasico
    def getAntigPlanta (self):
        return self.__antiguedad
    
    def getSueldo (self):
        #Sueldo = sueldo básico+ 1% del sueldo básico*antigüedad
        return self.__sueldoBasico + ((self.__sueldoBasico* 0.01) * self.__antiguedad)

    def mostrar (self):
        print("---Datos del Empleado---\n")
        super().mostrar()
        print("---Empleado de Tipo Planta---\n")
        print("Sueldo Basico: {} - Antiguedad: {}\n".format(self.__sueldoBasico, self.__antiguedad))
        print("Sueldo Calculado a Cobrar: {:.2f}".format(self.getSueldo()))
