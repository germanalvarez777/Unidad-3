from claseManejaLibros import ManejaLibros
from claseMenuLibros import MenuLibros
def test ():
    ml = ManejaLibros()
    ml.testListaLibros()
    print("Mostramos el listado de libros: \n")
    ml.mostrarListaLibros()
    prueba = input("Desea probar la composicion del ManejaLibros?(s/n): ")
    if (prueba == 's'):
        ml.probarComposicion()

if __name__ == '__main__':
    menu = MenuLibros ()
    band = True
    test()
    input("Ha finalizado el testeo de datos, presione una tecla para continuar\n")
    while band:
        print("""
        a - Ingresar un identificador de libro y mostrar su informacion. 
        b - Ingresar una palabra y mostrar el titulo o capitulo que coincide.
        c - Salir
        """)
        opcion = input("Ingrese una opcion: ")
        if ((opcion != 'a') and (opcion != 'b') and (opcion != 'c')):
            print("Opcion no valida")
            band = False
        else:
            if (opcion == 'c'):
                menu.salir()
                band = False
            else:
                menu.opcion(opcion)