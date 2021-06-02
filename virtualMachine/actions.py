# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------

import sys
import memory as mem
import reader


#Directorio de funciones
dirFuncs = reader.dirFunc
#Tabla de variables globales
dirVar = reader.dirVar
#Diccionario de constantes
dictCte = reader.dict_cte
#Cuadruplos
cuad = reader.Quad

#Variables globales
contProg = 0

reader.readFile()

#Memoria Global
globSize = dirFuncs[reader.programa].tam
mem.memGlob.append(mem.memoria(globSize[0], globSize[1], globSize[2], 0, 0, 0, 0))
memoriaGlob = mem.memGlob[-1]

mainSize = dirFuncs["Main"].tam
mem.memStack.append(mem.memoria(mainSize[0], mainSize[1], mainSize[2], mainSize[3], mainSize[4], mainSize[5], mainSize[6]))
memoriaMain = mem.memStack[-1]


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

#def suma(cuad, contProg):
# todo:  EXPRESIONES ARITMETICAS
def asigna(cuad, contProg):
  izq = int(cuad.dirIzq)
  res = int(cuad.result)
  #* Get del dato a ingresar
  op_Der = getContent(izq)
  #* Guarda a memoria el dato
  addDirContent(res, op_Der)
  return contProg + 1

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
#!---------------------------------------------------
#! Manejo de Memoria y Contenido
#!---------------------------------------------------

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

def getDirContent(auxdir):
    tipo = auxdir//1000
    desp = auxdir%1000
    if tipo == 2:
      if memoriaGlob.lInt[desp] != None:
        return memoriaGlob.lInt[desp]
      else:
        print("Error: variable sin valor",auxdir)
        sys.exit()
    if tipo == 4:
      if memoriaGlob.lFloat[desp] != None:
        return memoriaGlob.lFloat[desp]
      else:
        print("Error: variable sin valor",auxdir)
        sys.exit()    
    if tipo == 6:
      if memoriaGlob.lChar[desp] != None:
        return memoriaGlob.lChar[desp]
      else:
        print("Error: variable sin valor",auxdir)
        sys.exit()
    if tipo == 16:
      memactual = mem.memStack[-1]
      if memactual.lInt[desp] != None:
        return memactual.lInt[desp]
      else:
        print("Error: variable sin valor",auxdir)
        sys.exit()
    if tipo == 18:
      memactual = mem.memStack[-1]
      if memactual.lFloat[desp] != None:
        return memactual.lFloat[desp]
      else:
        print("Error: variable sin valor",auxdir)
        sys.exit()
    if tipo == 20:
      memactual = mem.memStack[-1]
      if memactual.lChar[desp] != None:
        return memactual.lChar[desp]
      else:
        print("Error: variable sin valor",auxdir)
        sys.exit()
    if tipo == 22:
      memactual = mem.memStack[-1]
      if memactual.lTint[desp] != None:
        return memactual.lTint[desp]
      else:
        print("Error: variable sin valor",auxdir)
        sys.exit()
    if tipo == 24:
      memactual = mem.memStack[-1]
      if memactual.lTfloat[desp] != None:
        return memactual.lTfloat[desp]
      else:
        print("Error: variable sin valor",auxdir)
        sys.exit()
    if tipo == 26:
      memactual = mem.memStack[-1]
      if memactual.lTchar[desp] != None:
        return memactual.lTchar[desp]
      else:
        print("Error: variable sin valor",auxdir)
        sys.exit()
    if tipo == 28:
      memactual = mem.memStack[-1]
      if memactual.lTboolean[desp] != None:
        return memactual.lTboolean[desp]
      else:
        print("Error: variable sin valor",auxdir)
        sys.exit()

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
      mem.pointer[desp] = content

#Switch que selecciona la funcion a ejecutar segun cuadruplos
def indicador(cuadr, contProg):
  dict_Ind = {
      'Goto': goto,
      'GotoF': gotoF,
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
  }
  func = dict_Ind.get(cuadr.action, 'False')
  if func != 'False':
    position = func(cuadr, contProg)
    return position
  return contProg + 1

while cuad[contProg].action != 'ENDProgram':
  contProg = indicador(cuad[contProg], contProg)

memoriaGlob.printMem()
memoriaMain.printMem()
print('\n')
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ FINALIZANDO C CUAK CUAK ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒", '\n')