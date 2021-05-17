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

#Insertar datos a tabla de funciones, no contiene el diccionario
def ingresarTabla(id, type):
    dirFuncs[id] = funcion(id, type)

def ingresarVariables(id,type):
    dirFuncs[auxFunc].addVar(id, type)

#Imprime el directorio de funciones: ID | TYPE
def dirPrint():
    for key in dirFuncs:
      dirFuncs[key].printFuncion()
      dirFuncs[key].printVarTable()


