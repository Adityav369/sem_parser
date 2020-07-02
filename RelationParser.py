from VarDecl import VarDecl
from Constraint import Constraint

def lookForVarDeclWithName(ent, filtered):
    if type(ent)==VarDecl:
        return ent
    else:
        for i in filtered:
            if type(i)==VarDecl and i.name==ent[0]:
                return i

def findNextVarDecl(filtered):
    for ent in filtered:
        if type(ent) is VarDecl:
            return ent


def findPrevVarDecl(filtered):
    filtered = reversed(filtered)
    for ent in filtered:
        if type(ent) is VarDecl:
            return ent

def find2PrevVarDecl(filtered):
    l = []
    for ent in filtered:
        if len(l)==2:
            return l
        if type(ent) is int:
            continue
        elif type(ent) is VarDecl or ent[1] == "declaredBefore":
            l.append(lookForVarDeclWithName(ent, filtered))
    return l


def findNext2VarDecl(filtered):
    l = []
    for ent in filtered:
        if len(l)==2:
            return l
        if type(ent) is int:
            continue
        elif type(ent) is VarDecl or ent[1] == "declaredBefore":
            l.append(lookForVarDeclWithName(ent, filtered))
    return l

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

def BinRelVec(filtered, func_ent):
    binRelVec = {"In", "Orthogonal"}
    operations = {"+", "=", "-"}
    constraints = []
    for i, ent in enumerate(filtered):
        if type(ent) is VarDecl or type(ent) is int:
            continue
        if ent[1] in binRelVec:
            c = Constraint()
            c.func = ent[1]
            vec, space = find2PrevVarDecl(filtered[:i])
            c.args.append(vec)
            c.args.append(space)
            constraints.append(c)
        if ent[0] in binRelVec:
            c = Constraint()
            c.func = ent[0]
            vec1, vec2 = find2PrevVarDecl(filtered[:i])
            c.args.append(vec1)
            c.args.append(vec2)
            constraints.append(c)
        if ent[0] in operations:
            if ent[0]=="=":
                #exp = s1 + s2
                exp = findPrevVarDecl(filtered[:i])
                s1, s2 = findNext2VarDecl(filtered[i+1:])
                c = Constraint()
                c.func = "Sum"
                c.args = [exp, s1, s2]
                constraints.append(c)
    return constraints



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
