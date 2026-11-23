lista = []
for i in range(0, 10):
    numero = int(input("Insira um numero na lista:"))
    lista.append(numero)


menor = lista [9]

for numero in lista:
    if numero < menor:
       menor = numero

print(menor)
