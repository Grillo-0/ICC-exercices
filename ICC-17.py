a = int(input())
b = int(input())

def multiply(a,b):
    r = 0
    if a > b:
        c = b
        b = a
        a = c
    for i in range(a):
        r = r + b
    return r

r = 1

for i in range(b):
        r = multiply(r,a)

print(r)
