n = int(input())

def factorial(x):
    r = 1
    for i in range(1,x+1):
        r = i * r
    return r

s = 0
for i in range(n+1):
    s = s + factorial(i)

print(s)
