#CLASES


class Person:
    especie= 'Humano'
    __pin_bancario=''
    def __init__ (self,name,age):
        self.name= name
        self.age= age
    
    def saludo(self):
        return F'Hola Soy {self.name} !' 
    
    def guardar_pin(cls,pin):
        cls.__pin_bancario= pin
        return 'Pin Guardado con exito!'
    
    def get_pinBancario(cls):
        return cls.__pin_bancario
    
    
        

class Empleado(Person):
    def __init__(self, name, age,puesto,company):
        super().__init__(name, age)
        self.puesto= puesto
        self.company= company
        
    
    

        
    
    
        
        
    
    

persona1= Person('Juan',23)

#print(persona1.name)

#print(persona1.saludo())

persona1.guardar_pin('Abc123')

#print(persona1.get_pinBancario())


persona2= Empleado('Tito',22, 'dev','tenerello')

print(persona2.name)
print(persona2.age)
print(persona2.puesto)

persona2.guardar_pin('MiPIN2')

pin=persona2.get_pinBancario()

print(pin)



class BankAccount:
    
    interest_rate=0.04
    
    def __init__(self, holder,balance):
        self.holder=holder
        self.balance=balance
    
    @classmethod
    def change_interest_rate(cls,new_rate):
        cls.interest_rate=new_rate
        
    @staticmethod
    def validate_amount(amount):
        return amount>0
    
    def withdraw (self, amount):
        if(self.validate_amount(amount)):
            if( self.balance>=amount):
             self.balance -= amount
            else:
                print('No se puede retirar ese Monto es superior al Saldo')
            
        else:
            print('Ingrese un monto valido mayor a 0')
            
    

javier_account=BankAccount('javier',1000)

print(javier_account.holder)

print(javier_account.balance)

javier_account.withdraw(250)

print(javier_account.balance)

print(javier_account.withdraw(850))
        
    
