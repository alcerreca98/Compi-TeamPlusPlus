# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------
import sys
import estructuras as estructura
import cuboSemantico as oracle
import modif_tables as table
import memoriaVirtual as mem

#stacks
Poper = []
Psaltos = []
Ptypes = []
PilaO = []
avail = []
Quad = []
paramK = 0
pointerParam = ""

#Variables globales
contQuad = 1
oraculo = oracle.SemanticCube().cube
Resultado = 1000

#Genera un quadruplo y lo inserta en la lista de cuadruplos
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

#! ------------------------------------------------------------
#! SET Y GET DE DIRECCIONES DE MEMORIA 
#! ------------------------------------------------------------
#incrementa en 1 el contador de direcciones y le suma su direccion base segun el tipo
#esto regresa la siguiente dirección local temporal libre
def getAvail(tipo):
  """ regresa la siguiente direccion de memoria temporal libre segun el tipo"""
  if tipo == 'int':
    table.lti = table.lti +1
    return table.lti + mem.ltI
  elif tipo == 'float':
    table.ltf = table.ltf +1
    return table.ltf + mem.ltF
  elif tipo == 'char':
    table.ltc = table.ltc +1
    return table.ltc + mem.ltC
  elif tipo == 'boolean':
    table.ltb = table.ltb +1
    return table.ltb + mem.ltB
  else:
    print("No deberia entrar aqui ERR")

#regresa la siguiente direccion de memoria local NO temporal libre.
def getAvailLocal(tipo):
  """ regresa la siguiente direccion de memoria local NO temporal libre """
  if tipo == 'int':
    table.li = table.li +1
    return table.li + mem.lI
  elif tipo == 'float':
    table.lf = table.lf +1
    return table.lf + mem.lF
  elif tipo == 'char':
    table.lc = table.lc +1
    return table.lc + mem.lC
  else:
    print("No deberia entrar aqui ERR")

#regresa la siguiente dirección de memoria global libre
def getAvailGlobal(tipo):
  """ regresa la siguiente dirección de memoria global libre """
  if tipo == 'int':
    table.gi = table.gi +1
    return table.gi + mem.gI
  elif tipo == 'float':
    table.gf = table.gf +1
    return table.gf + mem.gF
  elif tipo == 'char':
    table.gc = table.gc +1
    return table.gc + mem.gC
  else:
    print("No deberia entrar aqui ERR")

#incrementa el contador de memoria local por tipo, segun el tamaño de un arreglo o matriz
def setSaltoLocal(salto,tipo):
  """ incrementa el contador de memoria local por tipo, segun el tamaño de un arreglo o matriz """
  if tipo == 'int':
    table.li = table.li + salto
  elif tipo == 'float':
    table.lf = table.lf + salto
  elif tipo == 'char':
    table.lc = table.lc + salto

#incrementa el contador de memoria global por tipo, segun el tamaño de un arreglo o matriz
def setSaltoGlobal(salto,tipo):
  """ incrementa el contador de memoria global por tipo, segun el tamaño de un arreglo o matriz """
  if tipo == 'int':
    table.gi = table.gi + salto
  elif tipo == 'float':
    table.gf = table.gf + salto
  elif tipo == 'char':
    table.gc = table.gc + salto

#! -------------------------------------------------------------------
#######################!GENERACION DE CUADRUPLOS######################
#! -------------------------------------------------------------------

#TODO: Expresiones
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
          #get avail
          Resultado = getAvail(result_type)
          table.contadorERAlocalTemporal(result_type)
          quadInsert(operator, tempL, tempR, Resultado)
          #print(tempL, operator, tempR, Resultado)
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
          Resultado = getAvail(result_type)
          table.contadorERAlocalTemporal(result_type)
          quadInsert(operator, tempL, tempR, Resultado)
          #print(tempL, operator, tempR, Resultado)
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
        #print(result_type)
        if result_type != 'error':
          Resultado = getAvail(result_type)
          table.contadorERAlocalTemporal(result_type)
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
          Resultado = getAvail(result_type)
          table.contadorERAlocalTemporal(result_type)
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
          Resultado = getAvail(result_type)
          table.contadorERAlocalTemporal(result_type)
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

#TODO: cuadruplos ASIGNACION
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
        #print(tempL, operator, tempR)
        PilaO.append(tempL)
        Ptypes.append(lType)
        #Prueba Resultado
        #Resultado = Resultado + 1
        return True
      else:
        print("Error: typemismatch en asignacion", tempL, lType,"=", tempR, rType)
        sys.exit()
  return False

#TODO: cuadruplos READ / WRITE
#insertar cuadruplos de read/write
def popIO():
  """ insertar cuadruplos de read/write """
  size = len(Poper)
  if size > 0:
    if Poper[size-1] == 'read' or Poper[size-1] == 'write':
      tempR = PilaO.pop()
      Ptypes.pop()
      operator = Poper.pop()
      quadInsert(operator, None, None, tempR)
      return True
  return False

#TODO: cuadruplos RETURN
#insertar cuadruplos de return
def popReturn():
  """ insertar cuadruplos de return """
  size = len(Poper)
  if size > 0:
    if Poper[size-1] == 'return':
      tempR = PilaO.pop()
      Ptypes.pop()
      operator = Poper.pop()
      quadInsert(operator, None, None, tempR)
      return True
  return False

#TODO: puntos neuralgicos CONDICION IF
def Gotof_IF():
  exp_type = Ptypes.pop()
  #print(exp_type)
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
  return True

#TODO: puntos neuralgicos CICLO WHILE
#Reusa un punto del if
def stepWhile2():
  exp_type = Ptypes.pop()
  if exp_type != 'boolean':
    print('Error: type mismatch, While')
    sys.exit()
  else:
    cond = PilaO.pop()
    quadInsert('GotoF', cond, None, None)
    Psaltos.append(contQuad-1)
    return True

def stepWhile3():
  falso = Psaltos.pop()
  end = Psaltos.pop()
  quadInsert('Goto', None, None, end)
  Quad[falso].result = contQuad
  return True

#TODO: puntos neuralgicos CICLO FOR
#Reusa los puntos del while
def stepFor1():
  global Resultado
  tempR = PilaO.pop()
  rType = Ptypes.pop()
  tempL = PilaO.pop()
  lType = Ptypes.pop()
  result_type = oraculo['<'][lType][rType]
  if result_type != 'error':
    Resultado = getAvail(result_type)
    table.contadorERAlocalTemporal(result_type)
    quadInsert('<', tempL, tempR, Resultado)
    PilaO.append(Resultado)
    Ptypes.append(result_type)
    return True
  else:
    print("Error: type mismatch, For")
    sys.exit()
  
#? CUADRUPLOS DE LLAMADA DE FUNCION Y ARREGLOS ESTAN EN EL PARSER!