# Polymorphism in Python
# "Many forms" → The same function/method/operator behaves differently depending on the context.
# In Python, polymorphism is supported in 3 ways:
# Method Overriding (Run-time Polymorphism)
# Operator Overloading
# Duck Typing

# 1) Method Overriding (Run-time Polymorphism)
# When a child class defines a method with the same name as the parent class, the child’s method overrides the parent’s method.

class Animal:
    def speak(self):
        return "Some Sound"
class Dog(Animal):
    def speak(self):
        return "Bark!"
class Cat(Animal):
    def speak(self):
        return "Mewow!"
animals = [Dog(), Cat(), Animal()]
for i in animals:
    print(i.speak())

# 2) Operator Overloading
# In Python, operators like +, -, *, etc. are just methods under the hood (called dunder methods like __add__, __sub__, etc.).
# We can override them to make operators work for our custom objects.
class Book:
    def __init__(self, pages):
        self.pages = pages
    def __add__(self, other):
        return self.pages+ other.pages
b1=Book(100)
b2=Book(210)
print(b1+b2)

# 3) Duck Typing
#Python is dynamically typed,so if an obj behaves like a duck(has methods/attributes needed),Python doesn’t care about its actual class.
class Bird:
    def fly(self):
        print("Bird flying...")
class Airplane:
    def fly(self):
        print("Airplane flying")
def lift_off(entity):
    entity.fly()

lift_off(Bird())
lift_off(Airplane())