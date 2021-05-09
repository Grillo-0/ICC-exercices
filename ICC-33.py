numero = int(input())

res = 0
for i in range(2,numero):
    if numero / (i * (i + 1)*(i+2)) == 1:
        res = i
        break

if res != 0:
    print("S")
else:
    print("N")
