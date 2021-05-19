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

#Insertar datos a tabla de funciones, no contiene el diccionario
def ingresarTabla(id, type):
    #chequeo dobles funciones
    if(repeatedFunctions(id) == False):
        #ingresa la funcion a directorio de Funciones si no se repite
        dirFuncs[id] = funcion(id, type)
    

def ingresarVariables(id,type):
    #chequeo contra globales
    if(dirFuncs[programa].repeatedVariables(id) == False):
        #chequeo dobles locales
        if(dirFuncs[auxFunc].repeatedVariables(id) == False):
            #ingresa la variable a la tabla de variables si no se repite
            dirFuncs[auxFunc].addVar(id, type)

def repeatedFunctions(id):
    for ids in dirFuncs:
        if id == ids:
            print("Function : ", id, " already exists")
            sys.exit()
            return True
    return False

def ingresarParams(id):
    dirFuncs[auxFunc].addParam(id)

def checkIfExists(id):
    #chequeo existe en globales
    if(dirFuncs[programa].searchIfExists(id) == False):
        #chequeo existe en locales
        if(dirFuncs[auxFunc].searchIfExists(id) == False):
        #si no existe, print el error
            print('Variable :  ', id, " is not previously declared as global nor local in function ",auxFunc)
            sys.exit()
    else :
        return True
        #se comprueba que existe y se hace lo demás.


#Imprime el directorio de funciones: ID | TYPE
def dirPrint():
    for key in dirFuncs:
      dirFuncs[key].printFuncion()
      dirFuncs[key].printVarTable()
      dirFuncs[key].printParams()


