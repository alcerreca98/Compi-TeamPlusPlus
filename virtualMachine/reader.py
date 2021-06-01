# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------
import re
dirFunc = {}
dirVar = []
dict_cte = {}
Quad = []
programa = ""
boolProg = True

class mv_func(object):
  def __init__(self, id , type, params, di, tam):
    self.id = id
    self.type = type
    self.params = params
    self.di = di
    self.tam = tam
  
  def printFunc(self):
    print(self.id, self.type, self.params, self.di, self.tam)

class mv_var(object):
  def __init__(self, id , type, dir, dim):
    self.id = id
    self.type = type
    self.dir = dir
    self.dim = dim
  
  def printVar(self):
    print(self.id, self.type, self.dir, self.dim)

class cuadruplo(object):
  def __init__(self, cont, action, dirIzq, dirDer, result):
    self.cont = cont
    self.action = action
    self.dirIzq = dirIzq
    self.dirDer = dirDer
    self.result = result
  
  def printCuad(self):
    print(self.cont, self.action, self.dirIzq, self.dirDer, self.result)

def typeCheck(func):
  z = re.search('\d+\.\d+', func)
  x = re.search('[A-Za-z]', func)
  if(x != None):
    tipo = "char"
    return func
  elif(z != None):
    auxLlave = float(func)
    tipo = "float"
    return auxLlave
  else:
    auxLlave = int(func)
    tipo = "int"
    return auxLlave

def getType(cte):
  """ Regresa el tipo de dato """
  tipo = str(type(cte))
  temp = None
  if tipo == "<class 'float'>":
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

def convList(lista):
  aux = []
  lista = lista.lstrip('[')
  lista = lista.rstrip(']')
  lista = lista.rstrip()
  if lista == '':
    return(aux)
  else:  
    aux = lista.split(',')
    auxList = len(aux)
    aux = list(map(int, aux))
    return(aux)

def convParams(lista):
  aux = []
  lista = lista.lstrip('[')
  lista = lista.rstrip(']')
  if lista == '':
    return(aux)
  else:
    aux = lista.split(',')
    return(aux)

#Lectura del archivo
def readFile():
  print('\n')
  print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ INICIANDO C CUAK CUAK ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒", '\n')
  x = input('Ingresar nombre del archivo: ')
  path = "../compilacion/" + x
  print("compilacion/" + path)
  table = 1
  file = open(path, "r")
  compilacion = file.readlines()
  tam = len(compilacion)

  #*Lectura y administracion de categorias
  global boolProg
  global programa
  for i in range(tam):
    line = compilacion[i].rstrip('\n')
    if line[0] == '/':
      table = table + 1
    else:
      if table == 1:
        func = (line.split('~'))
        #* ID | Type | [Params] | Dir_inicial | [Tam]
        if boolProg == True:
          programa = func[0]
          boolProg = False
        tempParams = convParams(func[2])
        tempTam = convList(func[4])
        temp = mv_func(func[0], func[1], tempParams, int(func[3]), tempTam)
        dirFunc[func[0]] = temp
      elif table == 2:
        #* ID | Type | Dir | Dim
        func = (line.split('~'))
        tempDim = convList(func[3])
        temp = mv_var(func[0], func[1], int(func[2]), tempDim)
        dirVar.append(temp)
      elif table == 3:
        #* ID | REF
        func = (line.split('~'))
        auxLlave = typeCheck(func[0])
        dict_cte[auxLlave] = int(func[1])
      elif table == 4:
        #* CONT | Action | opIzq | opDer | Result
        func = (line.split('~'))
        temp = cuadruplo(func[0], func[1], func[2], func[3], func[4])
        Quad.append(temp)
    file.close
  
  for ids in dirFunc:
    dirFunc[ids].printFunc()

  tam = len(dirVar)
  for ids in range(tam):
    dirVar[ids].printVar()

  tam = len(Quad)
  for ids in range(tam):
    Quad[ids].printCuad()
  print(dict_cte)
