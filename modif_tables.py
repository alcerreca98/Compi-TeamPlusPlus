# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------
import sys
from estructuras import *

#Diccionario de funciones
dirFuncs = {}
#Variables globales
programa = ""
tipo = None
auxFunc = ""
tipoMeth = None
dictPrueba = {}

#Contadores
li = 0
lf = 0
lc = 0
lti = 0
ltf = 0
ltc = 0
ltb = 0

def clearVarSize():
    global li
    global lf
    global lc
    global lti
    global ltf
    global ltc
    global ltb
    li = 0
    lf = 0
    lc = 0
    lti = 0
    ltf = 0
    ltc = 0
    ltb = 0

#Insertar datos a tabla de funciones
def ingresarTabla(id, type):
    """ Insertar datos a tabla de funciones """
    #chequeo dobles funciones
    if(repeatedFunctions(id) == False):
        #ingresa la funcion a directorio de Funciones si no se repite
        dirFuncs[id] = funcion(id, type)
    
#Crear e insertar en tabla de variables con chequeo semantico de declaracion doble
def ingresarVariables(id, type):
    """ Crear e insertar en tabla de variables con chequeo semantico de declaracion doble """
    #chequeo contra globales
    if(dirFuncs[programa].repeatedVariables(id) == False):
        #chequeo dobles locales
        if(dirFuncs[auxFunc].repeatedVariables(id) == False):
            #ingresa la variable a la tabla de variables si no se repite
            dirFuncs[auxFunc].addVar(id, type)

#Busca si el nombre de la funcion ya estaba previamente declarado
def repeatedFunctions(id):
    """ Busca si el nombre de la funcion ya estaba previamente declarado """
    repeated = dirFuncs.get(id, False)
    if repeated == False:
        return False
    print("Function : ", id, " already exists")
    sys.exit()
    #for ids in dirFuncs:
    #    if id == ids:
    #        print("Function : ", id, " already exists")
    #        sys.exit()
    #return False

#agrega el tipo de la variable a la lista de Parametros de la funcion
def ingresarParams(type):
    """ agrega el tipo de la variable a la lista de Parametros de la funcion """
    dirFuncs[auxFunc].addParam(type)

#Busca si la variable estaba previamente declarada ya sea en contexto global o local
def checkIfExists(id):
    """ Busca si la variable estaba previamente declarada ya sea en contexto global o local """
    #chequeo existe en globales
    if(dirFuncs[programa].searchIfExists(id) == False):
        #chequeo existe en locales
        if(dirFuncs[auxFunc].searchIfExists(id) == False):
        #si no existe, print el error
            print('Variable :  ', id, " is not previously declared as global nor local in function ",auxFunc)
            sys.exit()
    return True
        #se comprueba que existe y se hace lo demás.

#Imprime el directorio de funciones con sus respectivas tablas de variables y especificando parametros
def dirPrint():
    """ Imprime el directorio de funciones con sus respectivas tablas de variables y especificando parametros """
    for key in dirFuncs:
      dirFuncs[key].printFuncion()
      dirFuncs[key].printVarTable()
      dirFuncs[key].printParams()


