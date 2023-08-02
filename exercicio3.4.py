lado01 = int(input("Informe o 1o lado: "))
lado02 = int(input("Informe o 2o lado: "))
lado03 = int(input("Informe o 3o lado: "))

if (lado03 < lado01 + lado02) and (lado02 < lado01 + lado02) and (lado01 < lado02 + lado03):
    if(lado01 == lado02) and (lado02 == lado03):
        print("Triangulo Equilátero")
    elif((lado01 == lado02) and (lado01 != lado03)) or ((lado03 == lado02) and (lado02 != lado01)) or ((lado01 == lado03) and (lado01 != lado02)):
        print("Triângulo Isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Os valores informados não correspondem a um triâgulo")
