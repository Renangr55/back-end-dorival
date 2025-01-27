import random

class jogoCartas ():
    def __init__(self):
        self.cartas = [1,2,3,4,5,6,7,8]
        self.primeiroJogador = []
        self.segundoJogador = []
        self.terceiroJogador = []
        self.quartoJogador = []
        self.cartasJogadas = []

    def embaralharCartas(self):
        random.shuffle(self.cartas)
        print('Cartas embaralhadas')
        return self.cartas

    def distribundoCartas(self):
        cartasDivididas = len(self.cartas) // 4

        self.primeiroJogador = self.cartas[:cartasDivididas]
        print(f"Primeiro Jogador: {self.primeiroJogador}")

        self.segundoJogador = self.cartas[cartasDivididas:cartasDivididas*2]
        print(f"segundo Jogador: {self.segundoJogador}")

        self.terceiroJogador = self.cartas[cartasDivididas*2:cartasDivididas*3]
        print(f"terceiroJogador: {self.terceiroJogador}")

        self.quartoJogador = self.cartas[cartasDivididas*3:]
        print(f"quarto Jogador: {self.quartoJogador}")


    def jogandoCartas(self):
        print('Jogo começou!!!!')

        while True:

            #jogador1
            PrimeiroJogadorCarta = int(input("jogado1 , escolha uma carta para jogar"))
            
            if PrimeiroJogadorCarta in self.primeiroJogador:
                self.primeiroJogador.remove(PrimeiroJogadorCarta)
                print(f"Jogador1 jogou uma carta {PrimeiroJogadorCarta}")
            else:
                print("Jogador 1,Você não tem essa carta")

            if len(self.primeiroJogador) == 0:
                print("As Cartas do jogador1 acabaram")
                break

            #Jogador2
            segundoJogadorCarta = int(input("jogado2 , escolha uma carta para jogar: "))
        
            if segundoJogadorCarta in self.segundoJogador:
                self.segundoJogador.remove(segundoJogadorCarta)
                print(f"Jogador2 jogou uma carta {segundoJogadorCarta}")
            else:
                print("Jogador 2,Você não tem essa carta")

            if len(self.segundoJogador) == 0:
                print("As Cartas do jogador2 acabaram")
                break

            #jogador3
            terceiroJogadorCarta = int(input("jogado3 , escolha uma carta para jogar"))
            
            if terceiroJogadorCarta in self.terceiroJogador:
                self.terceiroJogador.remove(terceiroJogadorCarta)
                print(f"Jogador3 jogou uma carta {terceiroJogadorCarta}")
            else:
                print("Jogador 3,Você não tem essa carta")

            if len(self.terceiroJogador) == 0:
                print("As Cartas do jogador3 acabaram")
                break

            #jogador4
            quartoJogadorCarta = int(input("jogado4 , escolha uma carta para jogar"))
            
            if quartoJogadorCarta in self.quartoJogador:
                self.quartoJogador.remove(quartoJogadorCarta)
                print(f"Jogador4 jogou uma carta {quartoJogadorCarta}")
            else:
                print("Jogador 4,Você não tem essa carta")


            if len(self.quartoJogador) == 0:
                print("As Cartas do jogador4 acabaram")
                break
            
             

    

test = jogoCartas()
print(test)

print(test.embaralharCartas())
print(test.distribundoCartas())
test.jogandoCartas()