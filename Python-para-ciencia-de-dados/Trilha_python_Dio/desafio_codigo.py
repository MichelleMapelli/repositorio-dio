# Desafio 1

letra = input() 

import string
alfabeto = [0]
alfabeto.extend(list(string.ascii_uppercase[::]))
print(alfabeto.index(letra))



# Desafio 2


while True: 
    try: 
        pernas = input()
        if pernas == "esquerda": 
            print("ingles")
            
        elif pernas == "direita":
            print("frances")
            
        elif pernas == "nenhuma":
            print("portugues")
            
        elif pernas == "ambas":
            print("caiu")
            
        else:
            print("Nenhuma das anteriores")
            
    except EOFError: 
        break


# Desafio 3

salario = int(input()) 

if (salario >= 0 and salario <= 600.00):
    reajuste = 0.17
elif (salario >= 600.01 and salario <= 900.00):
    reajuste = 0.13
elif (salario >= 900.01 and salario <= 1500.00):
    reajuste = 0.12
elif (salario >= 1500.01 and salario <= 2000.00):
    reajuste = 0.10
else:
    reajuste = 0.5

percentual = int(reajuste * 100)
reajuste_ganho = salario * reajuste
novo_salario = (salario + reajuste_ganho)

print('Novo salario:',"{:.2f}".format(novo_salario))
print('Reajuste ganho:',"{:.2f}".format(reajuste_ganho))
print('Em percentual: {} %'.format(percentual))
