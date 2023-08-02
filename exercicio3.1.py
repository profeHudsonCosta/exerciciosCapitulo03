#Exercicio 3.1
v01 = int(input("Informe o 1o valor: "))
v02 = int(input("Informe o 2o valor: "))
v03 = int(input("Informe o 3o valor: "))

if (v01 < v02) and (v01 < v03):
    print("O menor valor é: ", v01)
elif (v02 < v03) and (v02 < v03):
    print("O menor valor é: ", v02)
else: 
    print("O menor valor é ", v03)
