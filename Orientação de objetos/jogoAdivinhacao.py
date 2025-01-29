import random

class JogoAdivinhacao ():
    def __init__(self):
        self.numeroMisterioso = random.randint(1,10)
        
    def palpite (self):
        self.palpite = int(input("Digite um número de 1 a 10: "))
        
    def verificandoPalpite (self):
        if self.palpite == self.numeroMisterioso:
            print(f"o numero secret é {self.numeroMisterioso}")
            return "Você acertou o número"
        elif self.palpite > self.numeroMisterioso:
            print("você errou")
            return "seu palpite é maior que o número secreto"
        elif self.palpite < self.numeroMisterioso:
            print("você errou")
            return "seu palpite é menor do que o número secreto"
        else:
            return "error"
        
    def __str__(self):
        return f"o número secreto é {self.numeroMisterioso}"
        
usuario = JogoAdivinhacao()
print(usuario)

print(usuario.palpite())
print(usuario.verificandoPalpite())

        
    
        
        
        
        
        
    