salario=int(input("Introduza um salario:  "))

if salario <= 15000:
    taxa20 = salario * 0.2
    print("paga taxa de 20% =", taxa20)
else:
    if salario <= 20000:
        taxa30 = salario * 0.3
        print("paga taxa de 30% =", taxa30)
    else:
        if salario <= 25000:
            taxa35 = salario * 0.35
            print("paga taxa de 35% =", taxa35)
        else:
            if salario > 25000:
                taxa40 = salario * 0.4
                print("paga taxa de 40%", taxa40)