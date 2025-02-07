class Paciente ():
    def __init__(self,nome,idade,historicoConsultas):
        self.nome = nome
        self.idade = idade
        self.historicoConsultas = historicoConsultas
        self.consultaRealizadas = 0

    def marcarConsulta (self):
        consulta = input("Deseja marcar uma consulta(sim/não): ")
        if consulta == "sim":        
            self.consultaRealizadas += 1 
            return "ok!!! sua consulta foi marcada!!!"
        else:
            return f"volte sempre"
        
    def exibirConsultas (self):
        return f"{self.nome} seu historico de consulta é {self.consultaRealizadas + self.historicoConsultas}"
    
    def __str__(self):
        return f"olá {self.nome}, sua idade {self.idade} e seu hostórico de cnsulta anteriormente {self.historicoConsultas}"
 
    
pacienteRenan = Paciente("Renan" ,17,1)
print(pacienteRenan)

print(f"{pacienteRenan.marcarConsulta()}")
print(f"{pacienteRenan.exibirConsultas()}")
