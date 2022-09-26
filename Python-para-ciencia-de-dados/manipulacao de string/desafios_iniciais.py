CONSUMO = 12
tempo, velocidade = input().split()

# Calcule quantidade de litros necessária para realizar a viagem e imprima com TRÊS dígitos após o ponto decimal
distancia = int(tempo) * int(velocidade)
litros = distancia / CONSUMO
print(f"{litros:.3f}")