class Retangulo ():
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def area (self):
        return self.largura * self.altura 
    
    def perimetro (self):
        return 2 * (self.largura + self.altura)
    
    def diagonal (self):
        return (self.largura ** 2 + self.altura ** 2) ** (1/2)  # teorema de pitagoras
    
    def __str__(self):
        return f"a largura do triangulo é {self.largura} e a alutura é {self.altura}"
        

trianguloUsuario = Retangulo (10, 5)
print(trianguloUsuario)

print(f"Área do triangulo: {trianguloUsuario.area()}")
print(f"Perimetro do triangulo: {trianguloUsuario.perimetro()}")
print(f"Diagonal do triangulo: {trianguloUsuario.diagonal(): .2f}")
