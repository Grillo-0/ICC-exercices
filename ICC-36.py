n = int(input())
lista = list(map(int,input().split()))

maxSeq = 1
curSeq = maxSeq
antes = lista[0]
for i in range(1,n):
    if lista[i] >= antes:
        curSeq += 1
    else:
        curSeq = 1
    if curSeq > maxSeq:
        maxSeq = curSeq
    antes = lista[i]

print(maxSeq)

