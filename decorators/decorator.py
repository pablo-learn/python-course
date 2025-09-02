def my_decorator(func):
    # el core del decorador siempre se ejecuta al invocar @my_decorator
    def wrapper(name):
        print('decorator')
        func(name)
    return wrapper
  

@my_decorator
def say_hello(name):
    print(f'hello {name}')


say_hello('John')