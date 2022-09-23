def sacar(self, valor: float) -> None: # inicio do bloco do método

    if self.saldo >= valor: # inicio do bloco do if

        self.saldo -= valor

    # fim do bloco do if

# fim do bloco do método


def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("Retire o seu dinheiro na boca do caixa")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")

sacar(100)
