import json
import os
from ListaVehiculos import ListaVehiculos
from claseNodo import Nodo
from claseVehiculo import Vehiculo
from claseVehiculoNuevo import VehiculoNuevo
from claseVehiculoUsado import VehiculoUsado
from zope.interface import Interface
from zope.interface import implementer
from claseIElemento import IElemento
from MenuVehiculo import MenuVehiculo
from ObjectEncoder import ObjectEncoder
#@implementer (IElemento)

def cargarLista ():
    try:                            #archivo json ya cargado
        archivoJSON = ObjectEncoder()
        diccionario = archivoJSON.leerArchJSON('vehiculos.json')
        print("Dic: ", diccionario)
        listaAutos = archivoJSON.decodificarDicc (diccionario)
        print("Lista es: ", listaAutos)
        return listaAutos

    except:                         #archivo json no cargado 
        listaAutos = ListaVehiculos ()
        print("Se crea la Lista de Autos vacia\n")
        return listaAutos                       #retornamos la lista vacia


if __name__ == '__main__':
    
    salir = True
    menu = MenuVehiculo ()
    lista = cargarLista()
    while salir:
        print("""
        ===================================================================================
        1 - Insertar un vehículo en la colección en una posición determinada. 
        2 - Agregar un vehículo a la colección.
        3 - Mostrar por pantalla qué tipo de objeto se encuentra almacenado en una posición.
        4 - Modificar el precio base, y luego mostrar el precio de venta de un Auto Usado.
        5 - Mostrar todos los datos, incluido el importe de venta, del vehículo más económico.
        6 - Mostrar todos los vehiculos que la concesionaria tiene en venta.
        7 - Almacenar los objetos de la colección Lista en el archivo “vehiculos.json”.
        ====================================================================================\n
        """)
        op = input("Ingrese una opcion a trabajar: ")
        os.system ('clear')
        if ((op != '1') and (op != '2') and (op != '3') and (op != '4') and (op != '5') and (op != '6') and (op != '7') and (op != '8')):
            print("Opcion no Valida")
            salir = not salir
        else:
            if op == '8':
                menu.salir (lista)
                salir = not salir
            else:
                menu.opcion (op, lista)
