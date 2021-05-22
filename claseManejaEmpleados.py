import csv
import numpy as np
import re
from claseEmpleado import Empleado
from clasePlanta import Planta
from claseContratado import Contratado
from claseExterno import Externo
from claseFechaHora import FechaHora
class ManejaEmpleados:
    __cantidad = 0
    __dimension = 0
    __incremento = 0
    def __init__ (self, tamañoTeclado=0, incremento=0):
        self.__dimension = tamañoTeclado
        self.__incremento = incremento
        self.__cantidad = 0
        self.__empleados = np.empty (self.__dimension, dtype=Empleado)

    def agregarEmpleado (self, unEmpleado):
        if isinstance (unEmpleado, Empleado):           #nos aseguramos que recibimos una instancia de clase o subclase Empleado
            if (self.__cantidad == self.__dimension):
                self.__dimension += self.__incremento
                self.__empleados.resize (self.__dimension)

            self.__empleados[self.__cantidad] = unEmpleado
            self.__cantidad += 1
        else:
            print("La instancia recibida no pertenece ala clase Empleado!\n") 
    
    def testEmpleadoPlanta (self):
        archivo = open ('planta.csv', 'r')
        Reader = csv.reader (archivo, delimiter=';')
        band = True
        for fila in Reader:
            if band:
                """salteamos cabecera"""
                band = not band
            else:
                #fila[0] es nombre, fila[1] es dni, fila[2] es direccion, fila[3] es telefono, fila[4] sueldo basic, fila[5] antiguedad
                if re.match ('^[\d]', fila[0]):
                    print("Datos de Empleado planta no validos\n")
                else:
                    nom = fila[0]
                    dni = int(fila[1])
                    direcc = fila[2]
                    telef = int(fila[3])
                    sueldoBasic = float(fila[4])
                    antig = int(fila[5])
                    unEmpleado = Planta (nom, dni,direcc,telef,sueldoBasic, antig)
                    self.agregarEmpleado (unEmpleado)
        
        archivo.close()
    
    def testEmpleadoContratado (self):
        archivoC = open ('contratados.csv', 'r')
        Reader = csv.reader (archivoC, delimiter=';')
        band = True
        for fila in Reader:
            if band:
                """salteamos cabecera"""
                band = not band
            else:
                #fila[0] es nombre, fila[1] es dni, fila[2] es direccion, fila[3] es telefono, fila[4] fechaInicio, fila[5] fechafin, fila[6] es cantidad de horas
                if re.match ('^[\d]', fila[0]):
                    print("Datos de Empleado Contratado no validos\n")
                else:
                    nom = fila[0]
                    dni = int(fila[1])
                    direcc = fila[2]
                    telef = int(fila[3])
                    
                    fechaIn = fila[4]
                    i = fechaIn.find('/')
                    j = fechaIn.rfind('/')
                    if i != None and j != None:
                        dia = int(fechaIn[:i])
                        mes = int(fechaIn[i+1:j])
                        anio = int(fechaIn[j+1:])
                        #print("1-dia:{} , mes: {}, anio: {}".format(dia, mes, anio))
                        fInicio = FechaHora (dia,mes,anio)
                        fInicio.validar()
                    
                    fechaFin = fila[5]
                    i = fechaFin.find('/')
                    j = fechaFin.rfind('/')
                    if i != None and j != None:
                        dia = int(fechaFin[:i])
                        mes = int(fechaFin[i+1:j])
                        anio = int(fechaFin[j+1:])
                        #print("2-dia:{} , mes: {}, anio: {}".format(dia, mes, anio))
                        fFin = FechaHora (dia,mes,anio)
                        fFin.validar()

                    cantHoras = int(fila[6])
                    unEmpleado = Contratado (nom, dni,direcc,telef, fInicio, fFin, cantHoras)
                    self.agregarEmpleado (unEmpleado)
        
        archivoC.close()
    
    def testEmpleadoExterno (self):
        archivoE = open ('externos.csv', 'r')
        Reader = csv.reader (archivoE, delimiter=';')
        band = True
        for fila in Reader:
            if band:
                """salteamos cabecera"""
                band = not band
            else:
                #fila[0] es nombre, fila[1] es dni, fila[2] es direccion, fila[3] es telefono, fila[4] es tarea , fila[5] es fechaInic, fila[6] es fechaFin, fila[7] es viatico, fila[8] costoObra, fila[9] seguro de vida
                if re.match ('^[\d]', fila[0]):
                    print("Datos de Empleado Externo no validos\n")
                else:
                    nom = fila[0]
                    dni = int(fila[1])
                    direcc = fila[2]
                    telef = int(fila[3])
                    tarea = fila[4]
                    #creamos el atributo que es una instancia de la clase FechaHora
                    fechaIn = fila[5]
                    i = fechaIn.find('/')
                    j = fechaIn.rfind('/')
                    if i != None and j != None:
                        dia = int(fechaIn[:i])
                        mes = int(fechaIn[i+1:j])
                        anio = int(fechaIn[j+1:])
                        #print("1-dia:{} , mes: {}, anio: {}".format(dia, mes, anio))
                        fInicio = FechaHora (dia,mes,anio)
                        fInicio.validar()
        
                    fechafin = fila[6]
                    i = fechafin.find('/')
                    j = fechafin.rfind('/')
                    if i != None and j != None:
                        dia = int(fechafin[:i])
                        mes = int(fechafin[i+1:j])
                        anio = int(fechafin[j+1:])
                        #print("2-dia:{} , mes: {}, anio: {}".format(dia, mes, anio))
                        fFin = FechaHora (dia,mes,anio)
                        fFin.validar()

                    viatico = float(fila[7])
                    costoOb = float(fila[8])
                    seguro = float(fila[9])                    
                    unEmpleado = Externo (nom, dni,direcc,telef,fInicio, fFin, tarea,viatico,costoOb, seguro)
                    self.agregarEmpleado (unEmpleado)
        
        archivoE.close()
    
    def mostrarEmpleados (self):
        #metodo mostrar es generico de la clase padre, despues lo vuelvo a definir para cada subclase
        print("----Mostramos el listado de Empledos----\n")
        for i in range(self.__cantidad):
            self.__empleados[i].mostrar()

    #apartado 1
    def incrementarHoras (self, doc, canth):
        band = False
        i = 0
        while (i < (self.__cantidad) and band == False):
            if (self.__empleados[i].getDniEmp() == doc):
                if isinstance(self.__empleados[i], Contratado):         #el empleado es de tipo contratado
                    band = True
                    self.__empleados[i].setCantHoras (canth)
                    print("La persona {} incremento sus horas de trabajo".format(self.__empleados[i].getNomEmp()))
                else:
                    print("La persona ingresada no es un empleado de tipo Contratado\n")
            i += 1
    
    #apartado2 
    def mostrarTotalExterno (self, nomtarea, fechaActual):
        acum = 0
        for i in range(self.__cantidad):
            if isinstance (self.__empleados[i], Externo):
                if (self.__empleados[i].getTarea() == nomtarea.lower()):
                    
                    #print("1-fecha actual: ", fechaActual.mostrarFecha(), "fechafin: ", self.__empleados[i].getFechaFinExt().mostrarFecha())
                    #print("Valor de la comp: ", self.__empleados[i].getFechaFinExt() > fechaActual)
                    
                    if (self.__empleados[i].getFechaFinExt() > fechaActual):         #tarea no finalizada
                        acum += self.__empleados[i].getSueldo()
        if (acum > 0):
            print("Para la tarea: {}, el monto a pagar es {:.2f}".format(nomtarea, acum))
        else:
            print("La tarea {} ya ha sido finalizada!".format(nomtarea))

    #apartado3 - metodo getsueldo es de clase padre, aplicamos polimorfismo para cada subclase
    def ayudaEmpleados (self):
        print("El listado de personas que necesitan ayuda son\n")
        print("Nombre           DNI         Direccion\n")
        for i in range(self.__cantidad):
            if (self.__empleados[i].getSueldo() < 25000):
                print("{:8} {:8} {:8}\n".format(self.__empleados[i].getNomEmp(), self.__empleados[i].getDniEmp(), self.__empleados[i].getDireccionEmp()))