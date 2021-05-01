# ENTRADA:
n = int(input())

# PROCESSAMENTO:
res = 0
for i in range(1,n+1):
    res += 1/i
# SAIDA:
print("%.4f"%res)
