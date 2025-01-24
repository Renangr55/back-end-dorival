class ContaBancária ():
    def __init__(self, numeroConta, nomeTitular, saldo):
        self.numeroConta = numeroConta
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def sacar (self):
        self.saque = int(input("Digite o valor que você deseja sacar: "))
        if self.saque < self.saldo:
            self.recebimento = self.saldo - self.saque
            return f"pedido realizado,seu saldo foi de {self.saldo} para {self.recebimento}"
        else:
            if self.saque > self.saldo:
                return f"Saldo insuficiente"
            else:
                return f"informações erradas"

    def depositar (self):
        depositarValor = int(input('Escolha um valor para depositar: '))
        depositando = self.recebimento + depositarValor
        return f"Deposito feito com sucesso,seu saldo era {self.recebimento} e com o seu deposito ficou {depositando}"
    

    def __str__(self):
        return f"Seja bem vindo {self.nomeTitular},numero da sua conta {self.numeroConta} e seu saldo disponível é {self.saldo}"
        
        
renan = ContaBancária(100304, "Renan Gabriel Rodrigues Mendonça", 500)
print(renan)

print(f"{renan.sacar()}")
print(f"{renan.depositar()}")
