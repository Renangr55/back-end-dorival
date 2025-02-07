class Carro ():
    def __init__(self, marca,modelo,velocidadeAtual):
        self.marca= marca
        self.modelo = modelo
        self.velocidadeAtual = 0
        
    def Acelerar(self,acelerar):
        self.velocidadeAtual += acelerar
        return f'velocidade atual do {self.modelo}: {self.velocidadeAtual}KM, Acelerandoooo {self.modelo} para {acelerar}KM'
        
    def Freiar (self,freio):
        self.velocidadeAtual -= freio
        return f"velocidade atual do {self.modelo} {self.velocidadeAtual}KM, freiandoooooo {self.modelo} para {freio}KM"
        
    def exibirVelocidadeAtual(self):
        return f'velocidade atual {self.velocidadeAtual}'
    
    def __str__(self):
        return f'marca do carro: ({self.marca}), modelo do carro: ({self.modelo}), velocidade atual ({self.velocidadeAtual})'
        


carroRenan = Carro("Ford","Mustang GT",30)
print(carroRenan)

print(carroRenan.Acelerar(acelerar=int(input("Digite a velocidade que você deseja acelerar: "))))

print(carroRenan.Freiar(freio=int(input("Digite a velocidade que você deseja freiar: "))))

print(f"velocidade atual do carro: {carroRenan.exibirVelocidadeAtual()}KM")