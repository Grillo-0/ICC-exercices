n = int(input())
conjunto = [0] * n

for i in range(n):
    conjunto[i] = int(input())

pri = conjunto[1]
seg = conjunto[0]
estado = 0
adicional = 0

for i in range(n-1):
    if seg < pri:
        estado = estado + 5
    elif seg == pri:
        adicional = adicional + 1
    else:
        estado =  estado - 1
    if i + 2 != n:
        seg = pri
        pri = conjunto[i + 2]

if estado == 5 * (n - 1 - adicional):
    print(1)
else:
    if estado == -n + 1 + adicional:
        print(-1)
    else:
        print(0)
