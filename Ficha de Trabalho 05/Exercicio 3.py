lista = []
for i in range(0, 10):
    numero = int(input("Insira um numero na lista:"))
    lista.append(numero)


maior = lista [0]

for numero in lista:
    if numero > maior:
       maior = numero

print(maior)