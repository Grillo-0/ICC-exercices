l = int(input())
m = float(input())
a = float(input())
v = int(input())

total = 0

if v > l:
    total = m + a * (v - l)

print("{0:.2f}".format(total))
