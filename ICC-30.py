anos = int(input())
alturas = [0] * anos

for i in range(anos):
    alturas[i] = int(input())

altmax = 0
for i in range(anos):
    if alturas[i] > altmax:
        altmax = alturas[i]

apagadas = 0
for i in range(anos):
    if altmax == alturas[i]:
        apagadas = apagadas + 1

print(apagadas)
