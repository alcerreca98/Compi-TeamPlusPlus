# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------

from lex import archivo

#Funcion que exporta direcotrio de funciones, tabla de constantes y cuadruplos
def generaTxt(dir_func, cte, Quad):
  print(archivo)
  cte_tam = len(cte)
  file = open('' + archivo, 'w')
  
  #Tabla de funciones
  for ids in dir_func:
    line = str(ids) + 'Ð', str(dir_func[ids].type) + 'Ð', str(dir_func[ids].dir_var) + 'Ð', 
    str(dir_func[ids].params) + 'Ð', dir_func[ids].di + 'Ð', str(dir_func[ids].tam) 
    file.writelines(line)
  file.write('/\n')

  #Diccionario de constantes
  for i in range(cte_tam):
    line = str(cte[i].id) + 'Ð', str(dir_func[i].dir) + '\n'
    file.writelines(line)
    file.write('/\n')

  #Tabla de cuadruplos
  for i in range(0, len(Quad)):
    line = str(Quad[i].cont) + 'Ð', str(Quad[i].action) + 'Ð', str(Quad[i].dirIzq) + 'Ð', 
    str(Quad[i].dirDer) + 'Ð', str(Quad[i].result) + '\n'
    file.writelines(line) 