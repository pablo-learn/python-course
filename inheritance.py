class Mamifero:
    def __init__(self):
        pass
    
    def features(self):
        print('Tiene pelaje y glandulas mamarias')

class Perro(Mamifero):
    def __init__(self):
        pass
    
    def bark(self):
        print('Woof!!')
    
    def walking(self):
        print('Paseando alegre')
        
    def eat(self):
        print('Comiendo contento')

class Cachorro(Perro):
    def __init__(self):
        pass
    
    def play(self):
        print('Jugando y mordiendo zapatos')
        
cachorro1 = Cachorro()
cachorro1.bark()
cachorro1.play()
cachorro1.features()