#Construa uma aplicação de e-commerce onde produtos, clientes e pedidos são 
#objetos. Adicione funcionalidades como carrinho de compras, desconto, cálculo de 
#frete, histórico de compras e recomendação de produtos com base nas compras 
#anteriores

class Ecommerce:
    def __init__(self,nomeEcommerce):
        self.nomeEcommerce = nomeEcommerce
        print(f"Eccomerce criado {self.nomeEcommerce}")


class Produtos:
    def __init__(self,nomeProduto:str,preco:float,id:int):
        self.nomeProduto = nomeProduto
        self.preco = preco
        self.id = id
        self.carrinho = []
        self.produtoDisponivel = []
        

    def exibirProdutoDisponivel (self):
        self.produto = [self.nomeProduto,self.preco,self.id]
        self.produtoDisponivel.append(self.preco)
        print(self.produto)

    def exibirCarrinho(self):
        self.carrinho.append(self.produto)  
        print(f"exibindo seu carrinho: {self.carrinho}") 



        

class Clientes:
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade

    

class Pedido:
    def __init__(self,produtoCliente:str):
        self.produtoCliente = produtoCliente
       

    def verificandoPedido(self, produto):
        if self.produtoCliente == produto.produtoDisponivel:
            return "Esse produto tem no estoque"

        return "Produto adicionado no carrinho"
        

    def calculoFrete(self,endereco, produto):
        self.endereco = endereco
        print(f"Você mora em {endereco} ")
        self.frete = 100.00
        self.precoAtualizado = produto.preco + self.frete
        return self.precoAtualizado

    

    def __str__(self):
        return f'sua compra foi bem sucedida'
        
    

class desconto(Pedido):
    def __init__(self):
        print("você recebeu um desconto ")

    def descontoAplicado (self):
        self.desconto = 0.10
        self.precoAtualizado = self.precoAtualizado - self.desconto
        return self.precoAtualizado
        

        
        
tenisBar = Ecommerce("Tenis Bar")

tenisVremelho = Produtos(nomeProduto="tenis" , preco=190.00, id=10 )
tenisVremelho.exibirProdutoDisponivel()
tenisVremelho.exibirCarrinho()



macharete = Clientes("Rafael" , 15)

pedidoMacharete = Pedido("tenis")
print(pedidoMacharete)
print(pedidoMacharete.verificandoPedido(tenisVremelho))
print(pedidoMacharete.calculoFrete("sumaré", tenisVremelho))


