
# FOR

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print("\n")
    print("Executa no final do laço")




# RANGE
lista = list(range(4))
print(lista)


for numero in range (0, 11):
    print(numero, end=" ")
print("\n")


for numero in range(0, 51, 5):
    print(numero, end=" ")




# -----------------------------------------------------------------------------

# WHILE

opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Extrato...")
else:
     print("Obrigado por usar nosso sistema bancário")


# -----------------------------------------------------------------------------




# BREAK

while True:
    numero = int(input("Informa um numero: "))

    if numero == 100:
        break
    
    print(numero)


# nesse vai até 12
for numero in range(100):
    if numero == 12:
        break
    print(numero, end=" ")

# esse conta até 100, mas pula o 12
for numero in range(100):
    if numero == 12:
        continue
    print(numero, end=" ")