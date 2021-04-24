# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------

##Para ambas Directorio de Funciones y Tabla de variables.
#class table(object):
#    def __init__(self, id, type, dir, params, size, quad):
#        self.id = id
#        self.type = type
#        self.dir = dir
#        self.params = params
#        self.size = size
#        self.quad = quad
#
class funcion(object):
    def __init__(self, id, type, vart):
        self.id = id
        self.type = type
        self.vart = vart

class variable(object):
    def __init__(self, id, type):
        self.id = id
        self.type = type
    
    def printVar(self):
        print("id ="+self.id+" tipo= "+self.type)
    
    def getType(self):
        print("id ="+self.id+" tipo= "+self.type)
        
    def setType(self):
        print("id ="+self.id+" tipo= "+self.type)
    
funcDir = []
tablaVars = []
p1 = variable("iPos","int")
tablaVars.append(p1)
p2 = variable("iCont","int")
tablaVars.append(p2)
p3 = variable("fTGFA","float")
tablaVars.append(p3)
funcDir.append(funcion("Imprime","int",tablaVars))

#p1.printVar()
for ivariable in tablaVars:
   ivariable.printVar()