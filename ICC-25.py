n = int(input())
numeros = [0] * n

for i in range(n):
    numeros[i] = int(input())
maior = numeros[0]
menor = numeros[0]
soma = 0
for i in range(n):
    if numeros[i] > maior:
        maior = numeros[i]
    if numeros[i] < menor:
        menor = numeros[i]
    soma = soma + numeros[i]
print("{0}\n{1}\n{2}".format(maior,menor,soma))
