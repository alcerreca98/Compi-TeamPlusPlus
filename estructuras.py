# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------
import sys

#Estructura de Funcion
class funcion(object):
    """ Estructura de Funciones con atributos:

    id -> string con el nombre de la funcion

    type -> string con el tipo de la funcion

    dir_var -> Dictionary de variables locales de la funcion

    params -> Lista de parametros de la funcion
    
    """
    def __init__(self, id, type):#, vart):
        self.id = id
        self.type = type
        self.dir_var = {}
        self.params = []
    
    #Print de todos los atributos en la instancia de Funcion seleccionada
    def printFuncion(self):
        """ Print de todos los atributos en la instancia de Funcion seleccionada """
        print("\nid =", self.id, " tipo =", self.type)

    #getter de la tabla de variables de la función
    def getVarTable(self):
        """ getter de la tabla de variables de la función """
        return self.dir_var

    #Crea una instancia de variable y la agrega al directorio de variables de la funcion
    def addVar(self, id, type):
        """ Crea una instancia de variable y la agrega al directorio de variables de la funcion """
        self.dir_var[id] = variable(id, type)
    
    #Agrega el nombre del parametro a la lista de parametros
    def addParam(self, id):
        """ Agrega el nombre del parametro a la lista de parametros """
        self.params.append(id)
    
    #Busca los objetos variable segun los id's en la lista de parametros de la funcion y los imprime
    def printParams(self):
        """ Busca los objetos variable segun los id's en la lista de parametros de la funcion
         e imprime todos los atributos de cada variable"""
        tam = len(self.params)
        print("Params :")
        for p in range(tam) :
            var = self.dir_var.get(self.params[p])
            var.printVariable()

    #Imprime todos los atributos de cada uno de los objetos variable en la tabla de variables locales
    def printVarTable(self):
        """ Imprime todos los atributos de cada uno de los objetos variable en la tabla de variables locales """
        for var in self.dir_var:
            self.dir_var[var].printVariable()
    
    #Busca si hay dobles declaracones e imprime error si existen
    def repeatedVariables(self, id):
        """ Busca si hay dobles declaracones e imprime error si existen """
        for ids in self.dir_var:
            if id == ids:
                print('Variable :  ', id, " already exists in ", self.id)
                sys.exit()
                return True
        return False
    
    #Busca si al momento de llamar la variable ya este previamente declarada
    def searchIfExists(self, id):
        """ Busca si al momento de llamar la variable ya este previamente declarada """
        return self.dir_var.get(id, False)

#Estructura de Variables
class variable(object):
    """ Estructura de Variables """
    def __init__(self, id, type):
        self.id = id
        self.type = type

    #Print de todos los atributos en la instancia de Variable seleccionada
    def printVariable(self):
        """ Print de todos los atributos en la instancia de Variable seleccionada """
        print("id =",self.id," tipo =",self.type)

#Estructura de clases
class clases(object):
    """ Estructura de clases """
    def __init__(self, id, herencia):
        self.id = id
        self.herencia = herencia

#Estructura de objeto
class objeto(object):
    """ Estructura de objeto """
    def __init__(self, id, type):
        self.id = id
        self.type = type

#Estructura de cuadruplos
class cuadruplo(object):
    """ Estructura de cuadruplos """
    def __init__(self, cont, action, opIzq, opDer, result):
        self.cont = cont
        self.action = action
        self.opIzq = opIzq
        self.opDer = opDer
        self.result = result
    
    #Print de todos los atributos en la instancia de Cuadruplo seleccionada
    def printCuad(self):
        """ Print de todos los atributos en la instancia de Cuadruplo seleccionada """
        print(self.count,"\t",self.action,"\t",self.opIzq,"\t",self.opDer,"\t",self.result)




