n = int(input())
lista = list(map(int,input().split()))
desejo = int(input())

pos = -1
for i in range(n):
    if desejo == lista[i]:
        pos = i
        break

print(pos)
