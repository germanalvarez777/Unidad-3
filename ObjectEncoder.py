import json
from ListaVehiculos import ListaVehiculos
from claseVehiculoNuevo import VehiculoNuevo
from claseVehiculoUsado import VehiculoUsado

class ObjectEncoder:                #clase sin atributos
    def guardarArchJSON (self, dicc, archivo):
        with open(archivo, 'w', encoding = "UTF-8") as destino:
            json.dump (dicc, destino, indent = 4)
            destino.close()
    
    def leerArchJSON (self, archivo):
        with open (archivo, encoding = "UTF-8") as fuente:
            dicc = json.load(fuente)
            fuente.close()
            return dicc
        
    def decodificarDicc (self, dicc):
        if "__class__" not in dicc:
            return dicc
        else:
            class_name = dicc["__class__"]
            class_= eval(class_name)
            if class_name == "ListaVehiculos":
                vehiculos = dicc["comienzo"]
                manejador = class_()
                for i in range(len(vehiculos)):
                    dvehic = vehiculos[i]
                    class_name = dvehic.pop("__class__")
                    class_= eval(class_name)
                    atributos = dvehic["__atributos__"]
                    unVehic = class_(**atributos)
                    manejador.agregarElemento(unVehic)              #agrega cada instancia de vehic al final de la lista

                return manejador