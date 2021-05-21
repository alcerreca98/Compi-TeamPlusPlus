# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------
import sys
import estructuras as estructura
import cuboSemantico as oracle

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

#Inserta ID en stack de operandos
def pushPilaO(id):
  """ Inserta ID en stack de operandos  """
  PilaO.append(id)

#Regresa el tipo de dato
def getType(cte):
  """ Regresa el tipo de dato """
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
  """ Inserta tipo en stack de tipos """
  Ptypes.append(type)

#Insertar operacion en el stack de operadores
def pushPoper(action):
  """ Insertar operacion en el stack de operadores """
  Poper.append(action)

#Sacar fondo falso
def popFF():
  """
  Sacar fondo falso 
  
  es auxiliar a rmFF en el parser

  regla addFF tambien esta directo en parser
  
   """
  Poper.pop()

#Imprime toda la lista de cuadruplos
def imprimirCuadruplos():
  """ Imprime toda la lista de cuadruplos """
  tam = len(Quad)
  for x in range(tam):
    Quad[x].printCuad()

#Imprime toda la lista de Operandos
def imprimirPilaO():
  """ Imprime toda la lista de Operandos """
  tam = len(PilaO)
  #print(len(PilaO))
  for x in range(0,tam):
    print("PilaO en [", x,"]", PilaO[x])

#######################GENERACION DE CUADRUPLOS######################

#insertar cuadruplos de multiplicacion division con chequeo semantico
def expStep3():
  """ insertar cuadruplos de multiplicacion division con chequeo semantico """
  global Resultado
  size = len(Poper)
  if size > 0:
    if Poper[size -1] != '(':
      if Poper[size-1] == '*' or Poper[size-1] == '/':
        #print("ENTRE A 3")
        tempR = PilaO.pop()
        rType = Ptypes.pop()
        tempL = PilaO.pop()
        lType = Ptypes.pop()
        operator = Poper.pop()
        result_type = oraculo[operator][lType][rType]
        if result_type != 'error':
          quadInsert(operator, tempL, tempR, Resultado)
          print(tempL, operator, tempR, Resultado)
          PilaO.append(Resultado)
          Ptypes.append(result_type)
          #Prueba Resultado
          Resultado = Resultado + 1
          return True
        else:
          print("Error: typemismatch :", tempL, lType, operator, tempR, rType)
          sys.exit()
  return False

#insertar cuadruplos de suma resta con chequeo semantico
def expStep4():
  """ insertar cuadruplos de suma resta con chequeo semantico """
  global Resultado
  size = len(Poper)
  if size > 0:
    if Poper[size -1] != '(':
      if Poper[size-1] == '+' or Poper[size-1] == '-':
        #print("ENTRE A 4")
        tempR = PilaO.pop()
        rType = Ptypes.pop()
        tempL = PilaO.pop()
        lType = Ptypes.pop()
        operator = Poper.pop()
        result_type = oraculo[operator][lType][rType]
        if result_type != 'error':
          quadInsert(operator, tempL, tempR, Resultado)
          print(tempL, operator, tempR, Resultado)
          PilaO.append(Resultado)
          Ptypes.append(result_type)
          Resultado = Resultado + 1
          return True
        else:
          print("Error: typemismatch :", tempL, lType, operator, tempR, rType)
          sys.exit()
  return False

#insertar cuadruplos de operadores logicos con chequeo semantico
def expStep5():
  """ insertar cuadruplos de operadores logicos con chequeo semantico """
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
        print(result_type)
        if result_type != 'error':
          quadInsert(operator, tempL, tempR, Resultado)
          PilaO.append(Resultado)
          Ptypes.append(result_type)
          #Prueba Resultado
          Resultado = Resultado + 1
          return True
        else:
          print("Error: typemismatch :", tempL, lType, operator, tempR, rType)
          sys.exit()
  return False

#insertar cuadruplos de moperador AND con chequeo semantico
def expStep6():
  """ insertar cuadruplos de moperador AND con chequeo semantico """
  global Resultado
  size = len(Poper)
  if size > 0:
    if Poper[size -1] != '(':
      if Poper[size-1] == '&&' :
        #print("ENTRE A 6")
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
          print("Error: typemismatch :", tempL, lType, operator, tempR, rType)
          sys.exit()
  return False

#insertar cuadruplos de moperador OR con chequeo semantico
def expStep7():
  """ insertar cuadruplos de moperador OR con chequeo semantico """
  global Resultado
  size = len(Poper)
  if size > 0:
    if Poper[size -1] != '(':
      if Poper[size-1] == '||' :
        print("ENTRE A 7")
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
          print("Error: typemismatch :", tempL, lType, operator, tempR, rType)
          sys.exit()
  return False

#insertar cuadruplos de ASIGNACION con chequeo semantico
def asignaStep2():
  """ insertar cuadruplos de asignacion con chequeo semantico """
  #global Resultado
  size = len(Poper)
  if size > 0:
    if Poper[size-1] == '=' :
      #imprimirPilaO()
      tempR = PilaO.pop()
      #print("Mi Right operands es: ",tempR)
      rType = Ptypes.pop()
      tempL = PilaO.pop()
      #print("Mi Izq operands es: ",tempL)
      lType = Ptypes.pop()
      operator = Poper.pop()
      if lType == rType:
        quadInsert(operator, tempR, None, tempL)
        print(tempL, operator, tempR)
        #PilaO.append(tempL)
        #Ptypes.append(lType)
        #Prueba Resultado
        #Resultado = Resultado + 1
        return True
      else:
        print("Error: typemismatch en asignacion", tempL, lType,"=", tempR, rType)
        sys.exit()
  return False

def popIO():
  size = len(Poper)
  if size > 0:
    if Poper[size-1] == 'read' or Poper[size-1] == 'write':
      tempR = PilaO.pop()
      Ptypes.pop()
      operator = Poper.pop()
      quadInsert(operator, None, None, tempR)
      return True
  return False

def popReturn():
  size = len(Poper)
  if size > 0:
    if Poper[size-1] == 'return':
      tempR = PilaO.pop()
      Ptypes.pop()
      operator = Poper.pop()
      quadInsert(operator, None, None, tempR)
      return True
  return False

def Gotof_IF():
  exp_type = Ptypes.pop()
  print(exp_type)
  if exp_type != 'boolean':
    print('Error: type mismatch, IF')
    sys.exit()
  else:
    cond = PilaO.pop()
    quadInsert('GotoF', cond, None, None)
    Psaltos.append(contQuad-1)
    return True
  
def fillGOTO():
  end = Psaltos.pop()
  Quad[end].result = contQuad

def Goto_IF():
  quadInsert('Goto', None, None, None)
  falso = Psaltos.pop()
  Psaltos.append(contQuad-1)
  Quad[falso].result = contQuad