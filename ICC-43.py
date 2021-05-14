n = int(input())
lista = list(map(int,input().split()))

listaInversa=[]
for i in range(n-1,-1,-1):
    listaInversa.append(lista[i])

for i in listaInversa:
    print(i,'',end='')
