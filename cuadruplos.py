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
Resultado = 1000

def quadInsert(action, dirIzq, dirDer, Resultado):
  """Genera un quadruplo y lo inserta en la lista de cuadruplos"""
  temp = estructura.cuadruplo(contQuad-1, action, dirIzq, dirDer, Resultado)
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
  print(action)

#Sacar fondo falso
def popFF():
  Poper.pop()

def expStep3():
  global Resultado
  size = len(Poper)
  if size > 0:
    if Poper[size -1] != '(':
      if Poper[size-1] == '*' or Poper[size-1] == '/':
        tempR = PilaO.pop()
        print(tempR)
        rType = Ptypes.pop()
        tempL = PilaO.pop()
        print(tempL)
        lType = Ptypes.pop()
        operator = Poper.pop()
        result_type = oraculo[operator][lType][rType]
        if result_type != 'error':
          quadInsert(operator, tempL, tempR, Resultado)
          PilaO.append(Resultado)
          Ptypes.append(result_type)
          #Prueba Resultado
          Resultado = Resultado + 1
          return True
        else:
          print("Error: typemismatch,*,/")
          sys.exit()
  return False

def expStep4():
  global Resultado
  size = len(Poper)
  if size > 0:
    if Poper[size -1] != '(':
      if Poper[size-1] == '+' or Poper[size-1] == '-':
        tempR = PilaO.pop()
        print(tempR)
        rType = Ptypes.pop()
        tempL = PilaO.pop()
        print(tempL)
        lType = Ptypes.pop()
        operator = Poper.pop()
        result_type = oraculo[operator][lType][rType]
        if result_type != 'error':
          quadInsert(operator, tempL, tempR, Resultado)
          PilaO.append(Resultado)
          Ptypes.append(result_type)
          #Prueba Resultado
          Resultado = Resultado + 1
          return True
        else:
          print("Error: typemismatch,+,-")
          sys.exit()
  return False

def expStep5():
  global Resultado
  size = len(Poper)
  if size > 0:
    if Poper[size -1] != '(':
      if Poper[size-1] == '>' or Poper[size-1] == '<' or Poper[size-1] == '>=' or Poper[size-1] == '<=' or Poper[size-1] == '==' or Poper[size-1] == '!=':
        tempR = PilaO.pop()
        rType = Ptypes.pop()
        tempL = PilaO.pop()
        lType = Ptypes.pop()
        operator = Poper.pop()
        result_type = oraculo[operator][lType][rType]
        if result_type != 'error':
          quadInsert(operator, tempL, tempR, Resultado)
          PilaO.append(Resultado)
          Ptypes.append(result_type)
          #Prueba Resultado
          Resultado = Resultado + 1
          return True
        else:
          print("Error: typemismatch,>,<, >=, <=, ==, !=")
          sys.exit()
  return False

def expStep6():
  global Resultado
  size = len(Poper)
  if size > 0:
    if Poper[size -1] != '(':
      if Poper[size-1] == '&&' :
        tempR = PilaO.pop()
        rType = Ptypes.pop()
        tempL = PilaO.pop()
        lType = Ptypes.pop()
        operator = Poper.pop()
        result_type = oraculo[operator][lType][rType]
        if result_type != 'error':
          quadInsert(operator, tempL, tempR, Resultado)
          PilaO.append(Resultado)
          Ptypes.append(result_type)
          #Prueba Resultado
          Resultado = Resultado + 1
          return True
        else:
          print("Error: typemismatch,&&")
          sys.exit()
  return False

def expStep7():
  global Resultado
  size = len(Poper)
  if size > 0:
    if Poper[size -1] != '(':
      if Poper[size-1] == '||' :
        tempR = PilaO.pop()
        rType = Ptypes.pop()
        tempL = PilaO.pop()
        lType = Ptypes.pop()
        operator = Poper.pop()
        result_type = oraculo[operator][lType][rType]
        if result_type != 'error':
          quadInsert(operator, tempL, tempR, Resultado)
          PilaO.append(Resultado)
          Ptypes.append(result_type)
          #Prueba Resultado
          Resultado = Resultado + 1
          return True
        else:
          print("Error: typemismatch,||")
          sys.exit()
  return False

def asignaStep2():
  global Resultado
  size = len(Poper)
  if size > 0:
    tempR = PilaO.pop()
    rType = Ptypes.pop()
    tempL = PilaO.pop()
    lType = Ptypes.pop()
    operator = Poper.pop()
    if lType == rType:
      quadInsert(operator, tempR, None, tempL)
      PilaO.append(tempL)
      Ptypes.append(lType)
      #Prueba Resultado
      Resultado = Resultado + 1
      return True
    else:
      print("Error: typemismatch em asignacion =")
      sys.exit()
  return False




#Imprime toda la lista de cuadruplos
def imprimirCuadruplos():
  tam = len(Quad)
  for x in range(tam):
    Quad[x].printCuad()
