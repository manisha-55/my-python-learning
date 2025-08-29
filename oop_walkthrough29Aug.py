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

# 2) __repr__ vs __str__
# __repr__: unambiguous, for developers (debugging).
# __str__: readable, for users.
class Ticket:
    def __init__(self, id, status):
        self.id= id
        self.status= status
    def __str__(self):
        return f"Ticket(id={self.id!r}, status={self.status!r})"
    def __repr__(self):
        return f"[#{self.id}]{self.status}"

t1 = Ticket(11, "Open")
print(t1.id, t1.status)
print(repr(t1)) #dev view
print(str(t1))  #user view

