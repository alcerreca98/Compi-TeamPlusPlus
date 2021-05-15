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
def ingresarTabla(id, type, dict_var):
    temp = funcion.table(id, type, None)
    dirFuncs[id] = temp

#Identificación de tipo de insert
def insert(id, type):
    if isGlobal:
        globalInsert(id, type)
    else:
        varInsert(id, type)

#Insert variable global
def globalInsert(id, type):
    temp = 

#Insert variable local


#Imprime el directorio de funciones: ID | TYPE
def dirPrint():
    for id in dirFuncs:
        print('ID: ', id, ', Type: ', dirFuncs[id].type)

#Imprimir los diccionarios de variables globales: ID | TYPE //Está mal la condición
def dirLocalPrint():
    if(id == 'program'):
        print('ID: ', id, ', Type: ', dict_var[id].type)

#Imprimir los diccionarios de variables locales: ID | TYPE
def dirLocalPrint():
    for id in dict_var:
        print('ID: ', id, ', Type: ', dict_var[id].type)

