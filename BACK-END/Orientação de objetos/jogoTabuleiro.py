class Tabuleiro:
    def __init__(self):
        print("Tabuleiro criado com 8x8 casas.")

    def colocar_pecas(self):
        print("Peças colocadas no tabuleiro:")
        # Peças Brancas
        print("- Peão branco na posição (6, 0)")
        print("- Peão branco na posição (6, 1)")
        print("- Peão branco na posição (6, 2)")
        print("- Peão branco na posição (6, 3)")
        print("- Peão branco na posição (6, 4)")
        print("- Peão branco na posição (6, 5)")
        print("- Peão branco na posição (6, 6)")
        print("- Peão branco na posição (6, 7)")

        print("- Torre branca na posição (7, 0)")
        print("- Torre branca na posição (7, 7)")

        print("- Bispo branco na posição (7, 1)")
        print("- Bispo branco na posição (7, 6)")

        print("- Cavalo branco na posição (7, 2)")
        print("- Cavalo branco na posição (7, 5)")

        print("- rainha branca na posição (7, 3)")
        print("- Rei branco na posição (7, 4)")




        # Peças Pretas
        print("- Peão preto na posição (1, 0)")
        print("- Peão preto na posição (1, 1)")
        print("- Peão preto na posição (1, 2)")
        print("- Peão preto na posição (1, 3)")
        print("- Peão preto na posição (1, 4)")
        print("- Peão preto na posição (1, 5)")
        print("- Peão preto na posição (1, 6)")
        print("- Peão preto na posição (1, 7)")

        print("- Torre branca na posição (0, 0)")
        print("- Torre branca na posição (0, 7)")

        print("- Bispo preto na posição (0, 1)")
        print("- Bispo preto na posição (0, 6)")

        print("- Cavalo preto na posição (0, 2)")
        print("- Cavalo preto na posição (0, 5)")

        print("- rainha branca na posição (0, 3)")
        print("- Rei preto na posição (0, 4)")
        
    def mostrar(self):
        print("\n📜 Estado atual do tabuleiro:\n")
        print("♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜")
        print("♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟")
        print("-  -  -  -  -  -  -  -")
        print("-  -  -  -  -  -  -  -")
        print("-  -  -  -  -  -  -  -")
        print("-  -  -  -  -  -  -  -")
        print("♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙")
        print("♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖\n")


class Peca:
    def __init__(self, cor_peca, posicao):
        self.cor_peca = cor_peca
        self.posicao = posicao

    def mover(self, nova_posicao):
        print(f"{self.__class__.__name__} {self.cor_peca} movido de {self.posicao} para {nova_posicao}")
        self.posicao = nova_posicao

class Peao(Peca):
    pass

class Torre(Peca):
    pass

class Bispo(Peca):
    pass

class Cavalo(Peca):
    pass

class Rainha(Peca):
    pass

class Rei(Peca):
    pass

tabuleiro = Tabuleiro()
tabuleiro.colocar_pecas()
tabuleiro.mostrar()

peao_branco = Peao("branco", (6, 0))
peao_branco.mover((5, 0))

print("Tabuleiro após o movimento:")
print("\n📜 Estado atual do tabuleiro:\n")
print("♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜")
print("♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟")
print("-  -  -  -  -  -  -  -")
print("-  -  -  -  -  -  -  -")
print("-  -  -  -  -  -  -  -")
print("-  -  -  -  -  -  -  -")
print("♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙")
print("♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖\n")
