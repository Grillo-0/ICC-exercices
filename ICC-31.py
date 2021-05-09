n = int(input())
conjunto = [0] * n

for i in range(n):
    conjunto[i] = int(input())

menor =conjunto[0]
for i in range(n):
    if conjunto[i] < menor:
        menor = conjunto[i]
pmaior = menor
smaior = menor

for i in range(n):
    if conjunto[i] >= pmaior:
        smaior = pmaior
        pmaior = conjunto[i]
    else:
        if conjunto[i] >= smaior:
            smaior = conjunto[i]

print(pmaior)
print(smaior)
