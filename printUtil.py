from VarDecl import VarDecl
from Constraint import Constraint


def printFunc(labeled):
    print("----------")
    for i in labeled:
        if i == -1:
            continue
        elif type(i) == VarDecl:
            print("VarDecl of type:", i.type, "and name:", i.name)
        elif type(i) == Constraint:
            print(i.func)
            printEachVarDecl(i.args)
            print("----------")
        else:
            print(i)


def printEachVarDecl(args):
    for i in args:
        print(i.type, i.name)
