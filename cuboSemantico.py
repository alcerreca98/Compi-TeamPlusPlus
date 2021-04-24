# ------------------------------------------------------------
# Federico Alcerreca Treviño - A01281459
# Jaime Andres Montemayor Molina - A01176573
# ------------------------------------------------------------
import sys


# Declaracion de cubo semantico
class SemanticCube:
    def __init__(self):
        self.cube = {
            '+': {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'boolean': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
            },
            '-': {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'boolean': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
            },
            '/': {
                'int': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'boolean': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
            },
            '*': {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'boolean': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
            },
            '>': {
                'int': {
                    'int': 'boolean',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'float': {
                    'int': 'err',
                    'float': 'boolean',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'boolean': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
            },
            '<': {
                'int': {
                    'int': 'boolean',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'float': {
                    'int': 'err',
                    'float': 'boolean',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'boolean': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
            },
            '<=': {
                'int': {
                    'int': 'boolean',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'float': {
                    'int': 'err',
                    'float': 'boolean',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'boolean': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
            },
            '>=': {
                'int': {
                    'int': 'boolean',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'float': {
                    'int': 'err',
                    'float': 'boolean',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'boolean': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
            },
            '==': {
                'int': {
                    'int': 'boolean',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'float': {
                    'int': 'err',
                    'float': 'boolean',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'boolean': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'boolean',
                },
            },
            '!=': {
                'int': {
                    'int': 'boolean',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'float': {
                    'int': 'err',
                    'float': 'boolean',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'boolean': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'boolean',
                },
            },
            '&&': {
                'int': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'float': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'boolean': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'boolean',
                    'char': 'err',
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
            },
            '||': {
                'int': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'float': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
                'boolean': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'boolean',
                    'char': 'err',
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err',
                    'boolean': 'err',
                    'char': 'err',
                },
            }
        }
