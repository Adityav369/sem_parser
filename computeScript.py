from preprocess import tokenizeAndFilter, seqLabel
from VarDecl import VarDecl
from Constraint import Constraint
from RelationParser import BinRelFunc
from printUtil import printFunc

# Set A, B
# Map f
# From(f, A, B)
# Bijection(f)
# AutoLabel All


def computeVardecls(labeled):
    # assuming name comes after key word, eg. "function f", "function called f", "set A" etc.
    entities = {"Set", "Function"}
    visitedEntity = []
    var_decls = []
    for i, label in enumerate(labeled):
        if label[0] in entities:
            visitedEntity.append(label[0])
            # not removing as that step is O(n), which makes the method quadratic time
            labeled[i] = -1
        elif label[1] == "name":
            # var_decls.append(VarDecl(label[0], visitedEntity[-1]))
            labeled[i] = VarDecl(label[0], visitedEntity[-1])
    return labeled


def computeConstraints(filtered):
    constraints = []
    for ent in filtered:
        if type(ent) is VarDecl:
            if ent.type == "Function":
                constraints = BinRelFunc(filtered, ent)
    return constraints


sent = input("Enter a string: ")
filtered = tokenizeAndFilter(sent)
labeled = seqLabel(filtered)
check = computeVardecls(labeled)
printFunc(computeConstraints(check))
