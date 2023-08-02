num = int(input("Informe um número inteiro positivo: "))
cont = num
cont2 = 0

while (cont > 0):
    resto = num % cont
    if (resto == 0):
        cont2 = cont2 + 1
    
    cont = cont - 1

if (cont2 > 2):
    print("O número ", num, "não é primo.")
    print("O número ", num, "é divisível por ", cont2, "números.")
else:
    print("O numero ", num, "é primo")
