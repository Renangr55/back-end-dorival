class RedeSocial():
    def __init__(self):
        self.listaAmigos = []

    def adicionandoAmigos(self):
        tamanhoLista = 10
        nome = input("Digite o nome do seu amigo: ")
        opcao = input("Deseja adicionar mais amigos: ")
        
            
            self.listaAmigos.append(nome)
            
        print(self.listaAmigos)

    def publicarMensagens(self):
        mensagem = input("Digite sua mensagem")
        print(f'{mensagem} foi publicada')

    def comentarioPost(self):
        comentandoPost = input("Digite o seu comentário: ")
        print(f'você comentou no post {comentandoPost}')

    def pesquisaDeUsuario(self):
        pesquisarUsuario = input("Digite o usuário que vcocê deseja pesquisar: ")
        
        for amigos in self.listaAmigos:
            if amigos == pesquisarUsuario:
                print('usuario encontrado')
            else:
                print('usuário não encontrado')

social_network = RedeSocial()

social_network.adicionandoAmigos()

social_network.publicarMensagens()

social_network.comentarioPost()

social_network.pesquisaDeUsuario()