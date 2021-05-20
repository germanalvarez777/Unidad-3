from claseHelado import Helado
from claseSabor import Sabor
class ManejaHelados:
    __listaHelados = None
    def __init__ (self):
        self.__listaHelados = []
    def agregarHelado (self, unHelado):
        self.__listaHelados.append(unHelado)

    #Opcion 1 del Menu- Agregamos una instancia de la clase Helado
    def unaInstanciaH (self, manejSabores):
        gramos = int(input("Ingrese el tipo de Helado(100-150-250-500-1000gr):\n"))
        if ((gramos == 100) or (gramos == 150) or (gramos == 250) or (gramos == 500) or (gramos == 1000)):
            unHelado = Helado (gramos)
            self.agregarHelado(unHelado)
            cantSabores = int(input("Ingrese la cantidad de sabores a agregar: "))
            print("\n---Mostramos el listado de sabores---")
            manejSabores.mostrarSabores()
            for i in range(cantSabores):
                nombre = input("\nIngrese un sabor de helado: ")
                
                #traigo el objeto completo
                unSabor = manejSabores.buscarSabor (nombre)           #buscamos el sabor pedido
                 
                if unSabor != None:
                    unHelado.addSabor(unSabor)
                else:
                    print("El sabor ingresado no es correcto\n")
        else:
            print("El tipo de Helado ingresado no es valido\n")


    #metodo opcion2 - contar los pedidos por sabor 
    def saboresMasPedidos (self, manejSabores):
        sabores_pedidos = [0 for i in range (len(manejSabores.getLista()))]
        for helado in self.__listaHelados:
            for sabor in helado.getSabores():                               #cada sabor de cada lista de sabores en un helado
                #nrosabor = manejSabores.buscarNumero (sabor.getNombre())
                nrosabor = sabor.getNumeroSabor()
                if nrosabor != None:
                    sabores_pedidos[nrosabor-1] += 1                #-1 por ser lista con indice 0
        
        return sabores_pedidos

    def totalGrVendidos (self, nrosabor):                   #metodo de opcion3
        acum = 0
        for helado in self.__listaHelados:
            for sabor in helado.getSabores():
                if (sabor.getNumeroSabor() == nrosabor):
                    acum += int(helado.getGramos()/len(helado.getSabores()))
        
        return acum

    
    def saboresVendidos (self, tipoh):                      #metodo de opcion4
        print("Los sabores vendidos son: \n")
        for helado in self.__listaHelados:
            if (helado.getGramos() == tipoh):
                for sabor in helado.getSabores():
                    print("Nombre del Sabor: {}".format(sabor.getNombre()))

    def mostrarHelados (self):
        for helado in self.__listaHelados:
            print("=".center(50,'='))
            helado.mostrarHelado()
