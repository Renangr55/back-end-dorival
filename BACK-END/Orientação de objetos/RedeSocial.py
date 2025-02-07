class RedeSocial():
    def __init__(self,nome):
        self.listaAmigos = []
        self.nome = nome

    def adicionandoAmigos(self):
        quantidadeAmigos = int(input("Digite a quantidade de amigos que você deseja adicionar: "))
        if quantidadeAmigos > 1:
            for i in range(quantidadeAmigos):
                nome_amigos = input("Digite o nome do seu amigo: ")
                self.listaAmigos.append(nome_amigos)
            
                
        else:
            nome_amigos = input("Digite o nome do seu amigo: ")
            self.listaAmigos.append(nome_amigos)
            return self.listaAmigos
        
            
            
        return self.listaAmigos

    def publicarMensagens(self):
        mensagem = input("Digite sua mensagem: ")
        return f'"{mensagem}": sua mensagem foi publicada'

    def comentarioPost(self):
        comentandoPost = input("Digite o seu comentário: ")
        return f'você comentou no post = {comentandoPost}'

    def pesquisaDeUsuario(self):
        pesquisarUsuario = input("Digite o usuário que vcocê deseja pesquisar: ")
        
        for i in self.listaAmigos:
            if i == pesquisarUsuario:
                return 'usuario encontrado'
            
        return 'usuário não encontrado'



primeiroUsuario = RedeSocial("Renan")

print(primeiroUsuario.adicionandoAmigos())

print(primeiroUsuario.publicarMensagens())

print(primeiroUsuario.comentarioPost())

print(primeiroUsuario.pesquisaDeUsuario())