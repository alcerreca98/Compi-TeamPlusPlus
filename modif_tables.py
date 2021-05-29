# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------
import sys
from estructuras import *
import memoriaVirtual as mem

#Diccionario de funciones
dirFuncs = {}
#Variables globales
programa = ""
tipo = None
auxFunc = ""
tipoMeth = None
dictPrueba = {}
dictCte = {}

#contadores ERA
ERAli = 0
ERAlf = 0
ERAlc = 0
ERAlti = 0
ERAltf = 0
ERAltc = 0
ERAltb = 0

#Contadores direcciones
li = -1
lf = -1
lc = -1
lti = -1
ltf = -1
ltc = -1
ltb = -1
gi = 0
gf = 0
gc = 0
cte = 0
pointer = 0



def clearVarSize():
    global li
    global lf
    global lc
    global lti
    global ltf
    global ltc
    global ltb
    global ERAli
    global ERAlf
    global ERAlc
    global ERAlti
    global ERAltf
    global ERAltc
    global ERAltb
    li = -1
    lf = -1
    lc = -1
    lti = -1
    ltf = -1
    ltc = -1
    ltb = -1
    ERAli = 0
    ERAlf = 0
    ERAlc = 0
    ERAlti = 0
    ERAltf = 0
    ERAltc = 0
    ERAltb = 0

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

def addCte(cte_key):
    global cte
    temp = dictCte.get(cte_key,False)
    if(temp == False):
        dir_num = cte + mem.baseCte
        dictCte[cte_key] = dir_num
        cte = cte + 1

def contadorERAlocal(type):
    global ERAli
    global ERAlf
    global ERAlc

    if type == 'int':
        ERAli = ERAli +1
    elif type == 'float':
        ERAlf = ERAlf +1
    elif type == 'char':
        ERAlc = ERAlc +1
    else:
        print("No deberia entrar aqui ERR")

def saltoERAlocal(salto,type):
    global ERAli
    global ERAlf
    global ERAlc

    if type == 'int':
        ERAli = ERAli + salto
    elif type == 'float':
        ERAlf = ERAlf + salto
    elif type == 'char':
        ERAlc = ERAlc + salto

def contadorERAlocalTemporal(type):
    global ERAlti
    global ERAltf
    global ERAltc
    global ERAltb

    if type == 'int':
        ERAlti = ERAlti +1
    elif type == 'float':
        ERAltf = ERAltf +1
    elif type == 'char':
        ERAltc = ERAltc +1
    elif type == 'boolean':
        ERAltb = ERAltb +1
    else:
        print("No deberia entrar aqui ERR")
        print(type)

def ingresaERAifcLocal():
    #Agrega a el tamaño de la funcion, los espacios necesarios de int, float y char locales necesarios
    dirFuncs[auxFunc].tam.append(int(ERAli))
    dirFuncs[auxFunc].tam.append(int(ERAlf))
    dirFuncs[auxFunc].tam.append(int(ERAlc))

def ingresaERAifcLocalTemporal():
    #Agrega a el tamaño de la funcion, los espacios necesarios de int, float, char y boolean temporales necesarios
    dirFuncs[auxFunc].tam.append(int(ERAlti))
    dirFuncs[auxFunc].tam.append(int(ERAltf))
    dirFuncs[auxFunc].tam.append(int(ERAltc))
    dirFuncs[auxFunc].tam.append(int(ERAltb))

def printCteTable():
    x = dictCte.items()
    print(x)

#Imprime el directorio de funciones con sus respectivas tablas de variables y especificando parametros
def dirPrint():
    """ Imprime el directorio de funciones con sus respectivas tablas de variables y especificando parametros """
    for key in dirFuncs:
      dirFuncs[key].printFuncion()
      dirFuncs[key].printVarTable()
      dirFuncs[key].printParams()
    printCteTable()


