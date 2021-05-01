# ENTRADA:
a = int(input())
b = int(input())

# PROCESSAMENTO:
md = 1
d = 1

while (d != 0):
    d = a % b
    a = b
    b = d

# SAIDA:
print(a)
