a = int(input())
b = int(input())

r = 0

if a > b:
    c = b
    b = a
    a = c

for i in range(a):
    r = r + b

print(r)
