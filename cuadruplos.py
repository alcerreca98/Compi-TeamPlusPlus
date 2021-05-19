# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------
import sys
import estructuras as estructura
import cuboSemantico as oracle
import modif_tables as tabla

#stacks
Poper = []
Psaltos = []
Ptypes = []
PilaO = []
avail = []
Quad = []

#Variables globales
contQuad = 1
oraculo = oracle.SemanticCube().cube
#param = 1

def quadInsert(action, dirIzq, dirDer, result):
  """Genera un quadruplo y lo inserta en la lista de cuadruplos"""
  temp = estructura.cuadruplo(contQuad-1, action, dirIzq, dirDer, result)
  Quad.append(temp)


def pushPilaO(id):
  """ Inserta ID en stack de operandos  """
  PilaO.append(id)

def getType(cte):
    tipo = str(type(cte))
    temp = None
    if cte == 'true' or cte == 'false':
        temp = 'boolean'
        return temp
    elif tipo == "<class 'float'>":
        temp = 'float'
        return temp
    elif tipo == "<class 'int'>":
        temp = 'int'
        return temp
    elif cte[0] == "'":
        temp = 'char'
        return temp
    elif tipo == "<class 'str'>":
        temp = 'string'
        return temp

#Inserta tipo en stack de tipos
def pushType(type):
  Ptypes.append(type)

#Insertar operacion en el stack de operadores
def pushPoper(action):
  Poper.append(action)

#Sacar fondo falso
def popFF():
  Poper.pop()

#Imprime toda la lista de cuadruplos
def imprimirCuadruplos():
  tam = len(Quad)
  for x in range(tam):
    Quad[x].printCuad()
