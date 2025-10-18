from pydantic import BaseModel, StrictInt, StrictStr

class PersonaData(BaseModel):
    name:StrictStr
    age:StrictInt


class Persona:
    def __init__(self,data:PersonaData):
        self.name= data.name
        self.age=data.age
    
    def greetings(self):
        return F"Hola soy {self.name} y tengo {self.age}"
    
    


data= PersonaData(name='pepe',age=33)

persona1= Persona(data)

print(persona1.name)
print(persona1.age)