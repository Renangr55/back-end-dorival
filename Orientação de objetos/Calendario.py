import calendar
from datetime import datetime
import holidays

class Calendario ():
    
    def __init__(self,ano,mes):
        self.ano = ano
        self.mes = mes
        self.feriados = holidays.Brazil(years=2025)
       
        
    def ExibindoData (self):
        self.ultimo_dia = calendar.monthrange(self.ano, self.mes)[1]
        
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
                self.diasNormais.append(f"{dia} - diasFeriados {self.diasFeriados} {self.data}")
                return self.diasNormais
            
            else:
                self.diasFeriados.append(f"{dia} tem feriado")
                return self.diasFeriados
            
    def __str__(self):
        return f'dias com diasFeriados: {self.feriados} \n dias normais: {self.diasNormais}  '
        
        
teste = Calendario(2025, 3)
print(teste.ExibindoData())
print(teste.verificandoCalendario())
        