# 5) Inheritance in Python
# Inheritance allows a class (child/subclass) to use properties and methods of another class (parent/superclass).
# It helps in code reuse, hierarchy creation, and extension of functionality.
# Basic Example – Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Some Sound"

class Dog(Animal):
    def speak(self):
        return "woof!!"

class Cat(Animal):
    def speak(self):
        return "Meow!!!"

dog =Dog("Tommy")
cat = Cat("Kitty")
print(dog.name, "says", dog.speak())
print(cat.name, "says", cat.speak())