class MaquinaVendas():
    def __init__(self, nomeLoja):
        self.nomeLoja = nomeLoja
        self.listaProdutos = []

    def registrandoProdutos(self, nomeProduto, precoProduto, quantidadeProduto):
        
        codigoProduto = len(self.listaProdutos) 
        
        dadosProdutos = {
            'códigoProduto': codigoProduto,
            'nome': nomeProduto,
            'preço': precoProduto,
            'quantidade': quantidadeProduto  
        }
        self.listaProdutos.append(dadosProdutos)
        print(f"Produto {nomeProduto} registrado com sucesso!")

    def compraProdutos(self, codigoProduto, valorProduto, quantidadeComprada):
        for produto in self.listaProdutos:
            if produto['códigoProduto'] == codigoProduto: 
                if produto['quantidade'] >= quantidadeComprada: 
                    totalCompra = produto['preço'] * quantidadeComprada
                    if valorProduto >= totalCompra: 
                        troco = valorProduto - totalCompra
                        produto['quantidade'] -= quantidadeComprada 
                        print(f"Você comprou {quantidadeComprada} unidade(s) de {produto['nome']} por R${totalCompra:.2f}.")
                        print(f"Seu troco é: R${troco:.2f}")
                        print(f"Estoque atualizado: {produto['quantidade']} unidades de {produto['nome']} restantes.")
                        return
                    else:
                        print("Dinheiro insuficiente.")
                        return
                else:
                    print("Estoque insuficiente.")
                    return
        print("Produto não encontrado.")

    def sestoqueDisponivel(self):
        if not self.listaProdutos:
            print("A máquina de vendas está vazia.")
        else:
            print(f"Produtos disponíveis na {self.nomeLoja}:")
            for produto in self.listaProdutos:
                print(f"ID: {produto['códigoProduto']}, Nome: {produto['nome']}, Preço: R${produto['preço']:.2f}, Quantidade disponível: {produto['quantidade']}")


maquina = MaquinaVendas("Loja Virtual")

maquina.registrandoProdutos("Tênis", 100.0, 10)
maquina.registrandoProdutos("Chuteira", 120.0, 5)

maquina.sestoqueDisponivel()

maquina.compraProdutos(0, 500.0, 2)  
maquina.sestoqueDisponivel()