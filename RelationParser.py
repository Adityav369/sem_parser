from VarDecl import VarDecl
from Constraint import Constraint


def findNextVarDecl(filtered):
    for ent in filtered:
        if type(ent) is VarDecl:
            return ent


def findPrevVarDecl(filtered):
    for ent in filtered:
        if type(ent) is VarDecl:
            return ent


def BinRelFunc(filtered, func_ent):
    binRelFunc = {"Injection", "Surjection", "Bijection"}
    # function contraint eg. Injection(f)
    fconstraint = Constraint()
    # Bin rel constraint eg. From(f, A, B)
    tconstraint = Constraint()
    for i, ent in enumerate(filtered):
        if type(ent) is VarDecl or type(ent) is int:
            continue
        if ent[0] in binRelFunc:
            fconstraint.func = ent[0]
            fconstraint.args.append(func_ent)
        elif ent[1] == "From":
            fromSet = findNextVarDecl(filtered[i:])
            tconstraint.func = "From"
            tconstraint.args.append(func_ent)
            tconstraint.args.append(fromSet)
        elif ent[1] == "To":
            to = findNextVarDecl(filtered[i:])
            tconstraint.args.append(to)
    return [fconstraint, tconstraint]


# def BinRelSet(func, filtered, setVarDecl):
#     Constraints = namedtuple('Constraints', ['name', 'args'])
#     fconstraint = Constraints(func, [funcVarDecl])
#     tconstraint = Constraints("From", [])
#     tconstraint.args.append(funcVarDecl)
#     for i, ent in enumerate(filtered):
#         if not type(ent) is tuple:
#             continue
#         if ent[1] == "From":
#             fromSet = findNextVarDecl(filtered[i:])
#             tconstraint.args.append(fromSet)
#         elif ent[i] == "To":
#             to = findNextVarDecl(filtered[i:])
#             tconstraint.args.append(to)
#     return [fconstraint, tconstraint]
