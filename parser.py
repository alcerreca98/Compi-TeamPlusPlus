# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------

import ply.yacc as yacc
import logging
from lexer import file,entrada, path, tokens
import modif_tables as table
import cuadruplos as cuad
from estructuras import *

# Gramatica
#No defini starting symbol, pero segun documentacion
#la primera regla gramatical definida toma como default el strating simbol

# ------------------------------------------------------------
# Programa, para la estructura general
# ------------------------------------------------------------
def p_program(p):
    '''
    program : PROGRAM ID initProg SCOLON declarClases declarVar definFunc MAIN auxMain LPAREN RPAREN declarVar LBRACE listaEstatutos RBRACE prueba
    '''
def p_prueba(p):
    '''
    prueba : 
    '''
    table.dirPrint()
    cuad.imprimirCuadruplos()

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

def p_auxMain(p):
    '''
    auxMain :
    '''
    table.ingresarTabla("Main", None)
    table.auxFunc = "Main"
    #Regresar valor de salto de Main

# ------------------------------------------------------------
# Declaracion de Clases
# ------------------------------------------------------------
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

#iterador de idDeclare separado por comma
def p_listaIdDeclare(p):
    '''
    listaIdDeclare : idDeclare  
                   | idDeclare COMMA listaIdDeclare
    '''

#sintaxis de declaración de variables
def p_idDeclare(p):
    '''
    idDeclare : ID 
              | ID LBRACK CTE_I RBRACK 
              | ID LBRACK CTE_I RBRACK LBRACK CTE_I RBRACK
    '''
    table.ingresarVariables(p[1], table.tipo)

#sintaxis para indexación o llamada de variables
def p_idCall(p):
    '''
    idCall : ID
           | ID DOT ID
           | ID LBRACK exp RBRACK
           | ID LBRACK exp RBRACK LBRACK exp RBRACK
    '''
    if(table.checkIfExists(p[1])):
        cuad.pushPilaO(p[1])
        condicion = table.dirFuncs[table.programa].searchIfExists(p[1])
        if(condicion == False):
            var = table.dirFuncs[table.auxFunc].searchIfExists(p[1])
        else:
            var = table.dirFuncs[table.programa].searchIfExists(p[1])
        cuad.pushType(var.getType())
    cuad.imprimirPilaO()

#tipo de variables
def p_tipo(p):
    '''
    tipo : ID
         | INT
         | FLOAT
         | CHAR
    '''
    table.tipo = p[1]

# Metodos de la clase, opcionales
def p_declarMethods(p):
    '''
    declarMethods : tipoMethod FUNC ID LPAREN listaParam RPAREN LBRACE listaEstatutos RBRACE declarMethods
                  | empty
    '''

#tipo de metodos y funciones
def p_tipoMethod(p):
    '''
    tipoMethod : VOID
               | INT
               | FLOAT
               | CHAR
    '''
    table.tipoMeth = p[1]

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
    table.ingresarParams(p[3])

# ------------------------------------------------------------
# Declaración de Variables
# ------------------------------------------------------------
def p_declarVar(p):
    '''
    declarVar : VAR tipo COLON listaIdDeclare SCOLON declarVar
              | empty
    '''
# ------------------------------------------------------------
# Definicion de Funciones
# ------------------------------------------------------------
def p_definFunc(p):
    '''
    definFunc : tipoMethod FUNC ID auxFuncion LPAREN listaParam RPAREN declarVar LBRACE listaEstatutos RBRACE definFunc
              | empty
    '''

#guarda en el directorio de funciones la nueva instancia de funcion, con su nombre y tipo
def p_auxFuncion(p):
    '''
    auxFuncion :
    '''
    table.auxFunc = p[-1]
    table.ingresarTabla(table.auxFunc, table.tipoMeth)
# ------------------------------------------------------------
# Estatutos
# ------------------------------------------------------------
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
# ------------------------------------------------------------
# asignacion de valores a variables.
# ------------------------------------------------------------
def p_asignacion(p):
    '''
    asignacion  : idCall ASIGNA pushPoper exp asignStep2 
    '''

#asignStep1 es pushPoper()

def p_asignStep2(p):
    '''
    asignStep2  :
    '''
    if cuad.asignaStep2() == True:
        print("Terminé asignación")
     

# ------------------------------------------------------------
# Llamada de funciones, para clases y normales.
# ------------------------------------------------------------
def p_llamada(p):
    '''
    llamada   : ID DOT ID LPAREN enviaParam RPAREN
              | ID LPAREN enviaParam RPAREN 
    '''
def p_enviaParam(p):
    '''
    enviaParam  : paramReferencia
                | empty
    '''
def p_paramReferencia(p):
    '''
    paramReferencia : exp
                    | exp COMMA paramReferencia
    '''
# ------------------------------------------------------------
# Return
# ------------------------------------------------------------
def p_returnf(p):
    '''
    returnf   : RETURN LPAREN exp RPAREN 
    '''
# ------------------------------------------------------------
# Lectura
# ------------------------------------------------------------
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
# ------------------------------------------------------------
# Escritura
# ------------------------------------------------------------
def p_escritura(p):
    '''
    escritura   : WRITE LPAREN exp lextra RPAREN
                | WRITE LPAREN LETRERO lextra RPAREN
    '''
def p_lextra(p):
    '''
    lextra  : COMMA exp lextra
            | COMMA LETRERO lextra
            | empty
    '''
# ------------------------------------------------------------
# Condicion, If, If Else
# ------------------------------------------------------------
def p_condicion(p):
    '''
    condicion   : IF LPAREN exp RPAREN THEN LBRACE listaEstatutos RBRACE
                | IF LPAREN exp RPAREN THEN LBRACE listaEstatutos RBRACE ELSE LBRACE listaEstatutos RBRACE
    '''
# ------------------------------------------------------------
# Ciclo While
# ------------------------------------------------------------
def p_cond_w(p):
    '''
    cond_w : WHILE LPAREN exp RPAREN DO LBRACE listaEstatutos RBRACE
    '''
# ------------------------------------------------------------
# Ciclo For
# ------------------------------------------------------------
#idCall despues del for? debe ser definido 
def p_cond_f(p):
    '''
    cond_f : FOR asignacion TO exp DO LBRACE listaEstatutos RBRACE
    '''
# ------------------------------------------------------------
# Expresiones
# ------------------------------------------------------------
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
            | mexp step5 LT pushPoper mexp
            | mexp step5 GT pushPoper mexp
            | mexp step5 LTE pushPoper mexp
            | mexp step5 GTE pushPoper mexp
            | mexp step5 EQUALS pushPoper mexp
            | mexp step5 NEQUALS pushPoper mexp
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
        | CTE_I step1
        | CTE_F step1
        | CTE_C step1
        | llamada
        | idCall
    '''

def p_step1(p):
    '''
    step1   : 
    '''
    cuad.pushPilaO(p[-1])
    cuad.pushType(cuad.getType(p[-1]))

#Step2 es pushPoper()

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

# Meter fondo falso
def p_addFF(p):
    '''
    addFF :
    '''
    cuad.pushPoper(p[-1])

# Remover fondo falso
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
# ------------------------------------------------------------
# Regla Empty
# ------------------------------------------------------------
def p_empty(p):
    '''
    empty :
    '''
    pass
# ------------------------------------------------------------
# Error
# ------------------------------------------------------------
def p_error(p):
    print("Error de Sintaxis", p, p.lineno)

# Parser
parser = yacc.yacc()

#Test
log = logging.getLogger()
result = parser.parse(entrada, debug=log)
