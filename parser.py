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
    program : PROGRAM ID global SCOLON gomain vardef lfunc main
    '''
def p_global(p):
    '''
    global :
    '''
    #Inicializa directorio de Funciones
def p_gomain(p):
    '''
    gomain :
    '''
    #Genera el cuadruplo con el goto a vars globales e inicio de funciones
def p_vardef(p):
    '''
    vardef  : VAR vars lvars
            | empty
    '''
def p_lvars(p):
    '''
    lvars   : vars lvars
            | empty
    '''
def p_vars(p):
    '''
    vars    : type COLON lid SCOLON
    '''
def p_type(p):
    '''
    type    : INT
            | FLOAT
            | CHAR
    '''
    #Insert de tipo para semantica
def p_lid(p):
    '''
    lid     : ID lidaux
    '''
def p_lidaux(p):
    '''
    lidaux  : COMMA ID lidaux
            | empty
    '''
def p_lfunc(p):
    '''
    lfunc   : func lfunc
            | empty
    '''
def p_func(p):
    '''
    func    : type MODULE ID LPAREN lparam RPAREN vardef LBRACE estatuto lestatutos RBRACE
    '''
def p_lparam(p):
    '''
    lparam  : param 
            | param SCOLON lparam
            | empty
    '''
def p_param(p):
    '''
    param   : type ID
    '''
def p_lestatutos(p):
    '''
    lestatutos   : estatuto lestatutos
                 | empty
    '''
def p_estatuto(p):
    '''
    estatuto    : asigna SCOLON
                | llamada SCOLON
                | retorno SCOLON
                | lectura SCOLON
                | escritura SCOLON
                | condicion SCOLON
                | ciclo_w SCOLON
                | ciclo_f SCOLON
                | func_esp SCOLON
    '''
def p_asigna(p):
    '''
    asigna  : variable exp
    '''
def p_variable(p):
    '''
    variable   : ID
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
        | variable
        | llamada
    '''
def p_llamada(p):
    '''
    llamada   : LPAREN exp lexpresiones RPAREN
    '''
def p_lexpresiones(p):
    '''
    lexpresiones    : COMMA exp lexpresiones
                    | empty
    '''
def p_retorno(p):
    '''
    retorno   : RETURN LPAREN exp RPAREN
    '''
def p_lectura(p):
    '''
    lectura   : READ LPAREN variable RPAREN
    '''
def p_escritura(p):
    '''
    escritura   : WRITE LPAREN exp lextra RPAREN
                | WRITE LPAREN LETRERO lextra RPAREN
    '''
def p_lextra(p):
    '''
    lextra  : exp lextra
            | LETRERO lextra
            | empty
    '''
def p_condicion(p):
    '''
    condicion   : IF LPAREN exp RPAREN THEN LBRACE estatuto lestatutos RBRACE
                | IF LPAREN exp RPAREN THEN LBRACE estatuto lestatutos RBRACE ELSE LBRACE estatuto lestatutos RBRACE
    '''
def p_ciclo_w(p):
    '''
    ciclo_w : WHILE LPAREN exp RPAREN DO LBRACE estatuto lestatutos RBRACE
    '''
def p_ciclo_f(p):
    '''
    ciclo_f : FOR ID ASIGNA exp TO exp DO LBRACE estatuto lestatutos RBRACE
    '''
def p_func_esp(p):
    '''
    func_esp    : line
                | point
                | circle
                | arc
                | penup
                | pendown
                | color
                | size
                | clear
    '''    
def p_line(p):
    '''
    line : LINE LPAREN exp RPAREN
    '''
def p_point(p):
    '''
    point : POINT LPAREN exp COMMA exp RPAREN
    '''
def p_circle(p):
    '''
    circle : CIRCLE LPAREN exp RPAREN
    '''
def p_arc(p):
    '''
    arc : ARC LPAREN exp RPAREN
    '''
def p_penup(p):
    '''
    penup : PENUP LPAREN RPAREN
    '''
def p_pendown(p):
    '''
    pendown : PENDOWN LPAREN RPAREN
    '''
def p_color(p):
    '''
    color : COLOR LPAREN exp RPAREN
    '''
def p_size(p):
    '''
    size : SIZE LPAREN exp RPAREN
    '''
def p_clear(p):
    '''
    clear : CLEAR LPAREN RPAREN
    '''
def p_main(p):
    '''
    main : MAIN LPAREN RPAREN lvars LBRACE estatuto lestatutos RBRACE
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
