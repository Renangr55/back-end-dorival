import calendar
from datetime import datetime


class Calendario ():
    def __init__(self,ano,mes):
        self.mes = mes
        self.ano = ano
        self.feriados = {
            "01/01": "Ano Novo",
            "06/01": "Dia de Reis",
            "20/01": "São Sebastião",
            "25/01": "Aniversário de São Paulo",
            "21/04": "Tiradentes",
            "01/05": "Dia do Trabalhador",
            "07/09": "Independência do Brasil",
            "12/10": "Nossa Senhora Aparecida",
            "02/11": "Finados",
            "15/11": "Proclamação da República",
            "25/12": "Natal"
        }    
      
      
    def exibindoCalendario (self):
        return (calendar.month(self.ano,self.mes))
    
    
    
    def verificandoFeriados (self,dia):
        data_formatada = f"{dia:02d} / {self.mes:02d}"
        if data_formatada in self.feriados:
            return f"{data_formatada} é feriado: {self.feriados[data_formatada]}"
        return f"{data_formatada} não é feriado"
    
    def verificandoDiferenca (self,primeiroDia,segundoMes,segundoDia):
        primeira_data = datetime(self.ano,self.mes,primeiroDia)
        segunda_data = datetime(self.ano,segundoMes,segundoDia)
        diferencaDias = abs((primeira_data - segunda_data).days) 
        return f"a diferença da primeira data {primeira_data} para segunda data é {segunda_data} e a diferença das datas é {diferencaDias}"
        
    
   
        
janeiro = Calendario(2025,1)
print(janeiro)

print(janeiro.exibindoCalendario())
print(janeiro.verificandoDiferenca(10,2,10))
