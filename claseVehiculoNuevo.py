from claseVehiculo import Vehiculo
class VehiculoNuevo (Vehiculo):
    __version = None            #base o full
    Marca = None                #todos los vehiculos nuevos son de la misma marca

    def __init__ (self, modelo, cantPuertas, color, precioBaseV, version):
        super().__init__(modelo, cantPuertas, color, precioBaseV)
        self.__version = version.lower()
        
    @classmethod
    def setMarca (cls, marca):
        cls.Marca = marca
    @classmethod
    def getMarca (cls):
        return cls.Marca
    
    def getVersion (self):
        return self.__version

    def getImporteVenta (self):               #metodo abstracto, hay que implementarlo para no ser subclase abstracta
        suma = self.getPrecioBase() + (self.getPrecioBase() * 0.10)
        if (self.__version == 'full'):
            suma += self.getPrecioBase() * 0.02
        return suma

    def mostrarVehiculo (self):
        print("---Mostramos info del vehiculo---\n")
        super().mostrarVehiculo()
        print("\n---Info de vehiculo nuevo---")
        #print("Version: {}\nMarca: {}".format(self.__version, VehiculoNuevo.getMarca()))
        return 'Version:' + self.__version +'\nMarca:' + VehiculoNuevo.getMarca() + '\nImporte de Venta:'+ str(self.getImporteVenta()) 

    def obtenerVehiculo(self):                                      #metodo para opcion3
        return self.getModelo() + '-' + VehiculoNuevo.getMarca()

    def toJSON (self):
        d = dict (
            __class__ = self.__class__.__name__,
            __atributos__ = dict (
                modelo = self.getModelo(),
                cantPuertas = self.getCantPuertas(),
                color = self.getColor(),
                precioBaseV = self.getPrecioBase(),
                version = self.__version                    #importe no debe almacenarse, pues no es un atributo de la clase
            )
        )
        return d