
# super class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age



    def speak():
        return "I am an Animal"

# sub class
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed