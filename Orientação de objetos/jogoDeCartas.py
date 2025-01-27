import random

class JogoCartas:
    def __init__(self):
        self.cartas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.jogadores = {} 
        
    def embaralhar(self):
        random.shuffle(self.cartas)
        
    def distribuir_cartas(self, jogador, numero_cartas):
        if jogador not in self.jogadores:
            self.jogadores[jogador] = []
        for _ in range(numero_cartas):
            if self.cartas:
                self.jogadores[jogador].append(self.cartas.pop())
                
    def jogar(self, jogador, carta):
        if carta in self.jogadores.get(jogador, []):
            self.jogadores[jogador].remove(carta)
            print(f"\n{jogador} jogou a carta {carta}")
        else:
            print(f"\n{jogador} não tem a carta {carta}")
        
jogo = JogoCartas()
jogo.embaralhar()

jogo.distribuir_cartas("Jogador1", 3)
jogo.distribuir_cartas("Jogador2", 3)

jogo.jogar("Jogador1", "2")
jogo.jogar("Jogador2", "5")