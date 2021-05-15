# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------
import sys
import estructuras as table

#Diccionario de variables locales
lvarTable = {}
#Dicionario de vars globales
gvarTable = {}
#Diccionario de funciones
dirFuncs = {}

#Variables globales
isGlobal = True

#Insertar datos a tabla de funciones, no contiene el diccionario
def ingresarTabla(id, type, dict_func):
    temp = funcion(id, type, None)
    dirFuncs[id] = temp

#Imprime el directorio de funciones
def dirPrint():
    for id in dirFuncs:
        print('ID: ', id, ', Type: ', dirFuncs[id].type, ', Diccionario: ', dirFuncs[id].dict_func)
