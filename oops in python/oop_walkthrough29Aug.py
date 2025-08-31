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

# 3) Instance vs Class attributes;
# Instance attribute → belongs to a specific object (created using self. inside __init__). Each object has its own copy.
# Class attribute → shared across all objects of the class (defined directly in the class body, outside __init__).

class Job:
    counter = 0  # class attribute
    def __init__(self, title):
        self.title = title
        Job.counter += 1

    @classmethod
    def from_dict(cls, d):
        return cls(d["title"])

    @staticmethod
    def is_valid_title(title):
        return isinstance(title, str) and len(title) > 0

j = Job("Python Dev")
k = Job.from_dict({"title": "Data Engineer"})
print(Job.counter)
print(Job.is_valid_title("SRE"))

# 4) @classmethod
# Bound to the class itself, not the object.
# First argument → cls (represents the class).
# Can modify class attributes but not instance attributes directly.
# Used when you want to create alternative constructors or work with class-level data.
# @classmethod: first arg is the class (cls); great for alternative constructors or class-wide state.
# @classmethod lets you update class-level data (like company) for all objects.

class Employee:
    company = "ABC Crop"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

emp1 = Employee("Manisha", 50000)
emp2 = Employee("Raj", 80000)
#print(emp1.name, emp1.salary)
print(emp1.company)
print(emp2.company)
Employee.change_company("XYZ Pvt Ltd")
print(emp1.company)
print(emp2.company)

# 5) @staticmethod
# @staticmethod: utility function living inside the class namespace.
# Doesn’t take self (instance) or cls (class).
# Just a normal function inside a class.
# Used when logic is related to the class but does not need access to class/instance data.
class Mathutil:
    @staticmethod
    def __add__(self, other):
        return self+other
    @staticmethod
    def is_even(num):
        return num%2==0
print(Mathutil.__add__(5,6))
print(Mathutil.is_even(5))

# 4) Encapsulation: conventions, name-mangling, and @property
# Python uses conventions:
# public_attr → public
# _protected_attr → internal (don’t use outside)
# __private_attr → name-mangled to _Class__private_attr (discourages accidental access)
# Use properties to add validation while keeping attribute-style access.

class BankAcc:
    def __init__(self, balance=0):
        self._balance=0
        self.balance = balance
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, amount):
        if amount<0:
            raise ValueError("Balance cannot be -ve")
        self._balance=amount
acc = BankAcc(500)
acc.balance+=300
print(acc.balance)

# Using Getter & Setter Methods
# We usually control access with getter (to read value) and setter (to update value with validation).

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance= balance
    def get_balance(self):
        return self.__balance
    def set_balance(self, amount):
        if(amount<0):
            print("amount cannot be -ve")
        else:
            self.__balance = amount
b1 = BankAccount("Shrinidhi", 6000)
print(b1.get_balance())
b1.set_balance(7000)
print(b1.get_balance())

# 4. Using @property (Pythonic way of Encapsulation)
# Instead of writing separate get_ and set_ methods, Python gives us the @property decorator.
class BankAccountss:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, amount):
        if amount<0:
            print("balance cannot be -ve")
        else:
            self.__balance = amount

b= BankAccountss("nidhish", 1000)
print(b.balance)
b.balance = -2000
b.balance = 2200
print(b.balance)

