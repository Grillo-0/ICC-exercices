a = int(input())
b = int(input())
c = int(input())

r = 0

if a > b:
    r = a
else:
    r = b
if c > r:
    r = c

print(r)
