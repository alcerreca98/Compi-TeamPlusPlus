# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------

import sys
import memoria as mem
import reader
import numpy as np 

#Directorio de funciones
dirFuncs = reader.dirFunc
#Diccionario de constantes
dictCte = reader.dict_cte
#Cuadruplos
cuad = reader.Quad

#Variables globales
contProg = 0

reader.readFile()

#Switch que selecciona la funcion a ejecutar segun cuadruplos
def indicador(cuadr, contProg):
  dict_Ind = {
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


while cuad[i].action != 'End':
  contProg = indicador(cuad[contProg], contProg)


print('\n')
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ FINALIZANDO C CUAK CUAK ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒", '\n')