x = float(input())
v1 = float(input())
v2 = float(input())
a = float(input())

if a <= x:
    valor = v1*a
else:
    valor = a * v2

print("{0:.2f}".format(valor))
