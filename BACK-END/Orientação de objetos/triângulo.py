class Triangulo ():
    def __init__(self,primeiroLado,segundoLado,TerceiroLado):
        self.primeiroLado = primeiroLado
        self.segundoLado = segundoLado 
        self.terceiroLado = TerceiroLado
        
    def VerificacaoTriangulo (self):
        
        if(self.primeiroLado + self.segundoLado > self.terceiroLado and self.primeiroLado + self.terceiroLado > self.segundoLado and self.terceiroLado + self.segundoLado > self.primeiroLado):
            return "triangulo Válido"
        else:
            return "triangulotriangulo Inválido"
    def semiperimeto(self):
        semiperimetro = self.semiperimeto = (self.primeiroLado + self.segundoLado + self.terceiroLado) / 2
        return semiperimetro
    
    def CalcularArea(self):
        area = pow(self.semiperimeto * (self.semiperimeto - self.primeiroLado) * (self.semiperimeto - self.segundoLado) * (self.semiperimeto - self.terceiroLado), 0.5) #pow serve para calcular raiz quadrada
        return area
    
    def __str__(self):
        return f'primeiro lado: {self.primeiroLado} segundo lado : {self.segundoLado} , terceiroLado: {self.terceiroLado} '
        



trianguloUsuario = Triangulo(primeiroLado=5, segundoLado=6, TerceiroLado=7)
print(f"{trianguloUsuario} | status do triangulo: {trianguloUsuario.VerificacaoTriangulo()} | semiperímeto do triangulo: {trianguloUsuario.semiperimeto()} |  area do triangulo: {trianguloUsuario.CalcularArea(): .1f} ")
