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

#Insertar un quadruplo
def quadInsert(action, dirIzq, dirDer, result):
  temp = estructura.cuadruplo(contQuad-1, action, dirIzq, dirDer, result)
  Quad.append(temp)

#Insertar operacion en el stack de operadores
def addPoper(action):
  Poper.append(action)

#Sacar fondo falso
def popFF():
  Poper.pop()