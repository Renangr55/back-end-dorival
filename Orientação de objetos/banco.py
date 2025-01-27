class Banco():
    def __init__(self,nomeBanco):
        self.nomeBanco = nomeBanco
        self.Clientes = []
     

    def CadastrarClientes(self, id, nome, saldoCliente):
        self.id = id
        
        self.Clientes.append(
            {'id' : id,
            'nome' : nome,
            'Saldo do Cliente' : saldoCliente
            })

    def abrirConta (self, alternativa, valor,id_cliente, transferencia_de_Conta = None):
        operacao = self.Clientes[id_cliente]

                
        if alternativa == 1:
            operacao['Saldo do Cliente'] -= valor
            print(f'o {operacao["nome"]} agora tem: {operacao["Saldo do Cliente"]}')
     
        elif alternativa == 2:
            operacao['Saldo do Cliente'] += valor
            print(f'o {operacao["nome"]} agora tem: {operacao["Saldo do Cliente"]}')
       
        elif alternativa == 3 and id is not None:
            operacao['Saldo do Cliente'] -= valor
            transferencia_de_Conta = self.Clientes[transferencia_de_Conta]
            transferencia_de_Conta['Saldo do Cliente'] += valor
            print(f'o {operacao["nome"]} transferiu {valor} para: {transferencia_de_Conta["nome"]}')
                    


cliente = Banco("Bradesco")
usuario = Banco("Inter")


cliente.CadastrarClientes(0,"renan",50)
cliente.CadastrarClientes(1,"gabriel",80)

usuario.CadastrarClientes(0,"victor",80)
usuario.CadastrarClientes(1,"kaka",65)

cliente.abrirConta(1,10,0)
cliente.abrirConta(2, 20, 1) 
cliente.abrirConta(3, 30, 0, 1)