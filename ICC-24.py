n = int(input())
numeros = [0] * n

for i in range(n):
    numeros[i] = int(input())
maior = numeros[0]
for i in range(n):
    if numeros[i] > maior:
        maior = numeros[i]
print(maior)
