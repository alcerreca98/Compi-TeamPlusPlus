# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------

import ply.yacc as yacc
import logging
import sys
from lexer import entrada, tokens
import modif_tables as table
import memoriaVirtual as mem
import cuadruplos as cuad
import archCompilado as arc
from estructuras import *

# Gramatica
#No defini starting symbol, pero segun documentacion
#la primera regla gramatical definida toma como default el strating simbol

#! ------------------------------------------------------------
#! Programa, para la estructura general
#! ------------------------------------------------------------
def p_program(p):
    '''
    program : PROGRAM ID initProg SCOLON declarClases declarVar definFunc addGlobSize MAIN auxMain LPAREN RPAREN declarVar LBRACE listaEstatutos RBRACE endProg prueba
    '''

def p_addGlobSize(p):
    '''
    addGlobSize : 
    '''
    table.ingresaTamifcGlobal()

#Introduce el nombre del programa en la tabla de funciones
def p_initProg(p):
    '''
    initProg : 
    '''
    table.ingresarTabla(p[-1], None)
    table.programa = p[-1]
    table.auxFunc = p[-1]
    cuad.quadInsert('Goto', None, None, None)
    cuad.contQuad = cuad.contQuad+1
    table.addCte(0)

#* Como Main no entra como funcion Normal, tenemos que manualmente
#* Agregarlo al directorio de funciones, al contexto, llenarle su cuadruplo inicial
#* y hacer el FILL del cuad 0, para que sepa hacer el salto a Main
def p_auxMain(p):
    '''
    auxMain :
    '''
    table.ingresarTabla("Main", None)
    table.auxFunc = "Main"
    table.dirFuncs[table.auxFunc].fillDI(cuad.contQuad-1)
    cuad.Quad[0].result = cuad.contQuad-1
    #Regresar valor de salto de Main

# TODO: Cuadruplos ENDProgram
#* Como Main no entra como funcion Normal, tenemos que manualmente
#* agregar sus contadores de ERA a su tamaño y borrar su tabla de variables locales
def p_endProg(p):
    '''
    endProg : 
    '''
    temp = table.dirFuncs[table.auxFunc].dir_var
    for id in temp:
        var = temp.get(id)
        tipo = var.getType()
        table.contadorERAlocal(tipo)

    #Agrega a el tamaño de la funcion, los espacios necesarios de int, float y char locales necesarios
    table.ingresaERAifcLocal()
    #Agrega a el tamaño de la funcion, los espacios necesarios de int, float, char y boolean temporales necesarios
    table.ingresaERAifcLocalTemporal()
    #Borrar Tabla de Variables Locales
    table.dirFuncs[table.auxFunc].dir_var.clear()

    #Insertar cuadruplo de fin de funcion
    cuad.quadInsert('ENDProgram', None, None, None)
    cuad.contQuad = cuad.contQuad + 1
    
    #Reinicio contadores
    table.clearVarSize()

#! ------------------------------------------------------------
#! Declaracion de Clases
#! ------------------------------------------------------------
def p_declarClases(p):
    '''
    declarClases : CLASS ID herencia LBRACE ATTRIBUTES declarAttributes METHODS declarMethods RBRACE declarClases
                 | empty
    '''

#la Herencia es opcional
def p_herencia(p):
    '''
    herencia : LT EXTENDS ID GT
             | empty
    '''

#atributos de clase, opcionales
def p_declarAttributes(p):
    '''
    declarAttributes : tipo COLON listaIdDeclare SCOLON declarAttributes
                     | empty
    '''

#! ------------------------------------------------------------
#! Declaracion de Variables, Arreglos, Matrices
#! ------------------------------------------------------------
#iterador de idDeclare separado por comma
def p_listaIdDeclare(p):
    '''
    listaIdDeclare : idDeclare  
                   | idDeclare COMMA listaIdDeclare
    '''

#sintaxis de declaración de variables
def p_idDeclare(p):
    '''
    idDeclare : ID auxDeclare auxDeclare2
              | ID auxDeclare LBRACK CTE_I addCteTable RBRACK auxCTE 
              | ID auxDeclare LBRACK CTE_I addCteTable COMMA CTE_I addCteTable auxCTE2 RBRACK
    '''

#*con chequeos semanticos de doble declaracion
def p_auxDeclare(p):
    '''
    auxDeclare :
    '''
    table.ingresarVariables(p[-1], table.tipo)

def p_auxDeclare2(p):
    '''
    auxDeclare2 :
    '''
    if table.auxFunc == table.programa:
        temp = cuad.getAvailGlobal(table.tipo)
        table.dirFuncs[table.auxFunc].dir_var[p[-2]].dir = temp
    else:
        temp = cuad.getAvailLocal(table.tipo)
        table.dirFuncs[table.auxFunc].dir_var[p[-2]].dir = temp

#* con chequeo semanticos para arreglos y matrices
#* dimensiones deben de ser mayores a 0 
def p_auxCTE(p):
    '''
    auxCTE :
    '''
    if(p[-3] > 0) :
        table.dirFuncs[table.auxFunc].dir_var[p[-6]].dim.append(p[-3])
        if table.auxFunc == table.programa:
            temp = cuad.getAvailGlobal(table.tipo)
            table.dirFuncs[table.auxFunc].dir_var[p[-6]].dir = temp
            table.addCte(temp)
            cuad.setSaltoGlobal(p[-3]-1, table.tipo)
        else:
            temp = cuad.getAvailLocal(table.tipo)
            table.dirFuncs[table.auxFunc].dir_var[p[-6]].dir = temp
            table.addCte(temp)
            cuad.setSaltoLocal(p[-3]-1, table.tipo)
            table.saltoERAlocal(p[-3]-1, table.tipo)
    else:
        print("ERROR: Valor de dimensión inválido, debe ser mayor a 0")
        sys.exit()

def p_auxCTE2(p):
    '''
    auxCTE2 :
    '''
    if(p[-5] > 0 and p[-2] > 0) :
        table.dirFuncs[table.auxFunc].dir_var[p[-8]].dim.append(p[-5])
        table.dirFuncs[table.auxFunc].dir_var[p[-8]].dim.append(p[-2])
        auxSalto = p[-5] * p[-2] -1
        if table.auxFunc == table.programa:
            temp = cuad.getAvailGlobal(table.tipo)
            table.dirFuncs[table.auxFunc].dir_var[p[-8]].dir = temp
            table.addCte(temp)
            cuad.setSaltoGlobal(auxSalto, table.tipo)
        else:
            temp = cuad.getAvailLocal(table.tipo)
            table.dirFuncs[table.auxFunc].dir_var[p[-8]].dir = temp
            table.addCte(temp)
            cuad.setSaltoLocal(auxSalto, table.tipo)
            table.saltoERAlocal(auxSalto, table.tipo)
    else:
        print("ERROR: Valor de dimensión inválido, debe ser mayor a 0")
        sys.exit()

#! ------------------------------------------------------------
#! Llamada de Variables, Arreglos, Matrices, Atributos de clase
#! ------------------------------------------------------------
#sintaxis para indexación o llamada de variables
def p_idCall(p):
    '''
    idCall : ID idCallaux checkDim
           | ID idCallaux DOT ID
           | ID idCallaux LBRACK addFF exp RBRACK rmFF idCallaux4 checkDim1
           | ID idCallaux LBRACK addFF exp idCallaux2  rmFF COMMA addFF exp idCallaux3 RBRACK rmFF checkDim2
    '''
    
def p_idCallaux(p):
    '''
    idCallaux : 
    '''
    if(table.checkIfExists(p[-1])):
        condicion = table.dirFuncs[table.programa].searchIfExists(p[-1])
        if(condicion == False):
            var = table.dirFuncs[table.auxFunc].searchIfExists(p[-1])
        else:
            var = table.dirFuncs[table.programa].searchIfExists(p[-1])
        #cuad.pushPilaO(p[-1])
        cuad.pushPilaO(var.dir)
        cuad.pushType(var.getType())

# TODO: Cuadruplos VER de arreglos y matrices
def p_idCallaux2(p):
    '''
    idCallaux2 : 
    '''
    condicion = table.dirFuncs[table.programa].searchIfExists(p[-5])
    if(condicion == False):
        limInf = table.dictCte[0]
        limSup = table.dictCte[table.dirFuncs[table.auxFunc].dir_var[p[-5]].dim[0]]
    else:
        limInf = table.dictCte[0]
        limSup = table.dictCte[table.dirFuncs[table.programa].dir_var[p[-5]].dim[0]]
    resultExp = cuad.PilaO[-1]
    cuad.quadInsert("VER", resultExp, limInf, limSup)
    cuad.contQuad = cuad.contQuad + 1

def p_idCallaux3(p):
    '''
    idCallaux3 : 
    '''
    condicion = table.dirFuncs[table.programa].searchIfExists(p[-10])
    if(condicion == False):
        limInf = table.dictCte[0]
        limSup = table.dictCte[table.dirFuncs[table.auxFunc].dir_var[p[-10]].dim[1]]
        dim1 = table.dictCte[table.dirFuncs[table.auxFunc].dir_var[p[-10]].dim[0]]
        dirBase = table.dirFuncs[table.auxFunc].dir_var[p[-10]].dir
    else:
        limInf = table.dictCte[0]
        limSup = table.dictCte[table.dirFuncs[table.programa].dir_var[p[-10]].dim[1]]
        dim1 = table.dictCte[table.dirFuncs[table.programa].dir_var[p[-10]].dim[0]]
        dirBase = table.dirFuncs[table.programa].dir_var[p[-10]].dir
    resultExp2 = cuad.PilaO.pop()
    result_type2 = cuad.Ptypes.pop()
    resultExp1 = cuad.PilaO.pop()
    result_type = cuad.Ptypes.pop()
    if (result_type2 == 'int' and result_type == 'int'):
        acceso = table.accessPointer + mem.basePointer
        table.accessPointer = table.accessPointer +1
        cuad.quadInsert("VER", resultExp2, limInf, limSup)
        cuad.contQuad = cuad.contQuad + 1
        #desplazamiento = resultExp2*dim1+resultExp1
        temp = cuad.getAvail('int')
        table.contadorERAlocalTemporal('int')
        cuad.quadInsert('*',resultExp2, dim1, temp)
        cuad.contQuad = cuad.contQuad + 1
        temp2 = cuad.getAvail('int')
        table.contadorERAlocalTemporal('int')
        cuad.quadInsert('+',temp, resultExp1, temp2)
        cuad.contQuad = cuad.contQuad + 1
        cuad.quadInsert('+',temp2, dirBase, acceso)
        cuad.contQuad = cuad.contQuad + 1

        cuad.PilaO.pop()
        cuad.Ptypes.pop()

        cuad.pushPilaO(acceso)
        cuad.pushType(result_type)

    else:
        print("ERROR : No se puede accesar a un arreglo/Matriz en indice diferente a integer")
        sys.exit()

def p_idCallaux4(p):
    '''
    idCallaux4 : 
    '''
    condicion = table.dirFuncs[table.programa].searchIfExists(p[-7])
    if(condicion == False):
        limInf = table.dictCte[0]
        limSup = table.dictCte[table.dirFuncs[table.auxFunc].dir_var[p[-7]].dim[0]]
        dirBase = table.dirFuncs[table.auxFunc].dir_var[p[-7]].dir
    else:
        limInf = table.dictCte[0]
        limSup = table.dictCte[table.dirFuncs[table.programa].dir_var[p[-7]].dim[0]]
        dirBase = table.dirFuncs[table.programa].dir_var[p[-7]].dir
    resultExp = cuad.PilaO.pop()
    result_type = cuad.Ptypes.pop()
    #resultExp = cuad.PilaO[-1]
    #result_type = cuad.Ptypes[-1]
    if result_type == 'int':
        acceso = table.accessPointer + mem.basePointer
        table.accessPointer = table.accessPointer +1
        cuad.quadInsert("VER", resultExp, limInf, limSup)
        cuad.contQuad = cuad.contQuad + 1
        desplazamiento = resultExp
        cuad.quadInsert('+',desplazamiento, dirBase, acceso)
        cuad.contQuad = cuad.contQuad + 1

        cuad.PilaO.pop()
        cuad.Ptypes.pop()

        cuad.pushPilaO(acceso)
        cuad.pushType(result_type)
    else:
        print("ERROR : No se puede accesar a un arreglo/Matriz en indice diferente a integer")
        sys.exit()

def p_checkDim(p):
    '''
    checkDim : 
    '''
    condicion = table.dirFuncs[table.programa].searchIfExists(p[-2])
    if(condicion == False):
        dim = len(table.dirFuncs[table.auxFunc].dir_var[p[-2]].dim)
    else:
        dim = len(table.dirFuncs[table.programa].dir_var[p[-2]].dim)
    
    if dim > 0 :
        print("ERROR: en la funcion \"", table.auxFunc, "\" var: ",p[-2], " debe ser dimensionada")
        sys.exit()

def p_checkDim1(p):
    '''
    checkDim1 : 
    '''
    condicion = table.dirFuncs[table.programa].searchIfExists(p[-8])
    if(condicion == False):
        dim = len(table.dirFuncs[table.auxFunc].dir_var[p[-8]].dim)
    else:
        dim = len(table.dirFuncs[table.programa].dir_var[p[-8]].dim)
    
    if dim == 0 :
        print("ERROR: en la funcion \"", table.auxFunc, "\" var: ",p[-8], " declarada como no dimensionada, demasiados parametros")
        sys.exit()
    elif dim == 2 :
        print("ERROR: en la funcion \"", table.auxFunc, "\" var: ",p[-8], " declarada con 2 dimensiones, faltan parametros")
        sys.exit()    

def p_checkDim2(p):
    '''
    checkDim2 : 
    '''
    condicion = table.dirFuncs[table.programa].searchIfExists(p[-13])
    if(condicion == False):
        dim = len(table.dirFuncs[table.auxFunc].dir_var[p[-13]].dim)
    else:
        dim = len(table.dirFuncs[table.programa].dir_var[p[-13]].dim)
    
    if dim == 0 :
        print("ERROR: en la funcion \"", table.auxFunc, "\" var: ",p[-13], " declarada como no dimensionada, demasiados parametros")
        sys.exit()
    elif dim == 1 :
        print("ERROR: en la funcion \"", table.auxFunc, "\" var: ",p[-13], " declarada con una sola dimension, demasiados parametros")
        sys.exit()    
#! ------------------------------------------------------------
#! Tipos de Variables, vs tipos de Retorno de Funcion/Metodo
#! ------------------------------------------------------------
#tipo de variables
def p_tipo(p):
    '''
    tipo : ID
         | INT
         | FLOAT
         | CHAR
    '''
    table.tipo = p[1]

#tipo de metodos y funciones
def p_tipoMethod(p):
    '''
    tipoMethod : VOID
               | INT
               | FLOAT
               | CHAR
    '''
    table.tipoMeth = p[1]

#! ------------------------------------------------------------
#! Declaración de Métodos de Clase
#! ------------------------------------------------------------
# Metodos de la clase, opcionales
def p_declarMethods(p):
    '''
    declarMethods : tipoMethod FUNC ID LPAREN listaParam RPAREN LBRACE listaEstatutos RBRACE declarMethods
                  | empty
    '''

#! ------------------------------------------------------------
#! Declaración de Parametros
#! ------------------------------------------------------------
#Para parametros, en declaracion de metodos o funciones, arreglos y matrices van con exp o con CTE_I
def p_listaParam(p):
    '''
    listaParam : param
               | param COMMA listaParam
               | empty
    '''

#sintaxis de declaracion de parametros
def p_param(p):
    '''
    param : tipo COLON ID
    '''
    table.ingresarVariables(p[3], table.tipo)
    table.ingresarParams(table.tipo)
    temp = cuad.getAvailLocal(table.tipo)
    table.dirFuncs[table.auxFunc].dir_var[p[3]].dir = temp

#! ------------------------------------------------------------
#! Declaración de Variables
#! ------------------------------------------------------------
def p_declarVar(p):
    '''
    declarVar : VAR tipo COLON listaIdDeclare SCOLON declarVar
              | empty
    '''

#! ------------------------------------------------------------
#! Definicion de Funciones
#! ------------------------------------------------------------
def p_definFunc(p):
    '''
    definFunc : tipoMethod FUNC ID auxFuncion LPAREN listaParam RPAREN declarVar setDI LBRACE listaEstatutos RBRACE endF definFunc
              | empty
    '''

#guarda en el directorio de funciones la nueva instancia de funcion, con su nombre y tipo
def p_auxFuncion(p):
    '''
    auxFuncion :
    '''
    table.auxFunc = p[-1]
    table.ingresarTabla(table.auxFunc, table.tipoMeth)
    if(table.tipoMeth!='void'):
        table.contadorERAglobal(p_tipoMethod)
        table.dirFuncs[table.programa].addVar(table.auxFunc, table.tipoMeth)
        temp = cuad.getAvailGlobal(table.tipoMeth)
        table.dirFuncs[table.programa].dir_var[table.auxFunc].dir = temp

#guarda el cuadruplo inicial de la funcion
def p_setDI(p):
    '''
    setDI :
    '''
    temp = table.dirFuncs[table.auxFunc].dir_var
    for id in temp:
        var = temp.get(id)
        tipo = var.getType()
        table.contadorERAlocal(tipo)

    #llena el cuadruplo inicial de la funcion
    table.dirFuncs[table.auxFunc].fillDI(cuad.contQuad-1)
    #Agrega a el tamaño de la funcion, los espacios necesarios de int, float y char locales necesarios
    table.ingresaERAifcLocal()

# TODO: Cuadruplos ENDFunc
def p_endF(p):
    '''
    endF :
    '''
    #Borrar Tabla de Variables Locales
    table.dirFuncs[table.auxFunc].dir_var.clear()

    #Insertar cuadruplo de fin de funcion
    cuad.quadInsert('ENDFunc', None, None, None)
    cuad.contQuad = cuad.contQuad + 1
    #Agrega a el tamaño de la funcion, los espacios necesarios de int, float, char y boolean temporales necesarios
    table.ingresaERAifcLocalTemporal()

    #table.dirFuncs[table.auxFunc].printSize()
    #Reinicio contadores
    table.clearVarSize()

#! ------------------------------------------------------------
#! Estatutos
#! ------------------------------------------------------------
def p_listaEstatutos(p):
    '''
    listaEstatutos : estatutos listaEstatutos
                   | empty
    '''

def p_estatutos(p):
    '''
    estatutos   : llamada SCOLON
                | asignacion SCOLON
                | returnf SCOLON
                | lectura SCOLON
                | escritura SCOLON
                | condicion 
                | cond_w
                | cond_f
    '''

#! ------------------------------------------------------------
#! Asignaicon
#! ------------------------------------------------------------
def p_asignacion(p):
    '''
    asignacion  : idCall ASIGNA pushPoper exp asignStep2 
    '''

#* asignStep1 es pushPoper()

def p_asignStep2(p):
    '''
    asignStep2  :
    '''
    if (cuad.asignaStep2() == True):
        cuad.contQuad = cuad.contQuad + 1

#! ------------------------------------------------------------
#! Llamada de Funciones
#! ------------------------------------------------------------
def p_llamada(p):
    '''
    llamada   : ID DOT ID LPAREN enviaParam RPAREN
              | ID verExist LPAREN enviaParam coherenceGo RPAREN 
    '''

def p_enviaParam(p):
    '''
    enviaParam  : paramReferencia
                | empty
    '''

def p_paramReferencia(p):
    '''
    paramReferencia : exp paramType
                    | exp paramType COMMA paramCount paramReferencia
    '''

# TODO: Cuadruplos ERA
#* con chequeo semantico de que la funcion este previamente declarada
def p_verExist(p):
    '''
    verExist :
    '''
    exist = table.dirFuncs.get(p[-1], False)
    if(exist == False):
        print("ERROR : la funcion \"", p[-1] ,"\" no esta previamente declarada")
        sys.exit()
    
    cuad.quadInsert('ERA', None, None, p[-1])
    cuad.contQuad = cuad.contQuad + 1
    cuad.paramK = 1
    cuad.pointerParam = p[-1]

# TODO: Cuadrupos PARAM
#* con chequeo semantico en numero de parametros y sus tipos
def p_paramType(p):
    '''
    paramType :
    '''
    arg = cuad.PilaO.pop()
    arg_type = cuad.Ptypes.pop()
    params = table.dirFuncs[cuad.pointerParam].params
    tam = len(params)
    if(cuad.paramK > tam):
        print("ERROR: mas parametros de los esperados")
        sys.exit()
    tipo = table.dirFuncs[cuad.pointerParam].params[cuad.paramK-1]
    #num = "Par"+str(cuad.paramK)
    num = cuad.paramK
    if(arg_type == tipo):
        cuad.quadInsert('PARAM', arg, None , num)
        cuad.contQuad = cuad.contQuad + 1
    else:
        print("ERROR: type mismatch de parametros en llamada", cuad.pointerParam)
        sys.exit()

def p_paramCount(p):
    '''
    paramCount :
    '''
    cuad.paramK = cuad.paramK+1

# TODO: Cuadrupos GOSUB
def p_coherenceGo(p):
    '''
    coherenceGo :
    '''
    params = table.dirFuncs[cuad.pointerParam].params
    tam = len(params)
    if(cuad.paramK < tam):
        print("ERROR: faltaron parametros")
        sys.exit()
    cuad.quadInsert('GOSUB', None, None , cuad.pointerParam)
    cuad.contQuad = cuad.contQuad + 1
    #Parche Guadalupano
    tipoRet = table.dirFuncs[cuad.pointerParam].type
    if(tipoRet != 'void'):
        Guadalupano = cuad.getAvail(tipoRet)
        table.contadorERAlocalTemporal(tipoRet)
        func = table.dirFuncs[table.programa].dir_var.get(cuad.pointerParam)
        funcDir= func.dir
        cuad.quadInsert('=', funcDir, None , Guadalupano)
        cuad.pushPilaO(Guadalupano)
        cuad.pushType(tipoRet)
        cuad.contQuad = cuad.contQuad + 1

#! ------------------------------------------------------------
#! Return
#! ------------------------------------------------------------
def p_returnf(p):
    '''
    returnf   : RETURN pushPoper LPAREN exp RPAREN popReturn
    '''

def p_popReturn(p):
    '''
    popReturn   : 
    '''
    temp = cuad.popReturn()
    if temp:
        cuad.contQuad = cuad.contQuad + 1 

#! ------------------------------------------------------------
#! Read
#! ------------------------------------------------------------
def p_lectura(p):
    '''
    lectura   : READ pushPoper LPAREN listaId RPAREN
    '''

def p_listaId(p):
    '''
    listaId : idCall popIO
            | idCall COMMA popIO insertOpRead listaId
    '''

def p_insertOpRead(p):
    '''
    insertOpRead : 
    '''

    cuad.pushPoper("read")

def p_popIO(p):
    '''
    popIO : 
    '''
    temp = cuad.popIO()
    if temp == True:
        cuad.contQuad = cuad.contQuad +1

#! ------------------------------------------------------------
#! Write
#! ------------------------------------------------------------
def p_escritura(p):
    '''
    escritura   : WRITE pushPoper LPAREN exp popIO lextra RPAREN
                | WRITE pushPoper LPAREN LETRERO addCteTable letreroPush popIO lextra RPAREN
    '''

def p_lextra(p):
    '''
    lextra  : COMMA insertOpWrite exp popIO lextra
            | COMMA insertOpWrite LETRERO addCteTable letreroPush popIO lextra
            | empty
    '''

def p_insertOpWrite(p):
    '''
    insertOpWrite  :
    '''
    cuad.pushPoper('write')

#Prueba de letrero
def p_letreroPush(p):
    '''
    letreroPush  :
    '''
    cuad.pushPilaO(table.dictCte[p[-2]])
    cuad.pushType(cuad.getType(p[-2]))

#! ------------------------------------------------------------
#! Condicion, If, If Else
#! ------------------------------------------------------------
def p_condicion(p):
    '''
    condicion   : IF LPAREN exp RPAREN cond1 THEN LBRACE listaEstatutos RBRACE
                | IF LPAREN exp RPAREN cond1 THEN LBRACE listaEstatutos RBRACE ELSE cond3 LBRACE listaEstatutos RBRACE
    '''
    cuad.fillGOTO()

def p_cond1(p):
    '''
    cond1  :
    '''
    temp = cuad.Gotof_IF()
    if temp:
        cuad.contQuad = cuad.contQuad + 1

#* cond2 llena el fillgoto al final del estatuto condicion

def p_cond3(p):
    '''
    cond3  :
    '''
    temp = cuad.Goto_IF()
    if temp:
        cuad.contQuad = cuad.contQuad + 1

#! ------------------------------------------------------------
#! Ciclo While
#! ------------------------------------------------------------
def p_cond_w(p):
    '''
    cond_w : WHILE step1While LPAREN exp RPAREN step2While DO LBRACE listaEstatutos RBRACE step3While
    '''

def p_step1While(p):
    '''
    step1While :
    '''
    cuad.Psaltos.append(cuad.contQuad-1)

def p_step2While(p):
    '''
    step2While :
    '''
    temp = cuad.stepWhile2()
    if temp:
        cuad.contQuad = cuad.contQuad + 1

def p_step3While(p):
    '''
    step3While :
    '''
    temp = cuad.stepWhile3()
    if temp:
        cuad.contQuad = cuad.contQuad + 1

#!! ------------------------------------------------------------
#! Ciclo For
#!! ------------------------------------------------------------
def p_cond_f(p):
    '''
    cond_f : FOR asignacion TO exp step1While step1For step2While DO LBRACE listaEstatutos RBRACE step3While
    '''

def p_step1For(p):
    '''
    step1For : 
    '''
    temp = cuad.stepFor1()
    if temp:
        cuad.contQuad = cuad.contQuad + 1
#! ------------------------------------------------------------
#! Expresiones
#! ------------------------------------------------------------
def p_exp(p):
    '''
    exp     : texp step7
            | texp step7 OR pushPoper exp
    '''

def p_texp(p):
    '''
    texp    : gexp step6
            | gexp step6 AND pushPoper texp
    '''

def p_gexp(p):
    '''
    gexp    : mexp step5
            | mexp step5 LT pushPoper gexp
            | mexp step5 GT pushPoper gexp
            | mexp step5 LTE pushPoper gexp
            | mexp step5 GTE pushPoper gexp
            | mexp step5 EQUALS pushPoper gexp
            | mexp step5 NEQUALS pushPoper gexp
    '''

def p_mexp(p):
    '''
    mexp    : t step4
            | t step4 PLUS pushPoper mexp
            | t step4 MINUS pushPoper mexp
    '''

def p_t(p):
    '''
    t   : f step3
        | f step3 MULT pushPoper t
        | f step3 DIV pushPoper t
    '''

def p_f(p):
    '''
    f   : LPAREN addFF exp RPAREN rmFF
        | CTE_I addCteTable step1
        | CTE_F addCteTable step1
        | CTE_C addCteTable step1
        | llamada
        | idCall
    '''

#* f en expresiones se ayuda de addCteTable y step1 para agregar cte's a tabla de cte
def p_addCteTable(p):
    '''
    addCteTable   : 
    '''
    table.addCte(p[-1])

def p_step1(p):
    '''
    step1   : 
    '''
    #cuad.pushPilaO(p[-2])
    cuad.pushPilaO(table.dictCte[p[-2]])
    cuad.pushType(cuad.getType(p[-2]))

#*Step2 es pushPoper()

def p_step3(p):
    '''
    step3   : 
    '''
    temp = cuad.expStep3()
    if temp:
        cuad.contQuad = cuad.contQuad +1

def p_step4(p):
    '''
    step4   : 
    '''
    temp = cuad.expStep4()
    if temp:
        cuad.contQuad = cuad.contQuad +1

def p_step5(p):
    '''
    step5   : 
    '''
    temp = cuad.expStep5()
    if temp:
        cuad.contQuad = cuad.contQuad +1

def p_step6(p):
    '''
    step6   : 
    '''
    temp = cuad.expStep6()
    if temp:
        cuad.contQuad = cuad.contQuad +1

def p_step7(p):
    '''
    step7   : 
    '''
    temp = cuad.expStep7()
    if temp:
        cuad.contQuad = cuad.contQuad +1

#* Meter fondo falso
def p_addFF(p):
    '''
    addFF :
    '''
    cuad.pushPoper(p[-1])

#* Remover fondo falso
def p_rmFF(p):
    '''
    rmFF :
    '''
    cuad.popFF()

def p_pushPoper(p):
    '''
    pushPoper :
    '''
    cuad.pushPoper(p[-1])

#! ------------------------------------------------------------
#! Regla Empty
#! ------------------------------------------------------------
def p_empty(p):
    '''
    empty :
    '''
    pass

#! ------------------------------------------------------------
#! Error
#! ------------------------------------------------------------
def p_error(p):
    print("Error de Sintaxis", p, p.lineno)

#! ------------------------------------------------------------
#! Pruebas (llamadas a prints para verificar funcionamiento)
#! ------------------------------------------------------------
def p_prueba(p):
    '''
    prueba : 
    '''
    table.dirPrint()
    print("\n")
    cuad.imprimirCuadruplos()
    #Generacion de archivo
    arc.generaTxt(table.dirFuncs, table.dictCte, cuad.Quad)
    #cuad.imprimirPilaO()

#? ------------------------------------------------------------
#? EJECUTAR PARSER
#? ------------------------------------------------------------

# Parser
parser = yacc.yacc()

#Test
log = logging.getLogger()
result = parser.parse(entrada, debug=log)
