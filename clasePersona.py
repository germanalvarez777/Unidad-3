class Persona:
    __nombre = ''
    __direccion = ''
    __dni = ''
    def __init__ (self, nom='', dir='', dni=''):
        self.__nombre = nom
        self.__direccion = dir
        self.__dni = dni
    def getNombre (self):
        return self.__nombre
    def getDireccion (self):
        return self.__direccion
    def getDni (self):
        return self.__dni
    def mostrarPersona (self):
        print("Nombre: {}\nDireccion: {}\nDNI: {}\n".format(self.__nombre, self.__direccion, self.__dni))