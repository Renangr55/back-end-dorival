class Personagens():
    def __init__(self,nomePersonagem:str, saude:int , forca:int, defesa:int, habilidadeEspecial:str):
       self.nomePersonagem = nomePersonagem
       self.saude = saude
       self.forca = forca
       self.defesa = defesa
       self.habilidadeEspecial = habilidadeEspecial
       
       
    def atacar(self,oponente):
        golpe = max(self.forca - oponente.defesa, 0)
        oponente.saude -= golpe
        print("a luta começou")
        
        
        if oponente.saude <= 0:
            print("oponente morreu")
            print("vc ganhou!!")
            
    def tomarPocao(self,saudeAtualizada):
        self.saude += 5
        print("aumentou sua saude")
        
        if self.saude >= 100:
            print("sua saude está 100%")
            
        
    
    def exibindoPersonagem(self):
        print(f"Nome: {self.nomePersonagem} | saude: {self.saude} | força: {self.forca} | defesa: {self.defesa} | habildade : {self.habilidadeEspecial}")
    
    
skorpion = Personagens(nomePersonagem="skorpion", saude=90, forca=169, defesa=89 , habilidadeEspecial="bola de fogo")
subzero = Personagens(nomePersonagem="sub-zero", saude=89, forca=90, defesa=75 , habilidadeEspecial="tempestade de gelo")



skorpion.exibindoPersonagem()
subzero.exibindoPersonagem()

skorpion.atacar(subzero)
subzero.tomarPocao(subzero)

skorpion.exibindoPersonagem()
subzero.exibindoPersonagem()