class FechaHora:
    __dia = 0
    __mes = 0
    __anio = 0
    __hs = 0
    __min = 0
    __seg = 0
    def __init__ (self, d=1, m=1, a=2020, h=0, mi=0, s=0):    
        self.__dia = d
        self.__mes = m
        self.__anio = a
        self.__hs = h
        self.__min = mi
        self.__seg = s

    def validar (self):
        if ((self.__dia <= 31) and (self.__mes <= 12) and (self.__hs <= 24) and (self.__min < 60) and (self.__seg < 60)):
            if ((self.__dia <= 31) and ((self.__mes == 1) or (self.__mes == 3) or (self.__mes == 5) or (self.__mes == 7) or (self.__mes == 8) or (self.__mes == 10) or (self.__mes == 12))):
                print("{}/{}/{} - hora {}:{}:{} es valido\n".format(self.__dia,self.__mes,self.__anio,self.__hs,self.__min,self.__seg))
            
            elif ((self.__dia <= 30) and ((self.__mes == 4) or (self.__mes == 6) or (self.__mes == 9) or (self.__mes == 11))):
                print("{}/{}/{} - hora {}:{}:{} es valido\n".format(self.__dia,self.__mes,self.__anio,self.__hs,self.__min,self.__seg))
            
            elif ((self.__mes == 2) and (self.__dia <= 29)):
                print("Mes de febrero con dia valido para fecha {}/{}/{} - hora {}:{}:{}\n".format(self.__dia,self.__mes,self.__anio,self.__hs,self.__min,self.__seg))
            else:
                print("{}/{}/{} no es una Fecha valida\n".format(self.__dia, self.__mes,self.__anio))
                self.cambios()
                self.Mostrar()      
        else:
            print("Fecha {}/{}/{} - hora {}:{}:{}  con datos erroneos\n".format(self.__dia,self.__mes,self.__anio,self.__hs,self.__min,self.__seg))
            self.cambios()
            self.Mostrar()
        if ((self.__hs < 0) or (self.__min < 0) or (self.__seg < 0)):
            print("Fecha {}/{}/{} - hora {}:{}:{}  con datos erroneos\n".format(self.__dia,self.__mes,self.__anio,self.__hs,self.__min,self.__seg))
            self.cambios()
            self.Mostrar()

    def Mostrar (self):
        print("Dia: {}, Mes: {}, Anio: {}, Hora: {}, Min: {}, Segundo: {}".format(self.__dia, self.__mes, self.__anio, self.__hs, self.__min, self.__seg))
        print("===".center(50, '='))

    def mostrarFecha (self):
        return str(self.__dia) + '/' + str(self.__mes) + '/' + str(self.__anio)

    def validarBisiesto(self):
        if ((self.__anio  %4 == 0) and (self.__anio % 100 == 0) and (self.__anio % 400 == 0)):
            print("\nEl año {} es biciesto, tiene 366 dias\n".format(self.__anio))
            return True
        else:
            print("\nEl año {} no es biciesto(es Natural), tiene 365 dias\n".format(self.__anio))
            return False

    def cambios (self): 
        bisiesto = self.validarBisiesto()
        if (self.__seg == 60):
            self.__min += 1
            self.__seg = 0
        elif (self.__seg > 60):
            self.__min += self.__seg // 60               #asignamos nuevo valor a min
            self.__seg = self.__seg - 60
        if (self.__min == 60):
            self.__hs += 1
            self.__min = 0
        elif (self.__min > 60):
            self.__hs += self.__min // 60                #asignamos nuevo valor a hora
            self.__min = self.__min - 60
        if (self.__hs == 24):
            self.__dia += 1
            self.__hs = self.__hs- 24
        elif (self.__hs > 24):
            self.__dia += self.__hs // 24                #asignamos nuevo valor a dia
            self.__hs = self.__hs - 24
        if ((self.__dia == 31) and ((self.__mes == 1) or (self.__mes == 3) or (self.__mes == 5) or (self.__mes == 7) or (self.__mes == 8) or (self.__mes == 10) or (self.__mes == 12))):
            self.__mes += 1
            self.__dia = 1
        elif ((self.__dia == 30) and ((self.__mes == 4) or (self.__mes == 6) or (self.__mes == 9) or (self.__mes == 11))):
            self.__mes += 1
            self.__dia = 1
        elif (self.__dia > 31):
            self.__mes += (self.__dia // 30)             #asignamos nuevo valor a mes
            self.__dia = self.__dia - 31
            if (self.__dia > 31):
                self.__mes += (self.__dia // 30)
                self.__dia = self.__dia - 31
        if (self.__mes > 12): 
            self.__anio += 1
            self.__mes = self.__mes - 12
            if (self.__mes > 12):                   #se evalua si el total de meses sigue siendo mayor a 12
                self.__anio += 1
                self.__mes = self.__mes - 12
        if bisiesto:
            if ((self.__dia == 29) and (self.__mes == 2)):
                print("Febrero 29 Biciesto")
                self.__mes += 1
                self.__dia = 1
                self.__hs = 0
        else:
            if ((self.__dia == 28) and (self.__mes == 2)):
                print("Febrero 28 Natural")
                self.__mes += 1
                self.__dia = 1
                self.__hs = 0
        if ((self.__mes == 12) and (self.__dia == 31)):
            self.__anio += 1
            self.__mes = 1
            self.__dia = 1
            self.__hs = 0
            self.__min = 0
            self.__seg = 0

        if (self.__anio < 0):
            print("Fecha con Año no valido")
            self.__anio = 1
        if (self.__dia < 0):
            print("Fecha con Dia no valido")
            self.__dia = 1
        if (self.__mes < 0):
            print("Fecha con Mes no valido")
            self.__mes = 1
        if (self.__hs < 0):
            print("Fecha con Hora no valida")
            self.__hs = 0
        if (self.__min < 0):
            print("Fecha con Minutos no validos")
            self.__min = 0
        if (self.__seg < 0):
            print("Fecha con Segundos no validos")
            self.__seg = 0
                         

    def PonerEnHora (self, h=0, mi=0, s=0):
        if ((h <= 24) and (mi <= 60) and (s <= 60)):
            self.__hs = h
            self.__min = mi
            self.__seg = s
        else:
            print("El horario ingresado es incorrecto\n")   
        self.cambios()

    def AdelantarHora (self, h=0, mi=0):
        if ((h <= 24) and (mi <= 60)):
            self.__hs += h
            self.__min += mi
            self.cambios()
        else:
            print("El horario a adelantar es incorrecto\n")
    
    #A partir de aca, se agregan metodos para el ejercicio 6

    def getDia (self):
        return self.__dia
    def getMes (self):
        return self.__mes
    def getAnio (self):
        return self.__anio
    def getHora (self):
        return self.__hs
    def getMin (self):
        return self.__min
    def getSeg (self):
        return self.__seg
    def __add__ (self, otraFecha):              #opcion 1
        if (type(self) == type(otraFecha)):
            unaFecha = FechaHora (self.__dia+int(otraFecha.getDia()), self.__mes+ int(otraFecha.getMes()), self.__anio+int(otraFecha.getAnio()), self.__hs+int(otraFecha.getHora()), self.__min+int(otraFecha.getMin()), self.__seg+int(otraFecha.getSeg()))
            return unaFecha
        else:
            print("No se puede realizar la Suma de las fechas\n")

    def __gt__ (self, otraFecha):               #(opcion3) retorna true o false
        band = False
        if (type(self) == type(otraFecha)):
            if ((self.__dia == otraFecha.getDia()) and (self.__mes == otraFecha.getMes()) and (self.__anio == otraFecha.getAnio())):
                if (self.__hs > otraFecha.getHora()):
                    band = True
                elif (self.__hs == otraFecha.getHora()):
                    if (self.__min > otraFecha.getMin()):
                        band = True
                    elif (self.__min == otraFecha.getMin()):
                        if (self.__seg > otraFecha.getSeg()):
                            band = True
                        elif (self.__seg == otraFecha.getSeg()):
                            #print("Ambas Fechas son exactamente iguales\n")
                            band = False
                        else:
                            #otraFecha.Mostrar()
                            band = False
                    else:
                        band = False
                else:
                    band = False
            else:
                if (self.__anio > otraFecha.getAnio()):
                    band = True
                elif (self.__anio == otraFecha.getAnio()):
                    if (self.__mes > otraFecha.getMes()):
                        band = True
                    elif (self.__mes == otraFecha.getMes()):
                        if (self.__dia > otraFecha.getDia()):
                            band = True
                        else:                                       #no verificamos que el dia sea igual, sino se ejecuta el if de arriba
                            band = False
                    else:
                        band = False
                else:
                    band = False
            #return (self.__dia>otraFecha.getDia(), self.__mes> otraFecha.getMes(), self.__anio>otraFecha.getAnio(), self.__hs>otraFecha.getHora(), self.__min>otraFecha.getMin(), self.__seg>otraFecha.getSeg())
        
        #else:
        #    print("No se puede realizar la Comparacion de fechas\n")
        return band
        
    def __sub__ (self, otraFecha):              #opcion 2
        if (type(self) == type(otraFecha)):
            #pasamos las dos fechas a segundos
            segDi1 =self.__dia * 86400
            segHora1 = self.__hs * 3600
            segMin1 = (self.__min) * 60
            segMes1 = self.__mes * 2629800                  #Un mes equivale a 2.629.800 segundos
            segAnio1 = self.__anio * 31557600               #Un año equivale a 31.557.600 segundos
            segDi2 = (otraFecha.getDia()) * 86400
            segHora2 = (otraFecha.getHora()) * 3600
            segMin2 = (otraFecha.getMin()) * 60
            segMes2 = (otraFecha.getMes()) * 2629800
            segAnio2 = (otraFecha.getAnio()) * 31557600
            sumaSeg1 = segDi1 + segHora1 + segMin1 + segMes1 + segAnio1 + (self.__seg)
            sumaSeg2 = segHora2 + segMin2 + (otraFecha.getSeg()) + segDi2 + segMes2 + segAnio2
            print("Suma total de segundos para 1era Fecha: {}".format(sumaSeg1))
            print("Suma total de segundos para 2era Fecha: {}".format(sumaSeg2))
            return (sumaSeg1 - sumaSeg2)
        else:
            print("No se puede realizar la Resta de las fechas\n")