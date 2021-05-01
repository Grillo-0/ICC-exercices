import math

# ENTRADA:
a = float(input())
b = float(input())
c = float(input())

# PROCESSAMENTO:
delta = b*b - 4 * a * c
if delta >= 0:
    res = - b / a
    print("%.2f" % res)
else:
    res="nan"
    print(res)
# SAIDA:
