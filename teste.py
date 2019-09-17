def condicional(v1, v2):
    if v1 and v2:
        return True
    elif v1 and not v2:
        return False
    else:
        return True

def bicondicional(v1,v2):
    if v1 and v2:
        return True
    elif v1 and not v2:
        return False
    elif not v1 and v2:
        return False
    else:
        return True

def conjuncao(v1, v2):
    if v1 and v2:
        return True
    else: 
        return False
        
def disjuncaoI(v1, v2):
    if not v1 and not v1:
        return False
    else:
        return True

def disjuncaoE(v1, v2):
    if (v1 and v2) or (not v1 and not v2):
        return False
    else:
        return True
arrV = []
v = int(input('Informe numero de variáveis: '))
for x in range(0, x):
    arrV.append(x)

