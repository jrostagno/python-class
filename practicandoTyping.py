# depende de la vesion de python 
from typing import List, Optional, Union

def process_items(items:list[str]):
    for item in items:
        print(item)
        
        
def process_items(items:List[str]):
    for item in items:
        print(item)



# SI TENGO QUE TIPAR TUPLAS Y SETS 

def process_items_tuplas(items_t:tuple[int,str],items_s:set[bytes]):
    
    print(items_s, items_t)
    return items_t, items_s

# SI tengo que tipar diccionarios , pongo el tipo para el key y para el value

def list_precios(precios:dict[str, float]):
    
    for item , price in precios.items():
        print(F"ITEM -> {item}- cuesta ${price}")
    
    
# si puede aceptar varios tipos de valores por ejemplo STR o INT , puedo usar un union o un |

def process_items_union(items:Union[int,str]):
    print(items)
    
    
def process_items_union1(items:int | str):
    print(items)
    
    
#Valores Opcionales  Optional o usando None  PARA HACERLO OPCIONAL TENES QUE USAR EL NONE SI O SI 


def process_items_optional(item:str|None=None):
    if(item):
       return "Hay un item"
    else:
       return "No hay"
 
def process_items_optional1(item:Optional[str]=None):
    if(item):
       return "Hay un item"
    else:
       return "No hay"
    
   

process_items_tuplas((1,'tupla'),{b"hola",b"mundo"})
    


# process_items(['test1','test2','535'])

#  list_precios({'blusa':22.3,'jean':120.2})


print(process_items_optional1('holla'))