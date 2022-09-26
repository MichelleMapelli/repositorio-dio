curso = "pYtHon"
nome = "michelle LOPES TRigueiro"
espaco = "  Python "
curso1 = "Python"
texto = "   Olá mundo!      "

# Maiusculo
print(curso.upper())

# Minusculo
print(curso.lower())

# Titulo
print(curso.title())

# Eliminando espaços em branco  STRIP
print(espaco.strip())   # todo espaço
print(espaco.lstrip())  # esquerda
print(espaco.rstrip())  # direita

print(texto.strip() + ".")   # todo espaço
print(texto.lstrip() + ".")  # esquerda
print(texto.rstrip() + ".")  # direita


# Junções e centralizações de strings
print(curso1.center(10, "#"))
print(".".join(curso1))


for letra in curso1:
    print(letra, end="-")
print()
print("-".join(curso1))

