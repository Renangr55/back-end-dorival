class ContaBancária ():
    def __init__(self, numeroConta, nomeTitular, saldo):
        self.numeroConta = numeroConta
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def sacar (self):
        sacarValor = int(input("Digite o valor que você deseja sacar: "))
        if sacarValor < self.saldo:
            recebimento = self.saldo - sacarValor
            print(f"pedido realizado {recebimento}")
        else:
            if sacarValor > self.saldo:
                print( f"Saldo insuficiente")
            else:
                print( f"informações erradas")

    def depositar (self):
        depositarValor = int(input('Escolha um valor para depositar: '))
        if depositarValor < self.saldo:
            depositando = self.saldo - depositarValor
            print(f"Deposito feito com sucesso {depositando}")
        else:
            print( f" Ops...Deu erro")      
    def __str__(self):
        print( f"Seja bem vindo {self.nomeTitular},numero da sua conta {self.numeroConta} e seu saldo disponível é {self.saldo}")
        
        
renan = ContaBancária(100304, "Renan Gabriel Rodrigues Mendonça", 500)
print(renan)

ContaBancária.sacar(renan)
