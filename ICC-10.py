a = 1
l = []
while a != 0:
    a=int(input())
    l.append(a)

print(sum(a for a in l if a % 2 == 0))
print(sum(a for a in l if a % 2 != 0))
print(sum(l))
