# ENTRADA:
n = int(input())
m = int(input())

# PROCESSAMENTO:
res = 0
if (n > m):
    c = n
    n = m
    m = c
for i in range(n,m + 1):
    res += i
# SAIDA:
print(res)
