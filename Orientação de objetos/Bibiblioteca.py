class Biblioteca ():
    def __init__(self):
        self.livros = []
        self.quantidadeLivros = 0

    def cadastrandoLivros (self):
        tituloLivro = input("Digite o título do livro: ")
        idLivro = int(input("Digite o código do livro: "))
        infomacoesLivros = (tituloLivro, idLivro)
        self.livros.append(infomacoesLivros)
        self.quantidadeLivros += 1
        return "livro cadastrado"

    def emprestimoLivro (self):
        procurandolivro = input("Digite o nome do livro: ")
        for i in self.livros:
            if i == procurandolivro:
                print("Livro emprestado")
                self.livros.pop[procurandolivro]
            else:
                print("livro não encontrado")

    def devolverLivro (self):
        devolvendoLivro = input("Digite o título do livro: ")
        self.livros.append(devolvendoLivro)
        self.quantidadeLivros += 1

    def verificarLivro (self):
        verificandoLivro = input("Digite o título do livro: ")
        for i in self.livros:
            if verificandoLivro == self.livros:
                print("Esse livro está dísponível")
            else:
                print("Esse livro não está dísponível")
    
    def __str__(self):
        return f'livros disponível: {self.livros}'
    
cliente = Biblioteca()
print(cliente)

print(cliente.cadastrandoLivros())
print(cliente.emprestimoLivro())
print(cliente.devolverLivro())
print(cliente.verificarLivro())