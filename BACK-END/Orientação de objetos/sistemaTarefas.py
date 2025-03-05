from datetime import datetime

class Tarefa ():
    def __init__(self,nomeTarefa:str, status:str, categoriaAtividade:str, dataVencimento: str):
        self.nomeTarefa = nomeTarefa
        self.status = status
        self.categoriaAtividade = categoriaAtividade
        self.dataVencimento = datetime.strptime(dataVencimento, "%d/%m/%Y")  # Convertendo para um objeto de data
        self.historico = {
            "Tarefa" : self.nomeTarefa,
            "Status" : self.status,
            "categoria" : self.categoriaAtividade,
            "dataVencimento" : self.dataVencimento
        }
        
    def criarAtividade(self):
        print("ATIVIDADE CRIADA")
        
    def editarAtividade(self, tarefaAtualizada, statusAtualizado, categoriaAtualizada, dataAtualizada):
        
        self.nomeTarefa = tarefaAtualizada
        self.status = statusAtualizado
        self.categoriaAtividade = categoriaAtualizada
        self.dataVencimento = datetime.strptime(dataAtualizada, "%d/%m/%Y")

        self.historico.update({
            "Tarefa": self.nomeTarefa,
            "Status": self.status,
            "Categoria": self.categoriaAtividade,
            "Data de Vencimento": self.dataVencimento.strftime("%d/%m/%Y")
        })
        
        print(f"✏️ ATIVIDADE '{self.nomeTarefa}' ATUALIZADA!")

        
        
    def removerAtividade(self):
        self.historico.clear()
        print("ATIVIDADE REMOVIDA")
        
    def exibindoAtividade(self):
        if self.historico:
            print("\n📌 Detalhes da Atividade:")
            for chave, valor in self.historico.items():
                print(f"{chave}: {valor}")
        else:
            print("Nenhuma atividade cadastrada.")
    
        
    def filtros(self, statusDesejado):
        if self.status == statusDesejado:
            self.exibindoAtividade()
        else:
            print(f"Nenhuma atividade encontrada com o status '{statusDesejado}'.")
        
    
    def __str__(self):
        return f"nome da tarefa: {self.nomeTarefa} | STATUS : {self.status}"
   
        

fimSemana = Tarefa(nomeTarefa="correr", status="em andamento", categoriaAtividade="esporte", dataVencimento="10/12/2009")
print(fimSemana)

fimSemana.criarAtividade()
fimSemana.editarAtividade(tarefaAtualizada="academia", statusAtualizado="finalizado" , categoriaAtualizada="esporte", dataAtualizada="01/12/2007")
fimSemana.filtros("finalizado")
fimSemana.exibindoAtividade()

