idades = []
n = 0

while n >= 0:
    n = int(input())
    idades += [n]

del idades[-1]
soma = 0
maiores = 0
idosas = 0
for i in idades:
    soma += i
    if i >= 18:
        maiores += 1
    if i > 75:
        idosas += 1
media = soma / len(idades)
porcentagem = idosas /  len(idades)

print("{0:.2f}\n{1}\n{2:.2f}%".format(media,maiores,porcentagem*100))

