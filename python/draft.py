class Dog:
    species = "animal" #Class attribute

    def __init__(self, name): #instance attribute
        self.name = name

    def __str__(self):
        return "name "  + self.name

dog1 = Dog("a")
print(dog1.name)

dog2 = Dog("a")
print(dog2.name)

