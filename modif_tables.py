# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------
import sys
import estructuras as estructura

#Diccionario de variables locales
lvarTable = {}
#Dicionario de vars globales
gvarTable = {}
#Diccionario de funciones
dirFuncs = {}
#Diccionario de variables auxiliar
dirVarTemp = {}
#Variables globales
isGlobal = True
programa = ""
tipo = None
auxFunc = ""
tipoMeth = None
dictPrueba = {}

#Insertar datos a tabla de funciones, no contiene el diccionario
def ingresarTabla(id, type, dir_var):
    temp = estructura.funcion(id, type, None)
    dirFuncs[id] = temp

def ingresarVariables(id,type):
    temp = estructura.variable(id, type)
    dirVarTemp[id] = temp


#Identificación de tipo de insert
def insert(id, type):
    if isGlobal:
        globalInsert(id, type)
    else:
        varInsert(id, type)

#Insert variable global
def globalInsert(id, type):
    temp = estructura.variable(id, type)



#Insert variable local


#Imprime el directorio de funciones: ID | TYPE
def dirPrint():
    for id in dirFuncs:
        print('ID: ', id, ', Type: ', dirFuncs[id].type)
        temp = dirFuncs[id].dir_var
        for llave in temp:
            print('ID: ', llave, ', Type: ', temp[llave].type)

#Imprimir los diccionarios de variables globales: ID | TYPE //Está mal la condición
def dirLocalPrint():
    if(id == 'program'):
        print('ID: ', id, ', Type: ', dir_var[id].type)

#Imprimir los diccionarios de variables locales: ID | TYPE
def dirLocalPrint():
    for id in dir_var:
        print('ID: ', id, ', Type: ', dir_var[id].type)

