class Animal:
    def __init__(self, type, name):
        self.type = type
        self.name = name


    def __str__(self):
        return f"Animal: {self.type}, Name: {self.name}"

    def get_self(self):
        return self


animal = Animal("mamifero", "perro")
