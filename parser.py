# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------

import ply.yacc as yacc
import logging
from lexer import file, path, entrada, tokens

# Gramatica
#No defini starting symbol, pero segun documentacion
#la primera regla gramatical definida toma como default el strating simbol

# ------------------------------------------------------------
# Programa, para la estructura general
# ------------------------------------------------------------
def p_program(p):
    '''
    program : PROGRAM ID SCOLON declarClases declarVar definFunc MAIN LPAREN RPAREN LBRACE listaEstatutos RBRACE
    '''
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
    declarAttributes : listaIdDeclare COLON tipo SCOLON declarAttributes
                     | empty
    '''
def p_listaIdDeclare(p):
    '''
    listaIdDeclare : idDeclare 
                   | idDeclare COMMA listaIdDeclare
    '''
def p_idDeclare(p):
    '''
    idDeclare : ID
              | ID LBRACK CTE_I RBRACK
              | ID LBRACK CTE_I RBRACK LBRACK CTE_I RBRACK
    '''
def p_idCall(p):
    '''
    idCall : ID
           | ID DOT ID
           | ID LBRACK exp RBRACK
           | ID LBRACK exp RBRACK LBRACK exp RBRACK
    '''
def p_tipo(p):
    '''
    tipo : ID
         | INT
         | FLOAT
         | CHAR
    '''
# Metodos de la clase, opcionales
def p_declarMethods(p):
    '''
    declarMethods : tipoMethod FUNC ID LPAREN listaParam RPAREN LBRACE listaEstatutos RBRACE declarMethods
                  | empty
    '''
def p_tipoMethod(p):
    '''
    tipoMethod : VOID
               | INT
               | FLOAT
               | CHAR
    '''
#Para parametros, en declaracion de metodos o funciones, arreglos y matrices van con exp o con CTE_I
def p_listaParam(p):
    '''
    listaParam : param
               | param COMMA listaParam
               | empty
    '''
def p_param(p):
    '''
    param : ID COLON tipo
    '''
# ------------------------------------------------------------
# Declaración de Variables
# ------------------------------------------------------------
def p_declarVar(p):
    '''
    declarVar : VAR listaIdDeclare COLON tipo SCOLON declarVar
              | empty
    '''
# ------------------------------------------------------------
# Definicion de Funciones
# ------------------------------------------------------------
def p_definFunc(p):
    '''
    definFunc : tipoMethod FUNC ID LPAREN listaParam RPAREN declarVar LBRACE listaEstatutos RBRACE definFunc
              | empty
    '''
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
    asignacion  : idCall ASIGNA exp 
    '''
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
    lectura   : READ LPAREN listaId RPAREN
    '''
def p_listaId(p):
    '''
    listaId : idCall 
            | idCall COMMA listaId
    '''
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
    cond_f : FOR idCall ASIGNA exp TO exp DO LBRACE listaEstatutos RBRACE
    '''
# ------------------------------------------------------------
# Expresiones
# ------------------------------------------------------------
def p_exp(p):
    '''
    exp     : texp
            | texp OR exp
    '''
def p_texp(p):
    '''
    texp    : gexp
            | gexp AND texp
    '''
def p_gexp(p):
    '''
    gexp    : mexp
            | mexp LT mexp
            | mexp GT mexp
            | mexp EQUALS mexp
            | mexp NEQUALS mexp
    '''
def p_mexp(p):
    '''
    mexp    : t
            | t PLUS mexp
            | t MINUS mexp
    '''
def p_t(p):
    '''
    t   : f
        | f MULT t
        | f DIV t
    '''
def p_f(p):
    '''
    f   : LPAREN exp RPAREN
        | CTE_I
        | CTE_F
        | CTE_C
        | llamada
        | idCall
    '''
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
