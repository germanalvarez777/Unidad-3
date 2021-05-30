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
@implementer (IElemento)

def testPrueba ():
    marca = input("Ingrese la marca de los vehiculos nuevos: ")
    VehiculoNuevo.setMarca (marca)
    lista_test = ListaVehiculos()
    unVehic = VehiculoUsado ('Suran', 4, 'Rojo', 695429.3, 'VW', 'ODI-932', 2019, 3932.3)
    lista_test.agregarElemento(unVehic)
    otroVehic = VehiculoNuevo ('Focus', 2, 'Azul marino', 485832.3, 'Full')
    lista_test.insertarElemento(0, otroVehic)
    otroveh2 = VehiculoNuevo ('Focus 2', 4, 'Gris', 736382.3, 'Base')
    lista_test.insertarElemento(1,otroveh2)
    for dato in lista_test:
        print("=".center(40, '='))
        print(dato.mostrarVehiculo())

def cargarLista ():
    try:                            #archivo json ya cargado
        archivoJSON = ObjectEncoder()
        diccionario = archivoJSON.leerArchJSON('vehiculos.json')
        #print("Dic: ", diccionario)
        listaAutos = archivoJSON.decodificarDicc (diccionario)
        #print("Lista es: ", listaAutos)
        print("Coleccion de vehiculos NO vacia\n")
        return listaAutos

    except:                         #archivo json no cargado 
        listaAutos = ListaVehiculos ()
        print("Se crea la Lista de Autos vacia\n")
        return listaAutos                       #retornamos la lista vacia


if __name__ == '__main__':
    
    testPrueba()
    input("\nHa finalizado la prueba de datos, presione una tecla para continuar: \n")
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
