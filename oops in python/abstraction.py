# 1. What is Abstraction?
# Definition: Abstraction is the process of hiding the implementation details and showing only the essential features.
# It focuses on what an object does, not how it does it.
# 👉 Example in real life: When you drive a car, you use the steering wheel, accelerator, brake.
# You don’t need to know how the engine works internally.
# The car maker hides complexity and only exposes necessary features. # That’s abstraction.
# 2. How Python Supports Abstraction?
# Python doesn’t have true abstraction like Java or C++, but it uses Abstract Base Classes (ABC).
# Abstract Base Classes let you create blueprints where child classes must implement certain methods.
# 👉 We use the abc module: # from abc import ABC, abstractmethod


# 3. Abstract Class Rules
# Abstract class = class that cannot be instantiated (can’t create objects directly).
# Must inherit from ABC (class MyClass(ABC):).
# Can have abstract methods (must be implemented in child) and normal methods.
# Any class that inherits must provide implementation for all abstract methods, otherwise Python throws an error.

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def max_speed(self):
        pass
    @abstractmethod
    def fuel_type(self):
        pass
class Car(Vehicle):
    def max_speed(self):
        return 200
    def fuel_type(self):
        return "Petrol"
class Bike(Vehicle):
    def max_speed(self):
        return 120
    def fuel_type(self):
        return "Diesel"

c=Car()
print(c.max_speed())
print(c.fuel_type())

b= Bike()
print(b.max_speed())
print(b.fuel_type())