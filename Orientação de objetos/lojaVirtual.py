class lojaVirtual():
    def __init__(self,nomeLoja):
        self.nomeLoja = nomeLoja
        self.produtos = []
       
    
    def cadastrarProduto (self, nomeProduto,preco):

            codigoDoProduto = len(self.produtos)
            
            self.dadosProduto ={
                "codigo" : codigoDoProduto,
                "Produto" : nomeProduto,
                "preço" : preco,
                
            }     
            
            self.produtos.append(self.dadosProduto) 
            
    def carrinho (self, escolhaProduto, quantidade, desconto=0):
        self.dadosCarrinho = self.dadosProduto
        self.valorTotal = self.produtos[escolhaProduto]['preço'] * quantidade - desconto
        
        self.dadosCarrinho.pop('codigo')
        self.dadosCarrinho.update({'quantidade': quantidade, 'Valor Total': self.valorTotal})
        
        return self.dadosCarrinho
    
    
    
loja = lojaVirtual('paracabauP')

loja.cadastrarProduto('tenis', 20)
loja.cadastrarProduto('chuteiora', 10)

print(loja.carrinho(1,10,1))