class Aluno ():
    def __init__(self, nome,matricula,notas):
        self.nome = nome
        self.notas = notas
        self.matricula = matricula
    
    def calcularMedia (self):
        soma = 0
        for number in self.notas:
            soma += number
                
        return soma / len(self.notas)
    
    def verificarAluno (self):
        soma = 0
        for number in self.notas:
            soma += number
            
        
        media = soma / len(self.notas)
        if media >= 5:
            return "o aluno foi Aprovado"
        else: 
            return "O aluno foi Reprovado"
        
        
    
    def __str__(self):
        return f"O nome do aluno é {self.nome} e as notas dele são {self.notas}"


alunoRenan = Aluno ("Renan Gabriel" , 1928374655, notas=[9,5,7])
print(alunoRenan)
 

print(f"{alunoRenan.calcularMedia()}")
print(f"{alunoRenan.verificarAluno()}")