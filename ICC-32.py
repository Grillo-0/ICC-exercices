n = int(input())
conjunto = [0] * n

for i in range(n):
    conjunto[i] = int(input())

pri = conjunto[1]
seg = conjunto[0]
estado = 0

for i in range(2,n):
    if seg <= pri:
        estado = estado + 1
    else:
        estado =  estado - 1
    seg = pri
    pri = conjunto[i]

if estado == n - 2:
    print(1)
else:
    if estado == -n + 2:
        print(-1)
    else:
        print(0)
