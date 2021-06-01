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
memGlob = []
pointer = {}
class memoria(object):
  def __init__(self, rli, rlf, rlc, rlti, rltf, rltc, rltb):
    self.lInt = []
    self.lFloat = []
    self.lChar = []
    self.lTint = []
    self.lTfloat = []
    self.lTchar = []
    self.lTboolean = []

    #*Inicializar espacios de las variables locales y temporales
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

  def printMem(self):
    print(self.lInt, self.lFloat, self.lChar, self.lTint, self.lTfloat, self.lTchar, self.lTboolean)