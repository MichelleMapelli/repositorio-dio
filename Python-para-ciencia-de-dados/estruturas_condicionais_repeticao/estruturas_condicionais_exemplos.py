
MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("informe a sua idade: "))

if idade >= 18:
    print("Pode tirar a CNH")
if idade < 18:
    print("Ainda não pode tirar a CNH")


# ----------------------------------------------------------------------------


idade = int(input("informe a sua idade: "))

if idade >= 18:
    print("Pode tirar a CNH")
else:
    print("Ainda não pode tirar a CNH")



idade = int(input("informe a sua idade: "))

if idade >= 18:
    print("Pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricase não as práticas")
else:
    print("Ainda não pode tirar a CNH")

conta_normal = False
conta_universitaria = True
saldo = 2000
saque = 500
cheque_especial = 450


# ----------------------------------------------------------------------------


if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Sque realizado com uso do cheque especial")
    else:
        print("Não foi possivel realizar o saque")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente")
else:
    print("Sistema não reconheeu seu tipo de conta, entre em contato com o gerente")



# ----------------------------------------------------------------------------

saldo = 500
saque = 300

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")






