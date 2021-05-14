n = int(input())
lista = list(map(int,input().split()))
desejo = int(input())

ocorrencias = 0
for i in range(n):
    if desejo == lista[i]:
        ocorrencias += 1

print(ocorrencias)
