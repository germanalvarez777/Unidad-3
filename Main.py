from ArregloTallerCapac import ArrayTC
from ManejaPersona import ManejaPersona
from ManejaInscripcion import ManejaInscripcion

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
    testClaseAsociacion()