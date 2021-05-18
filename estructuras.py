# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------
import sys


class funcion(object):
    def __init__(self, id, type):#, vart):
        self.id = id
        self.type = type
        self.dir_var = {}
    
    def printFuncion(self):
        print("\nid =", self.id, " tipo =", self.type)

    def getVarTable(self):
        return self.dir_var

    def addVar(self, id, type):
        self.dir_var[id] = variable(id, type)

    def printVarTable(self):
        for var in self.dir_var:
            self.dir_var[var].printVariable()
    
    def repeatedVariables(self, id):
        for ids in self.dir_var:
            if id == ids:
                print('Variable :  ', id, " already exists")
                sys.exit()
                return True
        return False


class variable(object):
    def __init__(self, id, type):
        self.id = id
        self.type = type
    
    def printVariable(self):
        print("id =",self.id," tipo =",self.type)


class clases(object):
    def __init__(self, id, herencia):
        self.id = id
        self.herencia = herencia


class objeto(object):
    def __init__(self, id, type):
        self.id = id
        self.type = type

#Estructura de cuadruplos
class cuadruplo(object):
    def __init__(self, count, action, dirIzq, dirDer, result):
        self.count = count
        self.action = action
        self.dirIzq = dirIzq
        self.dirDer = dirDer
        self.result = result




