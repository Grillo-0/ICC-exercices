n = int(input())

div = n
soma = 0

while div != 0:
    soma = soma + div % 10
    div = div // 10

print(soma)
