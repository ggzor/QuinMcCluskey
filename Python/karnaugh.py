from collections import namedtuple

Assignation = namedtuple('Assignation', 'variable,value')
Combination = namedtuple('Combination', 'values')

def toCombination(vars, value):
    pass

def commonInCombinations(c1, c2):
    pass

def mintermToTruthTable(n, values):
    l = [False] * 2 ** n
    for i in values:
        l[i] = True
    return l