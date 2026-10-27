num1 = int(input("Valor 1: "))
num2 = int(input("Valor 2: "))
num3 = int(input("Valor 3: "))

if num1 <= num2:
    if num1 <= num3:
        menor = num1
    else:
        menor = num3

else:
    if num2 <= num3:
        menor = num2
    else:
        menor = num3

print("O menor número é: ", menor)
