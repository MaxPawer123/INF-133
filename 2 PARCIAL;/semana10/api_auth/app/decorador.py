from functools import wraps
def my_decorador(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("Antes de llamr a la funcionc")
        result=func(*args,**kwargs) #ags es una lista , kwargs es una diccionario
        print("Despues de llamar a la funcion")
        return result
    return wrapper

@my_decorador
def greet(name):
    """Funcion para saludar a alguien"""
    
    return (f"Hola,{name}!")

#Llama a la funcion
greet("juan")
print(greet.__name__)
print(greet.__doc__)

#Convetir en app