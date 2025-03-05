class Evento():
    def __init__(self,nomeEvento:str, local:str, descricao:str):
        self.nomeEvento = nomeEvento
        self.local = local
        self.descricao = descricao
        
    def __str__(self):
        return f" nome do evento: {self.nomeEvento} | local: {self.local} | descrição: {self.descricao}"
    

        
        
class Tarefa(Evento):
    def __init__(self, nomeEvento, local, descricao,TarefaDesejada,responsavel,prazo,status):
        super().__init__(nomeEvento, local, descricao)
        
        self.tarefasDesejada = TarefaDesejada
        self.responsavel = responsavel
        self.prazo = prazo
        self.status = status
        
    def aluguel(self,local):
        pagamento_aluguel = 2000
        
    def comida(self,comdaDesejada):
        pagamento_comida = 500
        
    def __str__(self):
        return f"nome: {self.nomeEvento} | Local: {self.local} | tarefa desejada: {self.tarefasDesejada} | responsavel: {self.responsavel} | prazo: {self.prazo} | status: {self.status}"

class Fornecedor(Evento):
    def __init__(self, nomeEvento, local, descricao, nomeFornecedor,servicoFornecido):
        super().__init__(nomeEvento, local, descricao)
        
        self.nomeFornecedor = nomeFornecedor
        self.servicoFornecido = servicoFornecido
        
        
    def __str__(self):
        return f"fornecedor: {self.nomeFornecedor} | serviço fornecido: {self.servicoFornecido}"
    
class responsavel(Evento):
    def __init__(self, nomeEvento, local, descricao,responsavelEvento):
        super().__init__(nomeEvento, local, descricao)
        
        self.responsavelEvento = responsavelEvento
    
    def __str__(self):
        return f"Evento: {self.nomeEvento} | responsavel pelo evento: {self.responsavelEvento}"
    
class Convidado(Evento):
    def __init__(self, nomeEvento, local, descricao, quantidadePessoas):
        super().__init__(nomeEvento, local, descricao)
    
        self.quantidadePessoas = quantidadePessoas
    def __str__(self):
        return f"Evento: {self.nomeEvento} | quantidade de pessoas: {self.quantidadePessoas}"
    
class Pagamento(Tarefa):
    def __init__(self, nomeEvento, local, TarefaDesejada):
        super().__init__(nomeEvento, local, TarefaDesejada)
        
    def realizarPagamento(self,valordisponivel,valorAluguel,valorTarefa):
        
        if valordisponivel > valorAluguel:
            print("Pagamento realizado do local")
        else:
            print("Pagemnto não realizado")
            
        if valordisponivel > valorTarefa:
            print(f"Pagmento realzado da {valorTarefa}")
        else:
            print("pagamento não foi realizado")
            
    def __str__(self):
        return f"nomeEvento: {self.nomeEvento} | realizando pagamento"
    
    
festa = Evento("Alyson's party", "Germany", "festa do meu querido alyson")
print(festa)

festa = Tarefa
        
    
        
            
        