nota1 = int(input("Valor nota 1: "))
nota2 = int(input("Valor nota 2: "))
nota3 = int(input("Valor nota 3: "))

media = ((nota1 + nota2 + nota3) /3)
mediap = ((nota1*0.25)+(nota2*0.35)+(nota3*0.40))

if mediap >= 9.5:
    print("Aprovado")

else:
    print("Reprovado")
