num = int(input("Introduza um numero: "))

soma=1
cme = -1
while num != -1:
    num = int(input("Introduza um numero: "))
    soma = soma + num
    cme = cme + 1

media = soma / cme
print("resultado: ", media)
