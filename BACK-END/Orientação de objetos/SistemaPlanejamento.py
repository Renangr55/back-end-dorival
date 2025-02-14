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
        
        
camisa = Produto("camisa" , 90.00 , 1 , 10)
print(camisa)
camisa.controleQuantidade(quantidadeAtualizada=50)

categoriaCamisa = Categoria("Roupa")
print(categoriaCamisa)


class Compra ():
    def __init__(self,produtoCompra):
        
        
        

adidas = Fornecedor("Adidas Brasil" , "Camisa Palmeiras 2023/2024")
adidas.adicionarProdutos()
print(adidas)
        
        
        
        

               
        