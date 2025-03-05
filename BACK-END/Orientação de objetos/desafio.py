class Evento:
    def __init__(self, nomeEvento: str, local: str, descricao: str):
        self.nomeEvento = nomeEvento
        self.local = local
        self.descricao = descricao
        
    def __str__(self):
        return f"nome do evento: {self.nomeEvento} | local: {self.local} | descrição: {self.descricao}"


class Tarefa(Evento):
    def __init__(self, nomeEvento, local, descricao, TarefaDesejada, responsavel, prazo, status):
        super().__init__(nomeEvento, local, descricao)
        self.tarefasDesejada = TarefaDesejada
        self.responsavel = responsavel
        self.prazo = prazo
        self.status = status
        
    def __str__(self):
        return f"nome: {self.nomeEvento} | Local: {self.local} | tarefa desejada: {self.tarefasDesejada} | responsavel: {self.responsavel} | prazo: {self.prazo} | status: {self.status}"


class Fornecedor(Evento):
    def __init__(self, nomeEvento, local, descricao, nomeFornecedor, servicoFornecido):
        super().__init__(nomeEvento, local, descricao)
        self.nomeFornecedor = nomeFornecedor
        self.servicoFornecido = servicoFornecido
        
    def __str__(self):
        return f"fornecedor: {self.nomeFornecedor} | serviço fornecido: {self.servicoFornecido}"
    

class Responsavel(Evento):
    def __init__(self, nomeEvento, local, descricao, responsavelEvento):
        super().__init__(nomeEvento, local, descricao)
        self.responsavelEvento = responsavelEvento
    
    def __str__(self):
        return f"Evento: {self.nomeEvento} | responsável pelo evento: {self.responsavelEvento}"


class Convidado(Evento):
    def __init__(self, nomeEvento, local, descricao, quantidadePessoas: int):
        super().__init__(nomeEvento, local, descricao)
        self.quantidadePessoas = quantidadePessoas
    
    def __str__(self):
        return f"Evento: {self.nomeEvento} | quantidade de pessoas: {self.quantidadePessoas} convidados"


class Pagamento(Tarefa):
    def __init__(self, nomeEvento, local, descricao, TarefaDesejada, responsavel, prazo, status, pagamentoTarefa):
        super().__init__(nomeEvento, local, descricao, TarefaDesejada, responsavel, prazo, status)
        self.pagamentoTarefa = pagamentoTarefa
        
    def realizarPagamento(self, valordisponivel: int, valorTarefa: int):
        if valordisponivel >= valorTarefa:
            print("Pagamento realizado da tarefa")
        else:
            print("Pagamento não realizado")
            
    def __str__(self):
        return f"nome de Evento: {self.nomeEvento} | realizando pagamento: {self.pagamentoTarefa}" 


festa = Evento("Alyson's party", "Germany", "festa do meu querido Alyson")
print(festa)

festa = Tarefa("Alyson's party", "Germany", "festa do meu querido Alyson", "alugar um espaço", "Renan", "em andamento", "22/01/2025")
print(festa)

festa = Fornecedor("Alyson's party", "Germany", "festa do meu querido Alyson", "Seara", "churrasco")
print(festa)

festa = Responsavel("Alyson's party", "Germany", "festa do meu querido Alyson", "Lucca Dias")
print(festa)

festa = Convidado("Alyson's party", "Germany", "festa do meu querido Alyson", 100)
print(festa)

festa = Pagamento("Alyson's party", "Germany", "festa do meu querido Alyson", "alugar um espaço", "Renan", "em andamento", "22/01/2025", "pagamento da alimentação")
print(festa)

festa.realizarPagamento(5000, 400)