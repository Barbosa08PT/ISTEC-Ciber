saldoconta = int(input("Introduza o saldo da conta: "))
saldomov = int(input("Quanto quer movimentar: "))
saldoatual = saldomov + saldoconta

print("Saldo da conta: ", saldoconta)
print("Saldo movimentado: ", saldomov)
print("Saldo apos transação: ", saldoatual)

if saldoatual > 0:
    print("Operação concluida.")
else:
    print("Operação inválida. Saldo insuficiente")