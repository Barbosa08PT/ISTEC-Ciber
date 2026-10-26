num1=int(input("numero 1:  "))
num2=int(input("numero 2:  "))

operacao = input("Operação aritmetica: ",)


if operacao == "+":
    soma = num1 + num2
    print("O resultado da soma é", soma)

if operacao == "-":
   sub = num1 - num2
   print("O resultado da soma é", sub)

if operacao == "*":
   mult = num1 * num2
   print("O resultado da soma é", mult)

if operacao == "/":
   div = num1 / num2
   print("O resultado da soma é", div)

else:
     print(f"erro: {operacao} nao reconhecido")



