# 5) Inheritance in Python
# Inheritance allows a class (child/subclass) to use properties and methods of another class (parent/superclass).
# It helps in code reuse, hierarchy creation, and extension of functionality.
# Basic Example – Single Inheritance

#1.Single Inheritance → One parent, one child.
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

#2. Multiple Inheritance → Child inherits from multiple parents.
#3. Multilevel Inheritance → A → B → C (chain).
#4. Hierarchical Inheritance → One parent, multiple children.
#5.Hybrid Inheritance → Combination of above.
# (Python resolves conflicts using MRO → Method Resolution Order)
# 🔹 super() keyword
# Used to call parent class constructor/methods in child class.

class Person:
    def __init__(self, name):
        self.name = name
class Employee(Person):
    def __init__(self, name , id):
        super().__init__(name)
        self.id = id
emp1 =Employee("Nidhish", 'E101')
print(emp1.name, emp1.id)