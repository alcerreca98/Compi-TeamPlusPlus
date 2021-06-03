# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------

from lexer import archivo

#! ------------------------------------------------------------
#! GENERADOR CODIGO INTERMEDIO archivo OBJ
#! ------------------------------------------------------------
#? Toma todas las estructuras de compilación y escribe lo necesario
#? para la ejecucion en un archivo con el código intermedio
#Funcion que exporta direcotrio de funciones, tabla de constantes y cuadruplos
def generaTxt(dir_func, cte, Quad):
  print(archivo)
  cte_tam = len(cte)
  file = open('compilacion/' + archivo, 'w')

  #TODO: ESCRIBE FORMATEADO EL DIRECTORIO DE FUNCIONES
  #Tabla de funciones
  for ids in dir_func:
    line = str(ids) + '~', str(dir_func[ids].type) + '~', str(dir_func[ids].params) + '~', str(dir_func[ids].di) + '~', str(dir_func[ids].tam) + '\n' 
    file.writelines(line)
  file.write('/\n')

  #TODO: ESCRIBE FORMATEADO LA TABLA DE VARIABLES GLOBALES
  #Tabla de variables globales
  for ids in dir_func:
    for var in dir_func[ids].dir_var:
      line = dir_func[ids].dir_var[var].printVariableComp()
      file.writelines(line)
      file.write('\n')
  file.write('/\n')

  #TODO: ESCRIBE FORMATEADA LA TABLA DE CONSTANTES
  #Diccionario de constantes
  for i in cte:
    line = str(i) + '~', str(cte[i]) + '\n'
    file.writelines(line)
  file.write('/\n')

  #TODO: ESCRIBE FORMATEADA LA LISTA DE CUADRUPLOS
  #Tabla de cuadruplos
  for i in range(0, len(Quad)):
    line = str(Quad[i].cont) + '~', str(Quad[i].action) + '~', str(Quad[i].opIzq) + '~', str(Quad[i].opDer) + '~', str(Quad[i].result) + '\n'
    file.writelines(line) 