import json
from ListaVehiculos import ListaVehiculos
from claseNodo import Nodo
from claseVehiculo import Vehiculo
from claseVehiculoNuevo import VehiculoNuevo
from claseVehiculoUsado import VehiculoUsado
from zope.interface import Interface
from zope.interface import implementer
from claseIElemento import IElemento
from ObjectEncoder import ObjectEncoder

@implementer (IElemento)

class MenuVehiculo:
    __switcher = None
    __marcaNuevos = None
    __jsonFile = None

    def __init__ (self):
        self.__switcher = {
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '5':self.opcion5,
            '6':self.opcion6,
            '7':self.opcion7,
            '8':self.salir
        }
        self.__jsonFile = ObjectEncoder()
        #IElemento(self.__lista)                                        #es necesario restringir la interfaz en este ejercicio?
        marca = input("Ingrese la marca de los vehiculos nuevos: ")
        VehiculoNuevo.setMarca (marca)


    def opcion (self, op, lista):
        func = self.__switcher.get (op, lambda: print("Opcion no valida"))
        func (lista)
    
    def salir (self, lista):                
        print("\nSalida del programa!")

    def crearVehiculo (self):
        tipo = int(input("Ingrese el tipo de vehiculo a comprar:(1-Nuevo,2-Usado)\n"))
        if tipo == 1:
            modelo = input("Ingrese el modelo del vehiculo: ")
            cantP = int(input("INgrese la cantidad de puertas: "))
            color = input("Ingrese el color: ")
            precioB = float(input("Ingrese el precio de Base: "))
            
            version = input("Ingrese la version del mismo: ")
            if (version.lower() == 'full' or version.lower() == 'base'):
                unVehic = VehiculoNuevo (modelo, cantP, color, precioB, VehiculoNuevo.getMarca())
        
        elif tipo == 2:
            modelo = input("Ingrese el modelo del vehiculo: ")
            cantP = int(input("INgrese la cantidad de puertas: "))
            color = input("Ingrese el color: ")
            precioB = float(input("Ingrese el precio de Base: "))
            marca = input("Ingrese la marca del auto: ")
            patente = input("Ingrese la patente: ")
            anio = int(input("Ingrese el año del modelo: "))
            km = float(input("Ingrese el kilometraje del mismo: "))
            unVehic = VehiculoUsado (modelo, cantP, color, precioB, marca, patente, anio, km)
        else:
            print("El tipo de vehiculo a comprar es incorrecto\n")

        return unVehic

    def opcion1 (self, lista):
        print("Ejecutamos la Opcion 1\nInsertar un vehículo en la colección en una posición determinada\n")
        posicion = int(input("Ingrese una posicion determinada a insertar: "))
        carga = input("Desea cargar vehiculo o no(s/n): ")
        if (carga.lower() == 's'):
            unVehic = self.crearVehiculo ()
        else:
            op = int(input("Ingrese auto1 o auto2: "))
            if op == 1:
                unVehic = VehiculoUsado ('Suran', 4, 'Rojo', 695429.3, 'VW', 'ODI-932', 2019, 3932.3)
            elif op == 2:
                unVehic = VehiculoNuevo ('Focus 2', 4, 'Gris', 736382.3, 'Base')

        lista.insertarElemento (posicion, unVehic)

    def opcion2 (self, lista):
        print("Ejecutamos la Opcion 2 - Agregar un vehículo a la colección\n")
        carga = input("Desea cargar vehiculo o no(s/n): ")
        if (carga.lower() == 's'):
            unVehic = self.crearVehiculo ()
        else:
            unVehic = VehiculoNuevo ('Focus', 2, 'Azul marino', 485832.3, 'Full')
        
        lista.agregarElemento (unVehic)

    def opcion3 (self, lista):
        print("Ejecutmaos la Opcion 3 - Mostrar un vehiculo por su posicion\n")
        posicion = int(input("Ingrese una posicion determinada a mostrar: "))
        lista.mostrarElemento (posicion)

    def opcion4 (self, lista):
        print("Ejecutamos la Opcion 4 - Modificar precio de base y venta de Auto Usado\n")
        print("Mostramos las patentes de vehiculos usados\n")
        lista.mostrarPatentesUsad()
        pat = input("\nIngrese una patente: ")
        if (pat != None):
            lista.modificarPrecioBase (pat)
        else:
            print("Patente ingresada no es valida\n")

    def opcion5 (self, lista):
        print("Ejecutamos la Opcion 5 - Mostrar todos los datos del Auto mas economico\n")
        lista.autoEconomico()
        

    def opcion6 (self, lista):
        print("Ejecutamos la Opcion 6 - Mostramos todos los vehiculos\n")
        for dato in lista:
            print("=".center(40, '='))
            print(dato.mostrarVehiculo())

    def opcion7 (self, lista):
        print("Ejecutamos la Opcion 7 - Almacenar los objetos de la lista en Archivo JSON\n")
        dicc = lista.toJSON()
        self.__jsonFile.guardarArchJSON (dicc, 'vehiculos.json')