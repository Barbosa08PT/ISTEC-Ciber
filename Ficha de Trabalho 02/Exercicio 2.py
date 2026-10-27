salario=int(input("Introduza um salario:  "))

if salario <= 15000:
    taxa20 = salario * 0.2
    print("paga taxa de 20% =", taxa20)

else:
    taxa30 = salario * 0.3
    print("paga taxa de 30% =", taxa30)



