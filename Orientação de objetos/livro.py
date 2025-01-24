class Livro ():
    def __init__(self,titulo,autor,numeroPagina):
        self.titulo = titulo
        self.autor = autor
        self.numeroPagina = numeroPagina
        self.livro = 1

    def emprestarLivro (self):
        emprestimo = input("você deseja pegar emprestado esse livro(sim/não): ")
        if emprestimo == "sim":
            self.livro -= 1
            return "livro emprestado com sucesso!!"
        else:
            print("Ok,volte sempre")
    
    def devolverlivro (self):
        devolver = int(input("quantas página você leu: "))
        if devolver == self.numeroPagina:
            self.livro += 1
            return "Livro devolvido !!!"
    
    def verficarLivro (self):
        if self.livro >= 1:
            return f"esse livro está dísponível"
        elif self.livro <= 1:
            return f"esse livro não está dísponível"
        else:
            print("Deu erro")
    
    def __str__(self):
        return f"título: {self.titulo} | autor:  {self.autor}| numero de páginas: {self.numeroPagina}"
    
livroUsuario = Livro("Segurança da informação", "PytonJavali", 90)
print(livroUsuario)

print(f"{livroUsuario.emprestarLivro()}")
print(f"{livroUsuario.devolverlivro()}")
print(f"{livroUsuario.verficarLivro()}")

