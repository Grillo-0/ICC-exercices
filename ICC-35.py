n = int(input())

def isPerfect(n):
    for i in range(n):
        cur = 2**(i-1)*(2**i-1)
        if cur == n:
            return 1
            break
        if cur > n:
            return 0
            break

if isPerfect(n):
    print("S")
else:
    print("N")
