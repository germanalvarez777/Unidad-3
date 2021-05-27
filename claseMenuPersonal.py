from claseNodoPersonal import NodoPersonal
from ListaPersonalUniv import ListaPersonalUniv

from clasePersonal import Personal
from claseDocente import Docente
from claseInvestigador import Investigador
from PersonalApoyo import PersonalApoyo
from claseDocInvestig import DocInvestig

from claseObjectEncoderP import ObjectEncoderP

from zope.interface import Interface
from zope.interface import implementer
from claseIElemento import IElemento
@implementer(IElemento)

class MenuPersonal: 
    __switcher = None
    __jsonArch = None
    def __init__(self):
        self.__switcher = {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '4': self.opcion4,
            '5': self.opcion5,
            '6': self.opcion6,
            '7': self.opcion7,
            '8': self.opcion8,
            '9': self.salir
        }
        self.__jsonArch = ObjectEncoderP()
    
    def opcion (self, op, lista):
        func = self.__switcher.get(op, lambda: print("Opcion no valida"))
        func(lista)

    def salir (self, lista):
        print("Salida del Programa\n")
    
    def cargarAgente (self):
        tipo = int(input("Ingrese un tipo de Personal(1-Docente,2-Investigador,3-PersonaldeApoyo,4-Doc/Inv)\n"))
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        cuil = input("Ingrese el cuil: ")
        sueldoB = float(input("Ingrese el sueldo basico: "))
        antig = int(input("Ingrese la antiguedad: "))
        if tipo == 1:
            carrera = input("Ingrese la carrera donde dicta clases: ")
            cargo = input("Ingrese el cargo docente(Simple, Semiexclusivo, Exclusivo)\n")
            catedra = input("Ingrese la catedra donde trabaja: ")
            agente = Docente (nombre, apellido, cuil, sueldoB, antig, carrera, cargo, catedra)
        elif tipo == 2:
            areaInv = input("Ingrese el area de investigacion: ")
            tipoInv = input("Ingrese el tipo de investigacion: ")
            agente = Investigador (nombre, apellido, cuil, sueldoB, antig, areaInv, tipoInv)
        elif tipo == 3:
            categ = input("Ingrese una categoria de inv(I,II,III,IV,V): ")
            if ((categ == 'I') or (categ == 'II') or (categ == 'III') or (categ == 'IV') or (categ == 'V')):
                agente = PersonalApoyo (nombre, apellido, cuil, sueldoB, antig, categ)

        elif tipo == 4:
            areaInv = input("Ingrese el area de investigacion: ")
            tipoInv = input("Ingrese el tipo de investigacion: ")
            carrera = input("Ingrese la carrera donde dicta clases: ")
            cargo = input("Ingrese el cargo docente(Simple, Semiexclusivo, Exclusivo)\n")
            catedra = input("Ingrese la catedra donde trabaja: ")
            categInv = input("Ingrese una categoria de inv(I,II,III,IV,V): ")
            impExtra = float(input("Ingrese un importe extra: "))
            agente = DocInvestig (nombre, apellido, cuil, sueldoB, antig, areaInv, tipoInv,carrera, cargo, catedra, categInv, impExtra)

        else:
            print("El tipo de personal ingresado no es correcto!\n")

        return agente

    def opcion1 (self, lista):
        print("Ejecutamos la Opcion 1\nInsertar agente en una posicion de la coleccion\n")
        #unAgente = self.cargarAgente ()
        op = int(input("Ingrese 1 o 2: "))
        unAgente = None
        if op == 1:
            unAgente = Docente ('Roberto', 'Sanchez', '23-20194573-7', 38345.3, 3, 'LSI', 'simple', 'Procedural')
        elif op == 2:
            unAgente = Investigador ('Antonio', 'Cassano', '18-38329232-8', 30001.3, 5, 'Tecno', 'OS')

        posicion = int(input("Ingrese la posicion a insertar: "))
        lista.insertarElemento (posicion, unAgente)

    def opcion2 (self, lista):
        print("Ejecutamos la Opcion 2\nAgregar un agente al final de la coleccion\n")
        op = int(input("Ingrese 1 o 2: "))
        unAgente = None
        if op == 1:
            unAgente = DocInvestig ('Fernando', 'Gimenez', '22-40923934-6', 57210.4, 6, 'Cientifica', 'IA', 'LCC', 'semiexclusivo', 'POO', 'II', 2334.2)
        elif op == 2:
            unAgente = PersonalApoyo ('Norelia', 'Correa', '24-31829342-7', 33384.9, 4, 15)

        lista.agregarElemento (unAgente)

    def opcion3 (self, lista):
        print("Ejecutamos la Opcion 3\n")
        pos = int(input("Ingrese una posicion a mostrar: "))
        lista.mostrarElemento(pos)

    def opcion4 (self, lista):
        print("Ejecutamos la Opcion 4\nIngresar una carrera y mostrar listado de agentes que son docentes-investigadores\n")
        lista.mostrarCarreras ()
        carrera = input("Ingrese una carrera: ")
        lista.generarListadoDI (carrera)

    def opcion5 (self, lista):
        print("Ejecutamos la Opcion 5\nContar Cantidad de Docentes-Inv e Investigadores\n")
        lista.mostrarAreasInv ()
        areaInv = input("\nIngrese un area de investigacion: ")
        lista.contarDoc_Inv (areaInv)

    def opcion6 (self, lista):
        print("Ejecutamos la Opcion 6\Mostrar listado ordenado de todos los agentes\n")
        lista.generarListado ()

    def opcion7 (self, lista):
        print("Ejecutamos la Opcion 7\nMostrar listado de Doc-Inv e importe total extra\n")
        lista.mostrarCatInv ()
        cat = input("Ingrese una categoria de investigacion: ")
        lista.calcularTotalExtra (cat)

    def opcion8 (self, lista):
        print("Ejecutamos la Opcion 8\nGuardar informacion de los agentes en archivo JSON\n")
        dicc = lista.toJSON ()
        self.__jsonArch.guardarArchivoJSON (dicc, 'personal.json')
