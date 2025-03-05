class Produto ():
    def __init__(self,nomeProduto:str,preco:float,codigoProduto:int,quantidade:int):
        self.nomeProduto = nomeProduto
        self.preco = preco
        self.codigoProduto = codigoProduto
        self.quantidade = quantidade
        self.ContadorEstoque = 0
        

    def controleQuantidade (self,quantidadeAtualizada):    
        self.quantidadeAtualizada = quantidadeAtualizada
        alteracaoQuantidade = self.quantidade + self.quantidadeAtualizada
        
        if alteracaoQuantidade < 0:
            print("não ha estoque suficiente para essa quantidade")
        else:
            print(f"quantidade informada {self.quantidade}, teve a atualização para {alteracaoQuantidade} ")   
            self.ContadorEstoque += alteracaoQuantidade    
            
    def __str__(self):
        return f'nome do produto: {self.nomeProduto}, código do Produto: {self.quantidade}'
    
class Categoria():
    def __init__(self,categoriaProduto:str):
        self.categoriaProduto = categoriaProduto
        
    def __str__(self):
        return f'a categoria do produto é {self.categoriaProduto}'

class Fornecedor():
    def __init__(self,nomeFornecedor:str, nomeProduto:str):
        self.nomeFornecedor = nomeFornecedor
        self.nomeProduto = nomeProduto
        self.estoque = []
        
    def adicionarProdutos (self):
        print(f"Produto fornecido por {self.nomeFornecedor}")
        self.estoque.append(self.nomeProduto)
        
        
    def __str__(self):
        return f"Produto: {self.nomeProduto} fornecido por {self.nomeFornecedor} "
        
        
class Compra(Fornecedor):
    def __init__(self,produto:str):
        self.produto = produto
      
        
    def comprando(self):
        if self.produto in self.estoque:
            self.estoque.remove(self.produto)
            print("realizado a compra")
        else:
            print("A compra não foi efetuada")
            
    def __str__(self):
        return f"você comprou um item: {self.produto}"
        
    
class Vendas ():
    def __init__(self, produto:str ,preco:float):
        self.produto = produto
        self.preco = preco
        
    def exibindoValor(self):
        self.precoAtualizada = self.preco + 60
        print(f"o preço do item é {self.precoAtualizada}")
        
        
    def __str__(self):
        return f"o nome do produto é: {self.produto} e elke vai ser vendido por um preço mais alto"
    

    
    
        
    
        
        



camisa = Produto("camisa" , 90.00 , 1 , 10)
print(camisa)
camisa.controleQuantidade(quantidadeAtualizada=50)

categoriaCamisa = Categoria("Roupa")
print(categoriaCamisa)    

comprandoProduto = Compra("Roupa")
print(comprandoProduto)
        
        
vendaProduto = Vendas("Roupa", 60.00)
print(vendaProduto)

vendaProduto.exibindoValor()

adidas = Fornecedor("Adidas Brasil" , "Camisa Palmeiras 2023/2024")
adidas.adicionarProdutos()
print(adidas)
        
        