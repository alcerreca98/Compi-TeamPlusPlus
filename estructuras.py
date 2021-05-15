# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------


#class funcion(object):
#    def __init__(self, id, type, vart):
#        self.id = id
#        self.type = type
#        self.vart = vart
#
#class variable(object):
#    def __init__(self, id, type):
#        self.id = id
#        self.type = type
#
#class clases(object):
#    def __init__(self, id, herencia):
#        self.id = id
#        self.herencia = herencia
#
#class objeto(object):
#    def __init__(self, id, type):
#        self.id = id
#        self.type = type
#    
#    def printVar(self):
#        print("id ="+self.id+" tipo= "+self.type)
#    
#    def getType(self):
#        print("id ="+self.id+" tipo= "+self.type)
#        
#    def setType(self):
#        print("id ="+self.id+" tipo= "+self.type)
#    
#funcDir = []
#tablaVars = []
#p1 = variable("iPos","int")
#tablaVars.append(p1)
#p2 = variable("iCont","int")
#tablaVars.append(p2)
#p3 = variable("fTGFA","float")
#tablaVars.append(p3)
#funcDir.append(funcion("Imprime","int",tablaVars))
#
##p1.printVar()
#for ivariable in tablaVars:
#   ivariable.printVar()

# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------
import sys

class funcion(object):
    def __init__(self, id, type, dict_func):#, vart):
        self.id = id
        self.type = type
        self.dict_func = dict_func
#        self.vart = vart

class variable(object):
    def __init__(self, id, type):
        self.id = id
        self.type = type

class clases(object):
    def __init__(self, id, herencia):
        self.id = id
        self.herencia = herencia

class objeto(object):
    def __init__(self, id, type):
        self.id = id
        self.type = type






