n = int(input())

def fibo(n):
    a = 1
    b = 1
    c = 0
    for i in range(n):
        c = a
        a += b
        b = c
    return b

for i in range(n):
    print(fibo(i),'',end='')
