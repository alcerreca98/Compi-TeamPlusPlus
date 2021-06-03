# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------
#Direcciones Globales
gI = 2000
gF = 4000
gC = 6000
#Temporales Globales
gtI = 8000
gtF = 10000
gtC = 12000
gtB = 14000
#Direcciones Locales
lI = 16000
lF = 18000
lC = 20000
#Temporales Locales
ltI = 22000
ltF = 24000
ltC = 26000
ltB = 28000

#*Stack de contexto
memStack = []
#*Memoria Global siempre activa
memGlob = []
#* Diccionario de Apuntadores de Acceso para Arreglos/Matrices
pointer = {}

#!---------------------------------------------------
#! Clase Memoria
#!---------------------------------------------------
#? 7 Arreglos, uno para cada tipo de dato int, float char
#? adempas de sus respectivos temporales y boolean temporal
class memoria(object):
  def __init__(self, rli, rlf, rlc, rlti, rltf, rltc, rltb):
    self.lInt = []
    self.lFloat = []
    self.lChar = []
    self.lTint = []
    self.lTfloat = []
    self.lTchar = []
    self.lTboolean = []

    #*Inicializar espacios de las variables locales y temporales como None
    #*genera los espacios en blanco segun el tamaño del ERA
    for i in range(int(rli)):
        self.lInt.append(None)
    for i in range(int(rlf)):
        self.lFloat.append(None)
    for i in range(int(rlc)):
        self.lChar.append(None)
    for i in range(int(rlti)):
        self.lTint.append(None)
    for i in range(int(rltf)):
        self.lTfloat.append(None)
    for i in range(int(rltc)):
        self.lTchar.append(None)
    for i in range(int(rltb)):
        self.lTboolean.append(None)

  def printPrueba(self):
    print("Estoy en el metodo printPrueba")

    #Print de todas las listas de datos de la instancia memoria
  def printMem(self):
    print("-----------------------------------------")
    print("lint: ",self.lInt)
    print("lfloat: ", self.lFloat)
    print("lchar: ",self.lChar)
    print("ltint: ",self.lTint)
    print("ltfloat: ",self.lTfloat)
    print("ltchar: ", self.lTchar)
    print("ltbool: ", self.lTboolean)
    print("-----------------------------------------")