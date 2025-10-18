

class Persona:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def saludar(self):
        return F"Hola soy {self.name} y tengo {self.age}"



class Ingeniero(Persona):
    
    def __init__(self, name, age, matricula):
        super().__init__(name, age)
        self.__matricula= matricula
        
    def getMatricula(self):
        return self.__matricula
    
    def saludar(self):
        return F"Hola soy INGGGG {self.name} y tengo {self.age}"
    
    def saludarProfesionalmente(self):
        return F"hola soy el ingeniero  {self.name} y tengo {self.age} !!"
    
    
class Youtuber (Persona):
    def __init__(self, name:str, age:int,canal:str,seguidores:int | None=None):
        super().__init__(name, age)
        self.canal=canal
        self.seguidores=seguidores
        
    
        def saludar(self):
         return F"Hola soy INGGGG {self.name} y tengo {self.age}"
    
    
    

youtuber1= Youtuber('dani',11,'olga',600)


    

print(youtuber1.age)
print(youtuber1.canal)
print(youtuber1.seguidores)

print(help(Youtuber.__init__))


    
    
ingeniero2= Ingeniero('Juan',23,'233FFFtt')

print(ingeniero2.getMatricula())
# print(ingeniero2.getMatricula())
# print(ingeniero2.saludarProfesionalmente())
# print(ingeniero2.saludar())
        