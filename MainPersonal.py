import os
from ListaPersonalUniv import ListaPersonalUniv

from clasePersonal import Personal
from claseDocente import Docente
from claseInvestigador import Investigador
from PersonalApoyo import PersonalApoyo
from claseDocInvestig import DocInvestig

from claseObjectEncoderP import ObjectEncoderP
from claseMenuPersonal import MenuPersonal


def testPrueba ():
    listaTest = ListaPersonalUniv()
    unAgente = Docente ('Roberto', 'Sanchez', '23-20194573-7', 38345.3, 3, 'LSI', 'simple', 'Procedural')
    listaTest.insertarElemento(0, unAgente)
    otroAgente = Investigador ('Antonio', 'Cassano', '18-38329232-8', 30001.3, 5, 'Tecno', 'OS')
    listaTest.agregarElemento(otroAgente)
    agen1 = DocInvestig ('Fernando', 'Gimenez', '22-40923934-6', 57210.4, 6, 'Cientifica', 'IA', 'LCC', 'semiexclusivo', 'POO', 'II', 2334.2)
    listaTest.agregarElemento(agen1)
    agen2 = PersonalApoyo ('Norelia', 'Correa', '24-31829342-7', 33384.9, 4, 15)
    listaTest.insertarElemento(1,agen2)
    
    for dato in listaTest:
        dato.mostrarDatos()

def cargarLista():
    try:                #si ya existe el archivo json cargado
        jsonArchivo = ObjectEncoderP()
        dicc = jsonArchivo.leerArchivoJSON ('personal.json')
        lista = jsonArchivo.decodificarDicc (dicc)
        print("Lista NO vacia cargada\n")
        print(lista)
        return lista
    except:                
        lista = ListaPersonalUniv()
        print("Lista vacia creada\n")
        return lista

if __name__ == '__main__':

    testPrueba()
    input("Ha finalizado el test de prueba, presione una tecla para continuar: \n")
    lista = cargarLista()
    menu = MenuPersonal()
    salir = True
    while salir:
        print("""
        ====================================================================
        1 - Insertar a agentes a la colección.
        2 - Agregar agentes a la colección.
        3 - Mostrar agente que se encuentra en la coleccion por posicion.
        4 - Ingresar una carrera y mostrar listado de agentes que son docentes-investigadores. 
        5 - Ingresar area de investig, y contar la cantidad de agentes Doc-Inv e investigaciones.
        6 - Generar listado de todos los agentes ordenados por apellido.
        7 - Generar listado de Doc-Investig y mostrar el total de importe extra a solicitar.
        8 - Almacenar los datos de todos los agentes en archivo JSON.
        9 - Salir.
        ====================================================================\n
        """)
        op = input("Ingrese una opcion: ")
        os.system ('clear')
        if ((op != '1') and (op != '2') and (op != '3') and (op != '4') and (op != '5') and (op != '6') and (op != '7') and (op != '8') and (op != '9')):
            print("Opcion no valida!")
            salir = not salir
        else:
            if (op == '9'):
                menu.salir(lista)
                salir = not salir
            else:
                menu.opcion(op, lista)
