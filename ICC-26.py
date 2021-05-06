lados = [0] * 3
for i in range(3):
    lados[i] = int(input())

def isInv(lados):
    state = False
    for i in range(3):
        state = state or lados[i] + lados[(i+1)%3] < lados[(i+2)%3]
    return state
def isEq(lados):
    if lados[0] == lados[1] == lados[2]:
        return True
    else:
        return False
def isIso(lados):
    state = False
    for i in range(3):
        if lados[i] == lados[(i+1)%3]:
            state = True
    return state

if isInv(lados):
    print("INVALIDO")
else:
    if isEq(lados):
        print("EQUILATERO")
    else:
        if isIso(lados):
            print("ISOSCELES")
        else:
            print("ESCALENO")
