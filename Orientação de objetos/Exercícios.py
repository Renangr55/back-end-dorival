# exercicio 1 

class Circulo ():
    def __init__(self,x,y,raio):
        self.x = x
        self.y = y
        self.raio = raio
       
      


    def area (self):
        pi = 3.14
        return pi * (self.raio ** 2)

    def diametro(self):
        return self.raio * self.raio
    
    def circuferencia (self):
        pi = 3.14
        return 2 * pi * self.raio
    
    def mover (self,x,y):
        self.x = x
        self.y = y
       

    def __str__(self):
        return f' circulo: centro = {self.x}, {self.y}, raio = {self.raio}'


test = Circulo(10,20,50)              
print(test)
print(f'Área: {test.area()}')
print(f'Diâmetro: {test.diametro()}')
print(f'Circunferência: {test.circuferencia()}')
        