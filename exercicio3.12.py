fat = 1
num = int(input("Informe um número natural positivo: "))

for num in range(num, 0, -1):
    fat = (num*fat)

print(fat)
