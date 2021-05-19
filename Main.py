from ArregloTallerCapac import ArrayTC
from ManejaPersona import ManejaPersona
from ManejaInscripcion import ManejaInscripcion
import os
from claseMenuTaller import MenuTaller
def testClaseAsociacion ():
    mp = ManejaPersona ()
    mp.testListaPersonas()
    mp.mostrarPersonas()
    listaP = mp.obtenerListaPers()
    
    manejCap = ArrayTC(3,5)
    manejCap.testListaTaller()

    manejInc = ManejaInscripcion(5,5)

    for pers in listaP:
        manejCap.inscribirPersona (pers, manejInc)

    manejCap.mostrarArrayTaller()
    manejInc.mostrarArrayIns()

    print("---Ejecutamos apartado 3---\n")
    manejCap.consultarIns()
    print("\n---Ejecutamos apartado 4---\n")
    manejCap.consultarInscriptos()
    print("\n---Ejecutamos apartado 5---\n")
    mp.mostrarPersonas()
    manejCap.registrarPago(manejInc)

    print("\n---Ejecutamos el apartado 6---\n")
    manejInc.guardarInsCsv()


if __name__ == '__main__':
    ejecutarTest = input("Desea realizar el testeo de datos(s/n): ")
    if ejecutarTest.lower() == 's':
        testClaseAsociacion()
        input("Testeo de datos ya finalizado, presione una tecla para continuar: \n")
    
    salir = True
    menu = MenuTaller()
    while salir:
        print("""
        =======================================================
        1 - Cargar los datos de los talleres.
        2 - Inscribir una persona en un taller.
        3 - Consultar inscripcion.
        4 - Consultar inscriptos.
        5 - Registrar pago.
        6 - Guardar inscripciones en un nuevo archivo.
        =======================================================
        """)
        opcion = input("\nIngrese una opcion a ejecutar: ")
        os.system('clear')
        if ((opcion != '1') and (opcion != '2') and (opcion != '3') and (opcion != '4') and (opcion != '5') and (opcion != '6') and (opcion != '7')):
            print("Opcion no valida\n")
            salir = False
        else:
            if (opcion == '7'):
                menu.salir()
                salir = False
            else:
                menu.opcion(opcion)
