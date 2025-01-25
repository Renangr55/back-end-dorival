class Banco():
    def __init__(self):
        self.pessoasCadastradas = 0
        self.Clientes = {
        }
     

    def CadastrarClientes(self, nome, rg, endereco, email):
        self.chave = (nome, rg, endereco, email)
        if self.chave not in self.Clientes:
            self.Clientes[self.chave] = True #adiconando os valoers na chave
            self.pessoasCadastradas += 1
            return F'{self. Clientes}'
        else:
            print("Deu errado")
    
    def exibirClientes (self):
       while True:
        for self.chave in self.Clientes:
            return f"Nome: {self.chave[0]}, RG: {self.chave[1]}, Endereço: {self.chave[2]}, Email: {self.chave[3]}"
        

    def abrirConta (self,nome, rg, endereco, email,tipoConta, valor = 100):
        self.valor = valor
        self.chave = (nome,rg,endereco,email)

        if self.chave in self.Clientes:
            numero_conta = f"Banco: {rg}, {nome}, {self.pessoasCadastradas}"

            conta = {
                "Tipo de conta" : tipoConta,
                "saldo" : valor
            }

            self.Clientes[numero_conta] = conta

            print(f"cliente do numero da conta {numero_conta}")
        else:
            print(f"{nome} não cadastrado")

    def operacoes(self):
        print("1 para sacar")
        print("2 para depositar")
        print("3 para transferencia")
        
        operacao = int(input("Digite um número: "))
        if operacao == 1:
            saque = int(input("Digite quanto você quer sacar: "))
            if saque < self.valor:
                operacaoSaque = self.valor - saque
                return f"você sacou,sua conta estava com {self.valor} e agora está com {operacaoSaque} e seu saque de {saque}, foi sucedida"
            else:
                print("erro")

        elif operacao == 2:
            depositando = int(input("Digite quanto você quer depositar: "))
            OperacaoDeposito = depositando + self.valor
            return f'Seu deposito ocorreu com sucesso: valor antigo {self.valor} e agora é {OperacaoDeposito},depois do seu depósito de {depositando} '
        

        elif operacao == 3:
            pessoa = input("Digite o nome da pessoa que você deseja fazer uma transferencia: ")
            if pessoa in self.Clientes:
                print("Conta verificada")
                transferencia = int(input("Digite o valor da transferência: "))
                if transferencia < self.valor:
                    return "transferência realizada"
                else:
                    return "deu errado"
                    



test = Banco()


test.CadastrarClientes("renan", 87293, "rua brasilia de pelotas", "manoqueraiva@gmail.com" )
test.CadastrarClientes("marian", 58393, "rua laurisca de franca", "finamente@gmail.com" )

print(test.abrirConta(nome="marian", rg=58393, endereco="rua laurisca de franca", email="finamente@gmail.com",tipoConta="Conta Corrente"))
print(test.abrirConta(nome="renan", rg=87293, endereco="rua brasilia de pelotas", email="manoqueraiva@gmail.com",tipoConta="Conta Corrente"))

print(test.operacoes())
print(test.exibirClientes())

