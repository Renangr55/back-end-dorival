import calendar
from datetime import datetime


class Calendario ():
    
    def __init__(self,ano,mes):
        self.ano = ano
        self.mes = mes
        self.feriados = {
            (2025, 1, 1): "Ano Novo",
            (2025, 12, 25): "Natal",
            (2025, 9, 7): "Independência do Brasil",
            (2025, 11, 15): "Proclamação da República"
        }
       
        
    def ExibindoData (self):
        self.ultimo_dia = calendar.monthrange(self.ano, self.mes)[1] #descobrindo quantos dias tem no mês
        
        self.dias = []
        
        for dia in range(1, self.ultimo_dia + 1):
            self.data = datetime(self.ano, self.mes,  dia)
            self.dias.append(self.data.strftime("%d/%m/%Y"))
            
        return self.dias

    def verificandoCalendario(self):
        self.diasFeriados = []
        self.diasNormais = []
        
        for dia in self.dias:
            dataFormatada = datetime.strptime(dia, "%d/%m/%Y")
            
            if dataFormatada in self.feriados:
                self.diasFeriados.append(f"{dia} - diasFeriados {self.diasFeriados} {self.data}")
                return "esses dias são"
        return {
            "feriados" : self.diasFeriados,
            
        }

        
        
        
        
    def __str__(self):
        return f'dias com diasFeriados: {self.feriados} \n dias normais: {self.diasNormais}  '
        
        
teste = Calendario(2025, 1)
print(teste.ExibindoData())
print(teste.verificandoCalendario())

        