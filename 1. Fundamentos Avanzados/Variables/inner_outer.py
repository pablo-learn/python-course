x = 'global' #Variable global

#Función externa
def outer_function():
    x = 'enclosing'
    #Función interna
    def inner_function():
        x = 'local' #Variable local
        print(x)
    
    inner_function()
    print(x)

outer_function()
print(x)