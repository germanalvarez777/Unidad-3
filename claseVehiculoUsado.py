from claseVehiculo import Vehiculo
from datetime import date
class VehiculoUsado (Vehiculo):
    __marca = None
    __patente = None
    __anio = 0
    __kilometraje = 0.0
    def __init__ (self, modelo, cantPuertas, color, precioBaseV, marca='', patente='', anio=0, kilometraje=0.0):
        super().__init__(modelo, cantPuertas, color, precioBaseV)
        self.__marca = marca
        self.__patente = patente
        self.__anio = anio
        self.__kilometraje = kilometraje
    
    def getMarca (self):
        return self.__marca
    def getPatente (self):
        return self.__patente
    def getAño (self):
        return self.__anio
    def getKilometraje (self):
        return self.__kilometraje
    
    def getImporteVenta (self):               #metodo abstracto, hay que implementarlo para no ser subclase abstracta
        fecha = str(date.today())
        i = fecha.find('-')
        anioAc = int(fecha[:i])
        #print("Año actual es: ", anioAc)
        imp = self.getPrecioBase() - (self.getPrecioBase() * 0.01 * (anioAc - self.__anio))
        if (self.__kilometraje > 100000):
            imp -= self.getPrecioBase() * 0.02

        return imp  

    def mostrarVehiculo (self):
        print("---Mostramos info del vehiculo---\n")
        super().mostrarVehiculo()
        print("\n---Info de vehiculo usado---")
        #print("Marca: {}\nPatente: {}\nAño: {} - Kilometraje: {:.2f}".format(self.__marca, self.__patente, self.__anio, self.__kilometraje))
        return 'Marca:'+ self.__marca+'\nPatente:' + self.__patente+'\nAño:' + str(self.__anio)+'\nKilometraje:' + str(self.__kilometraje)+'\nImporte de Venta:'+ str(self.getImporteVenta())

    def obtenerVehiculo (self):                             #metodo para opcion 3
        return self.getModelo() + '-' + self.__marca

    def toJSON (self):
        d = dict (
            __class__ = self.__class__.__name__,
            __atributos__ = dict (
                modelo = self.getModelo(),
                cantPuertas = self.getCantPuertas(),
                color = self.getColor(),
                precioBaseV = self.getPrecioBase(),
                marca = self.__marca,
                patente = self.__patente,
                anio = self.__anio,
                kilometraje = self.__kilometraje                    #importe no debe almacenarse, pues no es un atributo de la clase
            )
        )
        return d