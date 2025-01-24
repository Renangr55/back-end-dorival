class Produto ():
    def __init__(self,nome,preco,quantidadeEstoque):
        self.nome = nome
        self.preco = preco
        self.quantidadeEstoque = quantidadeEstoque
        
    def calculandoValorTotal (self):
        return self.preco * self.quantidadeEstoque
        
    def verificandoProduto(self):
        if self.quantidadeEstoque > 0:
            return 'Esse produto está disponível'
        else:
            return 'não temos esse produto no estoque'
        
    def __str__(self):
        return f'produto: {self.nome}, preço: {self.preco}, quantidade no estoque: {self.quantidadeEstoque}'
        

produtoUsuario = Produto("Chuteira",150,10) 

print(f"{produtoUsuario} Valor total em estoque: {produtoUsuario.calculandoValorTotal()} | status do pruduto: {produtoUsuario.verificandoProduto()}")
