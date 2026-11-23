lista = []
comissoes = 0
for i in range(0, 12):
    comissao = int(input("Insira a comissao:"))
    lista.append(comissao)
    comissoes = comissoes + comissao

print(comissoes)