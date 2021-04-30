# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------


#class funcion(object):
#    def __init__(self, id, type, vart):
#        self.id = id
#        self.type = type
#        self.vart = vart
#
#class variable(object):
#    def __init__(self, id, type):
#        self.id = id
#        self.type = type
#
#class clases(object):
#    def __init__(self, id, herencia):
#        self.id = id
#        self.herencia = herencia
#
#class objeto(object):
#    def __init__(self, id, type):
#        self.id = id
#        self.type = type
#    
#    def printVar(self):
#        print("id ="+self.id+" tipo= "+self.type)
#    
#    def getType(self):
#        print("id ="+self.id+" tipo= "+self.type)
#        
#    def setType(self):
#        print("id ="+self.id+" tipo= "+self.type)
#    
#funcDir = []
#tablaVars = []
#p1 = variable("iPos","int")
#tablaVars.append(p1)
#p2 = variable("iCont","int")
#tablaVars.append(p2)
#p3 = variable("fTGFA","float")
#tablaVars.append(p3)
#funcDir.append(funcion("Imprime","int",tablaVars))
#
##p1.printVar()
#for ivariable in tablaVars:
#   ivariable.printVar()

# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------
import sys

class funcion(object):
    def __init__(self, id, type):#, vart):
        self.id = id
        self.type = type
#        self.vart = vart

class variable(object):
    def __init__(self, id, type):
        self.id = id
        self.type = type

class clases(object):
    def __init__(self, id, herencia):
        self.id = id
        self.herencia = herencia

class objeto(object):
    def __init__(self, id, type):
        self.id = id
        self.type = type

#Diccionario de variables locales
lvarTable = {}
#Dicionario de vars globales
gvarTable = {}
#diccionario de funciones
dirFuncs = {}

isGlobal = True

#Crea una instancia de Funcion, y la inserta en el directorio de funciones
def insertDF(id, type):
    temp = funcion(id, type)
    dirFuncs[id] = temp

#Func that defines which insert use
def insert(id, type):
    if isGlobal:
        insertGlobal(id, type)
    else:
        insertLocal(id, type)

#Inserts globalvar
def insertGlobal(id, type):
    temp = variable(id, type)
    if len(gvarTable) > 0 and not repeat_gvar(id):
        gvarTable[id] = temp
    if not gvarTable:
        gvarTable[id] = temp

#Insert varibles in local lvarTable
def insertLocal(id, type):
    temp = variable(id, type)
    if len(lvarTable) > 0 and not repeat_lvar(id):
        lvarTable[id] = temp
    if not lvarTable:
        lvarTable[id] = temp

#Semantica, checa id repetidos en tabla de variables globales
def repeat_gvar(id):
    for ids in gvarTable:
        if id == ids:
            print('Id en uso: ', id)
            sys.exit()
            return True
    return False

#Semantica, checa id repetidos en tabla de variables locales
def repeat_lvar(id):
    for ids in lvarTable:
        if id == ids:
            print('Id en uso: ', id)
            sys.exit()
            return True
    return False

#Imprime el directorio de funciones
def dirPrint():
    for ids in dirFuncs:
        print('ID: ', ids, ', Type: ', dirFuncs[ids].type)

#Imprime la tabla de varibales globales
def gvarPrint():
    for ids in gvarTable:
        print('ID: ', ids, ', Type: ', gvarTable[ids].type)

#Imprime la tabla de variables locales
def varsPrint():
    for ids in lvarTable:
        print('ID: ', ids, ', Type: ', lvarTable[ids].type)