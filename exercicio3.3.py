val01 = int(input("Informe o 1o valor: "))
val02 = int(input("Informe o 2o valor: "))
val03 = int(input("Informe o 3o valor: "))

if (val01 < val02) and (val02 < val03):
    print(val01, " - ", val02, " - ", val03)
elif (val01 < val03) and (val03 < val02):
    print(val01, " - ", val03, " - ", val02)
elif (val02 < val01) and (val01 < val03):
    print(val02, " - ", val01, " - ", val03)
elif (val02 < val03) and (val03 < val01):
    print(val02, " - ", val03, " - ", val01)
elif(val03 < val01) and (val01 < val02):
    print(val03, " - ", val01, " - ", val02)
elif (val03 < val02) and (val02 < val01):
    print(val03, " - ", val02, " - ", val01)
