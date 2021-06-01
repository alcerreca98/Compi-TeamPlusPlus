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
mainSize = dirFuncs["Main"].tam
mem.memStack.append(mem.memoria(mainSize[0], mainSize[1], mainSize[2], mainSize[3], mainSize[4], mainSize[5], mainSize[6]))
memoriaMain = mem.memStack[-1]
memoriaMain.printPrueba()

#*-----------------------------------------------------------------------------
#*AQUI EMPIEZAN LAS FUNCIONES DE LAS ACCIONES DEFINIDAS EN CUADRUPLOS
#*-----------------------------------------------------------------------------

def goto(cuad, contProg):
  return int(cuad.result)

#def suma(cuad, contProg):

def asigna(cuad, contProg):
  dirIzq = cuad.dirIzq
  result = cuad.result
  if dirIzq >= 30000 and dirIzq < 40000:
    for i in dictCte.items():
      if i[1] == dirIzq:
        op_Der = i[0]
  else:
    opDer = mem.get()





#Switch que selecciona la funcion a ejecutar segun cuadruplos
def indicador(cuadr, contProg):
  dict_Ind = {
      'Goto': goto,
      '+' : suma,
      '-' : resta,
      '/' : div,
      '*' : mult,
  }
  func = dict_Ind.get(cuadr.action, 'False')
  if func != 'False':
    position = func(cuadr, contProg)
    return position
  return contProg + 1

while cuad[contProg].action != 'End':
  contProg = indicador(cuad[contProg], contProg)


print('\n')
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ FINALIZANDO C CUAK CUAK ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒", '\n')