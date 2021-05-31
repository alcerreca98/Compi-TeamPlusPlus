# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------

dirFunc = []
dict_cte = {}
Quad = []

class mv_func(object):
  def __init__(self, id , type, dir_var, params, di, tam):
    self.id = id
    self.type = type
    self.dir_var = {}
    self.params = []
    self.di = 0
    self.tam = []

class cuadruplo(object):
  def __init__(self, cont, action, dirIzq, dirDer, result):
    self.cont = cont
    self.action = action
    self.dirIzq = dirIzq
    self.dirDer = dirDer
    self.result = result

#Lectura del archivo
def readFile():
  print('\n')
  print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ INICIANDO C CUAK CUAK ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒", '\n')
  x = input('Ingresar nombre del archivo: ')
  path = "compilacion/" + x
  print("compilacion/" + path)
  table = 1
  file = open(path, r)
  compilacion = file.readlines()
  tam = len(compilacion)
  for i in range(tam):
    line = compilacion[i].rstrip('\n')
    if line[0] == '/':
      table = table + 1
    else:
      if table == 1:
        func = (line.split('Ð'))
        temp = mv_func(func[0], func[1], func[2], func[3], func[4], func[5], func[6])
        dirFunc.append(temp)
      elif table == 2:
        dict_cte[func[0]] = func[1]
      elif table == 3:
        func = (line.split('Ð'))
        temp = cuadruplo(func[0], func[1], func[2], func[3], func[4])
        Quad.append(temp)
    file.close
