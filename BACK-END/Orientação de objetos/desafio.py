class Evento():
    def __init__(self,nomeEvento:str, local:str, descricao:str):
        self.nomeEvento = nomeEvento
        self.local = local
        self.descricao = descricao
        
    def __str__(self):
        return f" nome do evento: {self.nomeEvento} | local: {self.local} | descrição: {self.descricao}"
    

        
        
class Tarefa():
        