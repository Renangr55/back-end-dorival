class Biblioteca ():
    def __init__(self):
        self.livros = []
        self.quantidadeLivros = 0
    

    def cadastrandoLivros (self,tituloLivro):
        self.livros.append(tituloLivro)
        self.quantidadeLivros += 1
        print("________________")
        print(self.livros)
        return f"livro cadastrado - {tituloLivro}"

    def emprestimoLivro (self,pesquisandoLivro):
            if pesquisandoLivro in self.livros:
                self.livros.remove(pesquisandoLivro)
                self.quantidadeLivros -= 1
                print("________________")
                return f'Livro emprestado - {pesquisandoLivro}'
            else:
                print("livro não encontrado")
                
       

    def devolverLivro (self,devolvendoLivro):
        self.livros.append(devolvendoLivro)
        self.quantidadeLivros += 1
        print("________________")
        return f"Livro devolvido: {devolvendoLivro}"

    def verificarLivro (self):
        tituloLivro = input("escreva o nome do livro: ")
        if tituloLivro in self.livros:
            print(self.livros)
            return f"Esse livro está dísponível - {tituloLivro}"
        else:
            return f"esse livro não está disponível = {tituloLivro}"
        
    
    
    def __str__(self):
        return f'livros disponívels: {self.livros}'
    
firstUser = Biblioteca()


secondUser = Biblioteca()





print(firstUser.cadastrandoLivros("Cristo se fez presente"))
print(secondUser.cadastrandoLivros("Jesus sempre esteve conosco"))

print(firstUser.emprestimoLivro("Cristo se fez presente"))
print(secondUser.emprestimoLivro("Jesus sempre esteve conosco"))

print(firstUser.devolverLivro("Cristo se fez presente"))
print(secondUser.devolverLivro("Jesus sempre esteve conosco"))

print(secondUser.verificarLivro())
print(firstUser.verificarLivro())