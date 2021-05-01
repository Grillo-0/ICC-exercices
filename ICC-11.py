n = int(input())
res = 1

for i in range(2,n):
    if (n % i == 0):
        res = 0
        break
if n == 1:
    res = 0
print(res)
