# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# ------------------------------------------------------------

import ply.yacc as yacc
import logging
from lexer import file, path, entrada, tokens

#test = open(path,"r")
#entrada = test.read()
#test.close()

# Gramatica
#No defini starting symbol, pero segun documentacion
#la primera regla gramatical definida toma como default el strating simbol
def p_program(p):
    '''
    program : PROGRAM ID SCOLON declarClases declarVar definFunc MAIN LPAREN RPAREN LBRACE listaEstatutos RBRACE
    '''
#
def p_declarClases(p):
    '''
    declarClases : CLASS ID herencia LBRACE ATTRIBUTES declarAttributes METHODS declarMethods RBRACE declarClases
                 | empty
    '''
def p_herencia(p):
    '''
    herencia : LT EXTENDS ID GT
             | empty
    '''
def p_declarAttributes(p):
    '''
    declarAttributes : listaId COLON tipo SCOLON declarAttributes
                     | empty
    '''
def p_listaId(p):
    '''
    listaId : idCall 
            | idCall COMMA listaId
    '''
def p_idCall(p):
    '''
    idCall : ID
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
def p_listaParam(p):
    '''
    listaParam : param
               | param COMMA listaParam
               | empty
    '''
def p_param(p):
    '''
    param : idCall COLON tipo
    '''
def p_declarVar(p):
    '''
    declarVar : VAR listaId COLON tipo SCOLON declarVar
              | empty
    '''
def p_definFunc(p):
    '''
    definFunc : tipoMethod FUNC ID LPAREN listaParam RPAREN declarVar LBRACE listaEstatutos RBRACE definFunc
              | empty
    '''
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
def p_asignacion(p):
    '''
    asignacion  : idCall ASIGNA exp 
    '''
def p_llamada(p):
    '''
    llamada   : ID DOT ID LPAREN enviaReferencia RPAREN
              | ID LPAREN enviaReferencia RPAREN 
    '''
def p_enviaReferencia(p):
    '''
    enviaReferencia   : exp
                      | exp COMMA enviaReferencia
                      | empty
    '''
def p_returnf(p):
    '''
    returnf   : RETURN LPAREN exp RPAREN 
    '''
def p_lectura(p):
    '''
    lectura   : READ LPAREN idCall RPAREN
    '''
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
def p_condicion(p):
    '''
    condicion   : IF LPAREN exp RPAREN THEN LBRACE listaEstatutos RBRACE
                | IF LPAREN exp RPAREN THEN LBRACE listaEstatutos RBRACE ELSE LBRACE listaEstatutos RBRACE
    '''
def p_cond_w(p):
    '''
    cond_w : WHILE LPAREN exp RPAREN DO LBRACE listaEstatutos RBRACE
    '''
def p_cond_f(p):
    '''
    cond_f : FOR idCall ASIGNA exp TO exp DO LBRACE listaEstatutos RBRACE
    '''
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
def p_empty(p):
    '''
    empty :
    '''
    pass

def p_error(p):
    print("Error de Sintaxis", p, p.lineno)

# Parser
parser = yacc.yacc()

#Test
log = logging.getLogger()
result = parser.parse(entrada, debug=log)
