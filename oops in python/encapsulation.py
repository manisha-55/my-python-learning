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