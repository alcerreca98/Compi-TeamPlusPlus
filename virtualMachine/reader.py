# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------
import re
dirFunc = {}
dirVar = {}
dict_cte = {}
Quad = []
programa = ""
boolProg = True

#! ------------------------------------------------------------
#! Estructura de Funcion, mv_func
#! ------------------------------------------------------------
#? Reconstruccion de la estructura de variables de compilacion
#? Menos las tablas de variables locales
class mv_func(object):
  """ Estructura de Funciones con atributos:

    id -> string con el nombre de la funcion

    type -> string con el tipo de la funcion

    params -> Lista de parametros de la funcion

    di -> cuadruplo inicial de la funcion

    tam -> Lista con el numero de variables locales y temporales
    por tipo, necesarios para calcular el tamaño del ERA """
  def __init__(self, id , type, params, di, tam):
    self.id = id
    self.type = type
    self.params = params
    self.di = di
    self.tam = tam
  
  def printFunc(self):
    print(self.id, self.type, self.params, self.di, self.tam)

#! ------------------------------------------------------------
#! Estructura Variables Globales
#! ------------------------------------------------------------
#? Reconstruccion de la estructura de Tabla de variables globales
class mv_var(object):
  """ Estructura de Variable con atributos:

    id -> string con el nombre de la variable

    type -> string con el tipo de la variable

    dir -> direccion de memoria asignada a la variable

    dim -> lista de dimensiones para arreglos o matrices
    """
  def __init__(self, id , type, dir, dim):
    self.id = id
    self.type = type
    self.dir = dir
    self.dim = dim
  
  def printVar(self):
    print(self.id, self.type, self.dir, self.dim)

#! ------------------------------------------------------------
#! Estructura Cuadruplos
#! ------------------------------------------------------------
#? Reconstruccion de la estructura de Cuadruplos de Compilación
class cuadruplo(object):
  def __init__(self, cont, action, dirIzq, dirDer, result):
    self.cont = cont
    self.action = action
    self.dirIzq = dirIzq
    self.dirDer = dirDer
    self.result = result
  
  def printCuad(self):
    print(self.cont, self.action, self.dirIzq, self.dirDer, self.result)


#! ------------------------------------------------------------
#! Recasteo de datos de String (lectura de OBJ) a original
#! ------------------------------------------------------------
#? Estas funciones hacen el casteo de los datos que son string cuando los lee el reader
#? y los inserta ya casteados a sus respectivos tipos a nuestras estructuras
#regresa el tipo de dato dado un string y compara contra regex
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

#regresa el tipo de dato dada una constante
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
  elif tipo == "<class 'bool'>":
      temp = 'boolean'
      return temp

#recasteo de la lista de tamaño de funcion y la lista de dimensiones de variables
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

#recasteo de lista de parametros de funcion
def convParams(lista):
  aux = []
  lista = lista.lstrip('[')
  lista = lista.rstrip(']')
  if lista == '':
    return(aux)
  else:
    aux = lista.split(',')
    tam = len(aux)
    for i in range(tam):
      if(aux[i].find('int')!=-1):
        aux[i]='int'
      if(aux[i].find('float')!=-1):
        aux[i]='int'
      if(aux[i].find('char')!=-1):
        aux[i]='int'
    return(aux)


#! ------------------------------------------------------------
#! FILE READER
#! ------------------------------------------------------------
#? Este modulo lee todo nuestro archivo OBJ de codigo intermedio
#? y hace la reconstrucción de estructuras para el manejo en la VM
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
        #TODO: LECTURA DE FUNCIONES
        #* ID | Type | [Params] | Dir_inicial | [Tam]
        if boolProg == True:
          programa = func[0]
          boolProg = False
        tempParams = convParams(func[2])
        tempTam = convList(func[4])
        temp = mv_func(func[0], func[1], tempParams, int(func[3]), tempTam)
        dirFunc[func[0]] = temp
      elif table == 2:
        #TODO: LECTURA DE TABLA VARIABLES GLOBALES
        #* ID | Type | Dir | Dim
        func = (line.split('~'))
        tempDim = convList(func[3])
        temp = mv_var(func[0], func[1], int(func[2]), tempDim)
        dirVar[func[0]]=temp
      elif table == 3:
        #TODO: LECTURA DE TABLA CONSTANTES
        #* ID | REF
        func = (line.split('~'))
        auxLlave = typeCheck(func[0])
        dict_cte[auxLlave] = int(func[1])
      elif table == 4:
        #TODO: LECTURA DE CUADRUPLOS
        #* CONT | Action | opIzq | opDer | Result
        func = (line.split('~'))
        temp = cuadruplo(func[0], func[1], func[2], func[3], func[4])
        Quad.append(temp)
    file.close
  
  #TODO: Prints de debugger, para verificar llenado y funcionamiento
  for ids in dirFunc:
    dirFunc[ids].printFunc()

  for ids in dirVar:
    dirVar[ids].printVar()

  tam = len(Quad)
  for ids in range(tam):
    Quad[ids].printCuad()
  print(dict_cte)
