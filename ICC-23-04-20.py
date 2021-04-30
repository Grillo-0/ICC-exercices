idade = int(input())

if idade >= 16 and idade <= 17:
    print("FACULTATIVO")
else:
    if idade >= 18 and idade <= 69:
        print("OBRIGATORIO")
    else:
        print("DISPENSADO")
