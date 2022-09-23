# A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

import sys


saldo = 2000.0
saque = float(input("Informa o valor do saque: "))

if saldo >= saque:
    print("Realizado o saque com sucesso!")

if saldo < saque:
    print("O seu saldo é insuficiente")





saldo = 2000.0
saque = float(input("Informa o valor do saque: "))

if saldo >= saque:
    print("Realizado o saque com sucesso!")

else:
    print("O seu saldo é insuficiente")





opcao = int(input("Informa uma opcao: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
    # ...
elif opcao == 2:
    print("Exibindo extrato...")
else:
    sys.exit("Opção inválida")





    