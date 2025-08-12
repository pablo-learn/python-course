# en general los decoradores al usarlos como @my_decorator ya se auto ejecutan,
""" 
cuando invocamos con valores como @decorator('pre saludo')
se ejecuta el decorador con el valor pre_saludo, por esto necesitamso retornar un decorador
para luego ser usado por defecto como si usaramos @decorator, este también se auto ejecutará.
 """
def my_decorator(pre_saludo):
    # se corre porque @my_decorator('pre saludo')
    print(pre_saludo)
    def decorator(func):
        # se corre porque al ejecutar @my_decorator('pre saludo') retornamos un decorador que sera auto ejecutado como decorador, es decir brindamos la funcion para que @my_decorator la ejecute
        def wrapper(saludo):
            # core del decorador
            func(saludo)
        return wrapper
    return decorator

@my_decorator('pre saludo')
def say_hello(saludo):
    print(saludo)

say_hello('hello')