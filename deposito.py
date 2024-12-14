class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        """
        Inicializa uma nova conta bancária.
        :param titular: Nome do titular da conta.
        :param saldo_inicial: Saldo inicial da conta, padrão é 0.
        """
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        """
        Deposita um valor na conta.
        :param valor: Valor a ser depositado.
        """
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        """
        Realiza um saque na conta, se houver saldo suficiente.
        :param valor: Valor a ser sacado.
        """
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente para o saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def exibir_saldo(self):
        """
        Exibe o saldo atual da conta.
        """
        print(f"Saldo atual: R${self.saldo:.2f}")


# Exemplo de uso
conta = ContaBancaria("João Silva", 500)
conta.exibir_saldo()
conta.depositar(200)
conta.exibir_saldo()
conta.sacar(100)
conta.exibir_saldo()
conta.sacar(700)