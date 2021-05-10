numero = int(input())

def func(x,n):
    return x * x * x + 3 * x * x + 2 * x - n

def dfunc(x):
    return 3 * x * x + 6 * x + 2

def consecutiveMultiplicaton(n):
    pchute = 0
    chute = n ** (1/3)

    while round(pchute,5) != round(chute,5):
        pchute = chute
        chute = chute - func(chute,n)/dfunc(chute)
    return round(chute,7)

n = consecutiveMultiplicaton(numero)
if n // 1 == n:
    print("S")
else:
    print("N")
