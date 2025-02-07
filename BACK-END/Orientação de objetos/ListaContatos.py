class Agenda ():
    def __init__(self,nome):
        self.nome = nome
        self.contatos = []
        
    def adicionar(self):
        self.adicionandoNome = input("Digite o nome da pessoa que você deseja adicionar: ")
        self.adicionandoNumeros = int(input("Insira o número telefônico: "))
        self.nomelista = self.adicionandoNome
        self.numeroLista = self.adicionandoNumeros
        informacoesContatos = (self.nomelista,self.numeroLista)
        self.contatos.append(informacoesContatos)
        print("Contato Adicionado")
        print(self.contatos)
        
    def Editar (self):
        editarNome = input("Digita um nome: ")
        
        for i,contatos in enumerate(self.contatos):
            if contatos[0] == editarNome:
                novoNumero = int(input("Digite o número novo: "))
                self.contatos[i] = (editarNome, novoNumero)
                print("Número adicionado com sucesso")
                break
            else:
                print("contato não adcionado")
  
        
        
    def remover(self):
        removendoContato = input("Digite o nome que você deseja remover: ")
        
        for i,contatos in enumerate(self.contatos):
            if contatos[0] == removendoContato:
                print("Contato removido")
                self.contatos.pop(i)
                return
        
        print("Contato não removido")
    
    def __str__(self):
        return f"{self.contatos}"
    
    
contato1 = Agenda('renan')


contato1.adicionar()
contato1.Editar()
contato1.remover()
print(contato1)

        
        
        