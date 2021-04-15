# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------
import ply.lex as lex

# Palabras Reservadas
reserved = {
    'program' : 'PROGRAM',
    'func' : 'FUNC',
    'main' : 'MAIN',

    'class' : 'CLASS',
    'extends' : 'EXTENDS',
    'attributes' : 'ATTRIBUTES',
    'methods' : 'METHODS',

    'var' : 'VAR',
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',

    'return' : 'RETURN',
    'void' : 'VOID',

    'read' : 'READ',
    'write' : 'WRITE',

    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',

    'while' : 'WHILE',
    'do' : 'DO',
    
    'for' : 'FOR',
    #'from' : 'FROM'    #el "for" ocupa el lugar del "desde" 
    'to' : 'TO',
}

# Lista de Tokens
tokens = [
    'ID',
    #'CLASS_ID'

    'CTE_I',
    'CTE_F',
    'CTE_C',
    'LETRERO',

    'DOT',
    'COMMA',
    'SCOLON',
    'COLON',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACK',
    'RBRACK',
    'QUOTE',

    'ASIGNA',
    'PLUS',
    'MINUS',
    'MULT',
    'DIV',

    'EQUALS',
    'NEQUALS',
    'GT',
    'LT',
    'GTE',
    'LTE',
    'AND',
    'OR',

] + list(reserved.values())

# Caracteres de Delimmitacion
t_DOT = r'\-\>'
t_COMMA = r'\,'
t_SCOLON = r'\;'
t_COLON = r'\:'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACK = r'\['
t_RBRACK = r'\]'
t_QUOTE = r'\"'

# Operadores Aritmeticos
t_ASIGNA = r'\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
    
# Operadores Logicos y de Comparacion
t_EQUALS = r'=='
t_NEQUALS = r'!='
t_GT = r'\>'
t_LT = r'\<'
t_GTE = r'>='
t_LTE = r'<='
t_AND = r'&&'
t_OR = r'\|\|'

t_ignore = ' \t\n'

#string antes de char
t_CTE_C = r'\'[A-Za-z]\''
t_LETRERO = r'\"(.*?)\"' #para el write

# Delcaracion de Funciones
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0]) # t.lineno
    t.lexer.skip(1)

#'(?:\d+(?:\.\d*)?|\.\d+)'
def t_CTE_F(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CTE_I(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Lexer
lex.lex()

#Test
print("===== Iniciando C cuack cuack =====\n")
file = input('Test file name : ')
if len(file) < 1 : file = "testGlobal.txt"
path = "Pruebas/" + file
print("Read from: " + path )
try:
    test = open(path, "r")
    entrada = test.read()
    test.close()
    lex.input(entrada)
    # Muestra tokens
    while True:
        tok = lex.token()
        if not tok:
            break
        print(tok)
    print("\n===== Finalizando Lexer C cuack cuack =====\n")
except OSError as e:
    print("\n===== Error en C cuack cuack =====\n")