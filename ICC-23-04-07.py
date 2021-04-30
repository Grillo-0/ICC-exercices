# ENTRADA:
n = int(input())
c = int(input())
m = int(input())

# PROCESSAMENTO:
sac = int(n/c)
res = int(n/c)

while (sac >= m ):
    #print(sac,res)
    sag = int(sac/m)
    res += sag
    sac -= sag * m
    sac += sag

# SAIDA:
print(res)
