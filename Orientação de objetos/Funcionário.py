class Funcionario ():
    def __init__(self,nome,salario,cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        
    def SalárioLiquido (self):
        descontos = self.salario * 0.09
        beneficios = (descontos * 0.75) - 142.80
        return self.salario - (descontos + beneficios)
    
    def __str__(self):
        return f"nome: {self.nome},salário bruto : {self.salario}, Cargo: {self.cargo}"
    
FuncionarioRenan = Funcionario("Renan", 3000 , "Gerente")
print(FuncionarioRenan)
print(f"seu salário liquido é : {FuncionarioRenan.SalárioLiquido(): .2f}")
        
        


