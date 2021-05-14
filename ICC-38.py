temperaturas = list(map(int,input().split()))

soma = 0
n = 0
for i in temperaturas:
    n += 1
    soma += i

media = soma/n
acimaMedia = 0

for i in temperaturas:
    if i > media:
        acimaMedia += 1

print(acimaMedia)
