x1 = int(input())
v1 = int(input())
x2 = int(input())
v2 = int(input())

if v1 != v2:
    res = (x1 - x2)/(v2-v1)
else:
    res = -1

if res >= 0 and res == int(res) or x1 == x2:
    print("SIM")
else:
    print("NAO")
