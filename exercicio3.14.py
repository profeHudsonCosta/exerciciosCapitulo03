periodo = int(input("Informe o período do investimento: "))
taxa = float(input("Informe a taxa de juros aplicada: "))
valor = float(input("Informe o valor investido: "))
for x in range(periodo):
    print(x, "o mês")
    print("Juros simples: ")
    vf = valor * (1 + taxa * x)
    print(vf)

    print("Juros compostos: ")
    vf = valor * (1 + taxa)**x
    print(vf)
