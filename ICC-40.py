n = int(input())
lista = list(map(int,input().split()))

maior = -float('inf')
pos = 0

for i in range(n):
    if lista[i] > maior:
        maior = lista[i]
        pos = i

print(maior)
print(pos)
