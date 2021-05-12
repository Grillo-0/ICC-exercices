n = int(input())

def divFinder(n):
    div = [0] * 1000
    for i in range(n - 1):
        d = i + 1
        if n % d == 0:
            div[i] = d
    return div

if n == sum(divFinder(n)):
    print("S")
else:
    print("N")
