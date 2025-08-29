# Class: a blueprint for objects (data + behavior).
# Object (instance): a concrete thing created from a class.
# 1) Classes, objects, self, __init__
# self is the instance being operated on. __init__ initializes instance state.

# Key points
# __init__ is not a constructor; the object is created by __new__ and then initialized by __init__.
# Attributes can be added in __init__ or later (u.role = "dev"), but prefer defining in __init__.

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def contact(self):
        return f"Email sent to {self.email}"

u1 = User("Manisha", 'abc@gmail.com')
print(u1.name)
print(u1.email)
print(u1.contact())

