n = int(input())

div = n
algarismos = [0]
while div > 0:
    algarismos.append(div % 10)
    div = div // 10

if len(algarismos) != 1:
    algarismos.pop(0)

for i in range(len(algarismos)):
    isnotPalindromo = algarismos[i] - algarismos[len(algarismos)-1-i]

if isnotPalindromo:
    print('N')
else:
    print('S')
