import math 

a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))

if (a != 0):
    delta = b**2 - 4*a*c
    print("O delta vale: ", delta)
    if (delta > 0):
         x1 = int((-b - math.sqrt(delta))/2*a)
         x2 = int((-b + math.sqrt(delta))/2*a)

         print("As raizes da equação são: ")
         print("X1: ", x1)
         print("X2: ", x2)
    elif (delta == 0):
         x = int((-b + math.sqrt(delta))/2*a)
         print("A raíz da equação é: ", x)
    else:
        print("Não há raizes reais para a equação!")
else:
        print("Valores não pertencem a uma equação do 2o Grau")
