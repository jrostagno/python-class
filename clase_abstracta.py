from abc import ABC,abstractmethod


class Persona(ABC):
    def __init__(self, name:str, age:int) -> None:
        self.name=name
        self.age=age
    
    @abstractmethod
    def saludar(self):
        return F"Saludar es mandatorio {self.name}"
    
    def saludar_pro(self):
        return F"Saludar como PRO no es mandarorio {self.name}"
    
    
    
class Medico(Persona):
    
    operaciones=None
    def __init__(self, name: str, age: int, especialidad:str, hospital:str|None=None) -> None:
        super().__init__(name, age)
        self.especialidad=especialidad
        self.hospital=hospital
        
    def saludar(self):
        return F"Hola soy {self.name}"
    
    def addOperations(self,opNumber:int):
        self.operaciones=opNumber
        return "Operaciones agregadas !"
        
        
        


medico1= Medico('Guillermo',60,"Cirujano Plastico")

print(medico1.addOperations(22))

print(medico1.operaciones)
        
        
         
    
        

