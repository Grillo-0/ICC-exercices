n = int(input())
res = 0

def isPrime(n):
    b = 1
    for i in range(2,n):
        if (n % i == 0):
            b = 0
            break
    if n == 1:
        b = 0
    return b

for i in range(n+1):
    if isPrime(i):
        res += i

print(res)
