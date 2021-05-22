class Empleado:
    __dni = None
    __nombre = ''
    __direccion = ''
    __telefono = None
    def __init__ (self, nom='', dni=0,direcc='', telef=0):
        self.__dni = dni
        self.__nombre = nom
        self.__direccion = direcc
        self.__telefono = telef
    def getDniEmp (self):
        return self.__dni
    def getNomEmp (self):
        return self.__nombre
    def getDireccionEmp (self):
        return self.__direccion
    def getTelefEmp (self):
        return self.__telefono
    
    #Metodo abstracto, aplicamos polimorfismo en cada subclase (Clase empleado candidata a clase Abstracta)
    def getSueldo (self):
        pass

    def mostrar (self):
        print("Nombre: {}\nDNI: {}\nDireccion: {}\nTelefono: {}\n".format(self.__nombre, self.__dni, self.__direccion, self.__telefono))
