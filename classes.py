# Classes

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def bark(self):
        print("Woof!")

Dog1 = Dog("Rodger", 9)
print(Dog1.name)
print(Dog1.age)
Dog1.bark()
