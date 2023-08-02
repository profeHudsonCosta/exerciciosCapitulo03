num = 0
soma = 0
cont = 0
maior = 0
menor = 0

while (num >= 0):
    num = int(input("Informe um número inteiro positivo ou -1 para encerrar o laço: "))
    if (cont == 0):
        menor = num

    if (num >= 0):
        cont = cont + 1
        soma = soma + num
        if (num > maior):
            maior = num
        if (num < menor):
            menor = num

media = soma/cont

print("Soma dos números inseridos: ", soma)
print("Média dos números inseridos: ", media)
print("Maior número inserido: ", maior)
print("Menor número inserido: ", menor)
