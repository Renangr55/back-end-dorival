class Animal():
    def __init__(self,nomeAnimal:str, especieAnimal:str):
        self.nomeAnimal = nomeAnimal
        self.especieAnimal = especieAnimal
        
    def __str__(self):
        return f"animal criado: {self.nomeAnimal} | especie: {self.especieAnimal}"
    
class Habitat(Animal):
    def __init__(self, nomeAnimal, especieAnimal,habitatAnimal):
        super().__init__(nomeAnimal, especieAnimal)
        self.habitatAnimal = habitatAnimal
        
    def localização(self):
        print(f"o {self.nomeAnimal} está localizado {self.habitatAnimal}")
        
    def mover(self): 
        print(f"O {self.nomeAnimal} está se movendo {self.habitatAnimal}")

class Alimentação(Animal):
    def __init__(self, nomeAnimal, especieAnimal, alimentacao):
        super().__init__(nomeAnimal, especieAnimal)
        self.alimentacao = alimentacao
        
        
    def comer(self):
        print(f"{self.nomeAnimal} está comendo { self.alimentacao}")
        
    def __str__(self):
        return f"a comida do {self.nomeAnimal} é {self.alimentacao}"
        
class Veterinario (Animal):
    def __init__(self, nomeAnimal, especieAnimal, nomeVeterinario):
        super().__init__(nomeAnimal, especieAnimal)
        self.nomeVeterinario = nomeVeterinario
        
    def cuidar(self):
        print(f"O {self.nomeVeterinario} está cuidando do {self.nomeAnimal}")
        print(f"O {self.nomeAnimal} está 100%")
    def __str__(self):
        return f"o nome do veterinário é {self.nomeVeterinario}"
    
class Funcionario (Animal):
    def __init__(self, nomeAnimal, especieAnimal, nomeFuncionario):
        super().__init__(nomeAnimal, especieAnimal)
        self.nomeFuncionario = nomeFuncionario
        
    def __str__(self):
        return f"o nome do funcionário que esta responsável pelo {self.nomeAnimal} é  {self.nomeFuncionario}"
    
    
    
cachorro = Animal("maik" , "vira-lata")
print(cachorro)

cachorro = Habitat("maik" , "vira-lata", "casa")
cachorro.localização( )
cachorro.mover()

cachorro = Alimentação("maik" , "vira-lata", "ração")
print(cachorro)
cachorro.comer()

cachorro = Veterinario("maik" , "vira-lata", "Alex shuma")
print(cachorro)
cachorro.cuidar()

cachorro = Funcionario("maik" , "vira-lata", "Rosimeire")
print(cachorro)

        
        
        
        
