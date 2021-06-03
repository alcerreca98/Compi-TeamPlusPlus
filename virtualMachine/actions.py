# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------

import sys
import memory as mem
import reader
import re

#Directorio de funciones
dirFuncs = reader.dirFunc
#Tabla de variables globales
dirVar = reader.dirVar
#Diccionario de constantes
dictCte = reader.dict_cte
#Cuadruplos
cuad = reader.Quad

#?Variables globales
#* Instruction Pointer
contProg = 0
#llamada de funciones
#* de donde vengo
migajita = []
#* a donde voy
cuadLlamada = []
#* sus parametros
funcParams = []
pInt = 0
pFloat = 0
pChar = 0
newMemory = None
#* ParcheGuadalupano
ParcheGuadalupano = []

#!---------------------------------------------------
#! Funciones de Acciones Cuadruplos
#!---------------------------------------------------

# todo:  SALTOS
def goto(cuad, contProg):
  return int(cuad.result)

def gotoF(cuad, contProg):
  izq = int(cuad.dirIzq)
  op_Izq = getContent(izq)
  if(op_Izq):
    return contProg +1
  else:
    return int(cuad.result)

def gosub(cuad, contProg):
  global ParcheGuadalupano
  global migajita
  global cuadLlamada
  Nombre = cuad.result
  pg=dirVar.get(Nombre, False)
  if(pg != False):
    ParcheGuadalupano.append(dirVar[Nombre].dir)
  migajita.append(contProg)
  salto = cuadLlamada.pop()
  return salto

def endfunc(cuad, contProg):
  global migajita
  returnCuad = migajita.pop()
  mem.memStack.pop()
  return returnCuad+1

# todo:  EXPRESIONES ARITMETICAS

def suma(cuad, contProg):
  izq = int(cuad.dirIzq)
  der = int(cuad.dirDer)
  res = int(cuad.result)
  #* Get contenido Operando Izquierdo
  op_Izq = getContent(izq)
  #* Get contenido Operando Derecho  
  op_Der = getContent(der)

  resultSuma = op_Izq + op_Der
  addDirContent(res, resultSuma)
  return contProg + 1

def resta(cuad, contProg):
  izq = int(cuad.dirIzq)
  der = int(cuad.dirDer)
  res = int(cuad.result)
  #* Get contenido Operando Izquierdo
  op_Izq = getContent(izq)
  #* Get contenido Operando Derecho  
  op_Der = getContent(der)

  resultResta = op_Izq - op_Der
  addDirContent(res, resultResta)
  return contProg + 1

def mult(cuad, contProg):
  izq = int(cuad.dirIzq)
  der = int(cuad.dirDer)
  res = int(cuad.result)
  #* Get contenido Operando Izquierdo
  op_Izq = getContent(izq)
  #* Get contenido Operando Derecho  
  op_Der = getContent(der)

  resultMult = op_Izq * op_Der
  addDirContent(res, resultMult)
  return contProg + 1

def div(cuad, contProg):
  izq = int(cuad.dirIzq)
  der = int(cuad.dirDer)
  res = int(cuad.result)
  #* Get contenido Operando Izquierdo
  op_Izq = getContent(izq)
  #* Get contenido Operando Derecho  
  op_Der = getContent(der)
  if(op_Der == 0):
    print("ERROR: division por 0")
    sys.exit()
  resultMult = op_Izq / op_Der
  addDirContent(res, resultMult)
  return contProg + 1

def menor(cuad, contProg):
  izq = int(cuad.dirIzq)
  der = int(cuad.dirDer)
  res = int(cuad.result)
  #* Get contenido Operando Izquierdo
  op_Izq = getContent(izq)
  #* Get contenido Operando Derecho  
  op_Der = getContent(der)

  if(op_Izq < op_Der):
    addDirContent(res, True)
  else:
    addDirContent(res, False)
  return contProg + 1

def menorIgual(cuad, contProg):
  izq = int(cuad.dirIzq)
  der = int(cuad.dirDer)
  res = int(cuad.result)
  #* Get contenido Operando Izquierdo
  op_Izq = getContent(izq)
  #* Get contenido Operando Derecho  
  op_Der = getContent(der)

  if(op_Izq <= op_Der):
    addDirContent(res, True)
  else:
    addDirContent(res, False)
  return contProg + 1

def mayor(cuad, contProg):
  izq = int(cuad.dirIzq)
  der = int(cuad.dirDer)
  res = int(cuad.result)
  #* Get contenido Operando Izquierdo
  op_Izq = getContent(izq)
  #* Get contenido Operando Derecho  
  op_Der = getContent(der)

  if(op_Izq > op_Der):
    addDirContent(res, True)
  else:
    addDirContent(res, False)
  return contProg + 1

def mayorIgual(cuad, contProg):
  izq = int(cuad.dirIzq)
  der = int(cuad.dirDer)
  res = int(cuad.result)
  #* Get contenido Operando Izquierdo
  op_Izq = getContent(izq)
  #* Get contenido Operando Derecho  
  op_Der = getContent(der)

  if(op_Izq >= op_Der):
    addDirContent(res, True)
  else:
    addDirContent(res, False)
  return contProg + 1

def equals(cuad, contProg):
  izq = int(cuad.dirIzq)
  der = int(cuad.dirDer)
  res = int(cuad.result)
  #* Get contenido Operando Izquierdo
  op_Izq = getContent(izq)
  #* Get contenido Operando Derecho  
  op_Der = getContent(der)

  if(op_Izq == op_Der):
    addDirContent(res, True)
  else:
    addDirContent(res, False)
  return contProg + 1

def notEquals(cuad, contProg):
  izq = int(cuad.dirIzq)
  der = int(cuad.dirDer)
  res = int(cuad.result)
  #* Get contenido Operando Izquierdo
  op_Izq = getContent(izq)
  #* Get contenido Operando Derecho  
  op_Der = getContent(der)

  if(op_Izq != op_Der):
    addDirContent(res, True)
  else:
    addDirContent(res, False)
  return contProg + 1

def opAnd(cuad, contProg):
  izq = int(cuad.dirIzq)
  der = int(cuad.dirDer)
  res = int(cuad.result)
  #* Get contenido Operando Izquierdo
  op_Izq = getContent(izq)
  #* Get contenido Operando Derecho  
  op_Der = getContent(der)

  if(op_Izq and op_Der):
    addDirContent(res, True)
  else:
    addDirContent(res, False)
  return contProg + 1

def opOr(cuad, contProg):
  izq = int(cuad.dirIzq)
  der = int(cuad.dirDer)
  res = int(cuad.result)
  #* Get contenido Operando Izquierdo
  op_Izq = getContent(izq)
  #* Get contenido Operando Derecho  
  op_Der = getContent(der)

  if(op_Izq or op_Der):
    addDirContent(res, True)
  else:
    addDirContent(res, False)
  return contProg + 1

# todo:  ESTATUTOS SECUENCIALES

def asigna(cuad, contProg):
  izq = int(cuad.dirIzq)
  res = int(cuad.result)
  #* Get del dato a ingresar
  op_Der = getContent(izq)
  #* Guarda a memoria el dato
  addDirContent(res, op_Der)
  return contProg + 1

def read(cuad, contProg):
  res = int(cuad.result)
  #* Get del dato a ingresar
  valor = input()
  try:
      valor = int(valor)
  except ValueError:
      try:
          valor = float(valor)
      except ValueError:
          pass
  in_type = reader.getType(valor)
  res_type = getMemType(res)
  if (in_type != res_type):
    print("Error: Type Mismatch en input", in_type, " a ", res_type)
    sys.exit()
  #* Guarda a memoria el dato
  addDirContent(res, valor)
  return contProg + 1

def write(cuad, contProg):
  res = int(cuad.result)
  #* Get del dato a ingresar
  escribe = getContent(res)
  #* Imprime el dato
  print(escribe)
  return contProg + 1

# todo:  LLAMADA DE FUNCIONES

def era(cuad, contProg):
  global cuadLlamada
  global funcParams
  global newMemory
  funcName = cuad.result
  funcion = dirFuncs.get(funcName, False)
  if (funcion != False) :
    funcParams = dirFuncs[funcion.id].params
    cuadLlamada.append(dirFuncs[funcion.id].di)
    eraSize = dirFuncs[funcion.id].tam
    #eraSize = (eraSize.split(','))
    newMemory = mem.memoria(eraSize[0],eraSize[1],eraSize[2],eraSize[3],eraSize[4],eraSize[5],eraSize[6])
  else:
    print("No deberia entrar aqui porque el chequeo semantico de que la funcion este declarada está en el compilador")
    sys.exit()
  return contProg + 1

def params(cuad, contProg):
  global funcParams
  global pInt
  global pFloat 
  global pChar
  izq = int(cuad.dirIzq)
  op_Izq = getContent(izq)
  res = int(cuad.result)
  paramNum= len(funcParams)
  if(funcParams[res-1]=='int'):
    auxdir=16000+pInt
    pInt = pInt+1
  elif(funcParams[res-1]=='float'):
    auxdir=18000+pFloat
    pInt = pFloat+1
  elif(funcParams[res-1]=='char'):
    auxdir=22000+pChar
    pInt = pChar+1

  mem.memStack.append(newMemory)
  addDirContent(auxdir,op_Izq)
  if(res == paramNum):
    pInt = 0
    pFloat = 0
    pChar = 0
  
  return contProg + 1

def retorno(cuad, contProg):
  global ParcheGuadalupano
  res = int(cuad.result)
  valor = getContent(res)
  pg = ParcheGuadalupano.pop()
  addDirContent(pg, valor)
  return contProg+1

# todo:  ARREGLOS / MATRICES

def verif(cuad, contProg):
  exp = getContent(int(cuad.dirIzq))
  limInf = getContent(int(cuad.dirDer))
  limSup = getContent(int(cuad.result))
  if((exp<limInf) or (exp>limSup)):
    print("Error en index", exp, " in ",contProg," out of bounds")
    sys.exit()
  return contProg+1

def sumaDimensionada(cuad, contProg):
  izq = int(cuad.dirIzq)
  der = int(cuad.dirDer)
  res = int(cuad.result)
  #* Get contenido Operando Izquierdo
  op_Izq = getContent(izq)
  #* Get contenido Operando Derecho  
  op_Der = getContent(der)
  desp = res%1000
  resultSuma = op_Izq + op_Der
  mem.pointer[desp]=resultSuma
  return contProg + 1

#!---------------------------------------------------
#! Manejo de Memoria y Contenido
#!---------------------------------------------------
#obtiene el valor del contenido en una dada dirección, sea de constante, apuntador, local o global
def getContent(dir):
  if dir >= 30000 and dir < 40000:
    for i in dictCte.items():
      if i[1] == dir:
        valor = i[0]
  elif dir >= 80000:
    desp = dir%1000
    valor = getDirContent(mem.pointer[desp])
  else:
    valor = getDirContent(dir)
  return valor
#obtiene el valor del contenido en una dada dirección local o global
def getDirContent(auxdir):
    tipo = auxdir//1000
    desp = auxdir%1000
    if tipo == 2:
      if memoriaGlob.lInt[desp] != None:
        return memoriaGlob.lInt[desp]
      else:
        print("Error: variable sin valor",auxdir,contProg)
        sys.exit()
    if tipo == 4:
      if memoriaGlob.lFloat[desp] != None:
        return memoriaGlob.lFloat[desp]
      else:
        print("Error: variable sin valor",auxdir,contProg)
        sys.exit()    
    if tipo == 6:
      if memoriaGlob.lChar[desp] != None:
        return memoriaGlob.lChar[desp]
      else:
        print("Error: variable sin valor",auxdir,contProg)
        sys.exit()
    if tipo == 16:
      memactual = mem.memStack[-1]
      if memactual.lInt[desp] != None:
        return memactual.lInt[desp]
      else:
        print("Error: variable sin valor",auxdir, contProg)
        sys.exit()
    if tipo == 18:
      memactual = mem.memStack[-1]
      if memactual.lFloat[desp] != None:
        return memactual.lFloat[desp]
      else:
        print("Error: variable sin valor",auxdir,contProg)
        sys.exit()
    if tipo == 20:
      memactual = mem.memStack[-1]
      if memactual.lChar[desp] != None:
        return memactual.lChar[desp]
      else:
        print("Error: variable sin valor",auxdir,contProg)
        sys.exit()
    if tipo == 22:
      memactual = mem.memStack[-1]
      if memactual.lTint[desp] != None:
        return memactual.lTint[desp]
      else:
        print("Error: variable sin valor",auxdir,contProg)
        sys.exit()
    if tipo == 24:
      memactual = mem.memStack[-1]
      if memactual.lTfloat[desp] != None:
        return memactual.lTfloat[desp]
      else:
        print("Error: variable sin valor",auxdir,contProg)
        sys.exit()
    if tipo == 26:
      memactual = mem.memStack[-1]
      if memactual.lTchar[desp] != None:
        return memactual.lTchar[desp]
      else:
        print("Error: variable sin valor",auxdir,contProg)
        sys.exit()
    if tipo == 28:
      memactual = mem.memStack[-1]
      if memactual.lTboolean[desp] != None:
        return memactual.lTboolean[desp]
      else:
        print("Error: variable sin valor",auxdir,contProg)
        sys.exit()
    if tipo == 80:
      valor = mem.pointer[desp]
      print("get dir content de :",valor)
      return getDirContent(valor)

#Inserta en una direccion dada, el contenido especificado
def addDirContent(auxdir, content):
    tipo = auxdir//1000
    desp = auxdir%1000
    if tipo == 2:
      memoriaGlob.lInt[desp] = content
    if tipo == 4:
      memoriaGlob.lFloat[desp] = content  
    if tipo == 6:
      memoriaGlob.lChar[desp] = content    
    if tipo == 16:
      memactual = mem.memStack[-1]
      memactual.lInt[desp] = content
    if tipo == 18:
      memactual = mem.memStack[-1]
      memactual.lFloat[desp] = content  
    if tipo == 20:
      memactual = mem.memStack[-1]
      memactual.lChar[desp] = content
    if tipo == 22:
      memactual = mem.memStack[-1]
      memactual.lTint[desp] = content
    if tipo == 24:
      memactual = mem.memStack[-1]
      memactual.lTfloat[desp] = content   
    if tipo == 26:
      memactual = mem.memStack[-1]
      memactual.lTchar[desp] = content  
    if tipo == 28:
      memactual = mem.memStack[-1]
      memactual.lTboolean[desp] = content
    if tipo == 80:
      address = mem.pointer[desp]
      addDirContent(address,content)
#regresa el tipo de memoria esperado segun el mapa de memoria paraa su direccion
def getMemType(auxdir):
  tipo = auxdir//1000
  if tipo == 2:
    temp = 'int'
    return temp  
  if tipo == 4:
    temp = 'float'
    return temp
  if tipo == 6:
    temp = 'string'
    return temp
  if tipo == 16:
    temp = 'int'
    return temp
  if tipo == 18:
    temp = 'float'
    return temp
  if tipo == 20:
    temp = 'string'
    return temp
  if tipo == 22:
    temp = 'int'
    return temp
  if tipo == 24:
    temp = 'float'
    return temp
  if tipo == 26:
    temp = 'string'
    return temp
  if tipo == 28:
    temp = 'boolean'
    return temp

# TODO: getParam y getParamContenta hacen lo mismo que getContent y getDirContent
# TODO: con la diferencia de que la busqueda de locales lo hacen en la memoria ANTERIOR al contexto
def getParam(dir):
  if dir >= 30000 and dir < 40000:
    for i in dictCte.items():
      if i[1] == dir:
        valor = i[0]
  elif dir >= 80000:
    desp = dir%1000
    valor = getParamContent(mem.pointer[desp])
  else:
    valor = getParamContent(dir)
  return valor

def getParamContent(auxdir):
  tipo = auxdir//1000
  desp = auxdir%1000
  if tipo == 2:
    if memoriaGlob.lInt[desp] != None:
      return memoriaGlob.lInt[desp]
    else:
      print("Error: variable anterior sin valor",auxdir)
      sys.exit()
  if tipo == 4:
    if memoriaGlob.lFloat[desp] != None:
      return memoriaGlob.lFloat[desp]
    else:
      print("Error: variable anterior sin valor",auxdir)
      sys.exit()    
  if tipo == 6:
    if memoriaGlob.lChar[desp] != None:
      return memoriaGlob.lChar[desp]
    else:
      print("Error: variable anterior sin valor",auxdir)
      sys.exit()
  if tipo == 16:
    memactual = mem.memStack[-2]
    if memactual.lInt[desp] != None:
      return memactual.lInt[desp]
    else:
      print("Error: variable anterior sin valor",auxdir)
      sys.exit()
  if tipo == 18:
    memactual = mem.memStack[-2]
    if memactual.lFloat[desp] != None:
      return memactual.lFloat[desp]
    else:
      print("Error: variable anterior sin valor",auxdir)
      sys.exit()
  if tipo == 20:
    memactual = mem.memStack[-2]
    if memactual.lChar[desp] != None:
      return memactual.lChar[desp]
    else:
      print("Error: variable anterior sin valor",auxdir)
      sys.exit()
  if tipo == 22:
    memactual = mem.memStack[-2]
    if memactual.lTint[desp] != None:
      return memactual.lTint[desp]
    else:
      print("Error: variable anterior sin valor",auxdir)
      sys.exit()
  if tipo == 24:
    memactual = mem.memStack[-2]
    if memactual.lTfloat[desp] != None:
      return memactual.lTfloat[desp]
    else:
      print("Error: variable anterior sin valor",auxdir)
      sys.exit()
  if tipo == 26:
    memactual = mem.memStack[-2]
    if memactual.lTchar[desp] != None:
      return memactual.lTchar[desp]
    else:
      print("Error: variable anterior sin valor",auxdir)
      sys.exit()
  if tipo == 28:
    memactual = mem.memStack[-2]
    if memactual.lTboolean[desp] != None:
      return memactual.lTboolean[desp]
    else:
      print("Error: variable anterior sin valor",auxdir)
      sys.exit()

def addReturnContent(auxdir, content):
    tipo = auxdir//1000
    desp = auxdir%1000
    if tipo == 2:
      memoriaGlob.lInt[desp] = content
    if tipo == 4:
      memoriaGlob.lFloat[desp] = content  
    if tipo == 6:
      memoriaGlob.lChar[desp] = content    
    if tipo == 16:
      memactual = mem.memStack[-2]
      memactual.lInt[desp] = content
    if tipo == 18:
      memactual = mem.memStack[-2]
      memactual.lFloat[desp] = content  
    if tipo == 20:
      memactual = mem.memStack[-2]
      memactual.lChar[desp] = content
    if tipo == 22:
      memactual = mem.memStack[-2]
      memactual.lTint[desp] = content
    if tipo == 24:
      memactual = mem.memStack[-2]
      memactual.lTfloat[desp] = content   
    if tipo == 26:
      memactual = mem.memStack[-2]
      memactual.lTchar[desp] = content  
    if tipo == 28:
      memactual = mem.memStack[-2]
      memactual.lTboolean[desp] = content
    if tipo == 80:
      mem.pointer[desp] = content
#!---------------------------------------------------
#! SWITCH DE ACCIONES
#!---------------------------------------------------
#Switch que selecciona la funcion a ejecutar segun cuadruplos
def indicador(cuadr, contProg):
  dict_Ind = {
      'Goto': goto,
      'GotoF': gotoF,
      'GOSUB': gosub,
      'ENDFunc': endfunc,
      '+' : suma,
      '-' : resta,
      '/' : div,
      '*' : mult,
      '=' : asigna,
      '<' : menor,
      '<=' : menorIgual,
      '>' : mayor,
      '>=' : mayorIgual,
      '==' : equals,
      '!=' : notEquals,
      '&&' : opAnd,
      '||' : opOr,
      'read' : read,
      'write' : write,
      'ERA' : era,
      'PARAM' : params,
      'return' : retorno,
      'VER' : verif,
      '+t' : sumaDimensionada,
  }
  func = dict_Ind.get(cuadr.action, 'False')
  if func != 'False':
    position = func(cuadr, contProg)
    return position
  return contProg + 1


#!---------------------------------------------------
#! EJECUCION
#!---------------------------------------------------

reader.readFile()
#? Inicializa Memoria Global
globSize = dirFuncs[reader.programa].tam
mem.memGlob.append(mem.memoria(globSize[0], globSize[1], globSize[2], 0, 0, 0, 0))
memoriaGlob = mem.memGlob[-1]
#? Inicializa Primera Memoria Local, contexto : Main
mainSize = dirFuncs["Main"].tam
mem.memStack.append(mem.memoria(mainSize[0], mainSize[1], mainSize[2], mainSize[3], mainSize[4], mainSize[5], mainSize[6]))
memoriaMain = mem.memStack[-1]

while cuad[contProg].action != 'ENDProgram':
  contProg = indicador(cuad[contProg], contProg)

memoriaGlob.printMem()
memoriaMain.printMem()
print('\n')
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ FINALIZANDO C CUAK CUAK ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒", '\n')