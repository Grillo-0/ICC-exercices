import math

l =  float(input())
a =  float(input())
c =  float(input())
m =  float(input())

area = l * a

latas = math.ceil(area / m)

preco = latas * c

print(f"{latas:.0f}\n{preco:.2f}")
