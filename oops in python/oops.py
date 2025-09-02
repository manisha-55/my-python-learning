from abc import ABC, abstractmethod

# ---------------------------
# 1) Abstraction (Blueprint)
# ---------------------------
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# ---------------------------
# 2) Inheritance
# ---------------------------
class CreditCardPayment(Payment):
    def __init__(self, card_number, holder_name):
        self.__card_number = card_number   # Encapsulation (private attribute)
        self.holder_name = holder_name

    # Getter (Encapsulation)
    def get_card_number(self):
        return "**** **** **** " + self.__card_number[-4:]

    # Setter (Encapsulation)
    def set_card_number(self, new_number):
        if len(new_number) == 16:
            self.__card_number = new_number
        else:
            print("Invalid card number")

    # Implement abstract method
    def pay(self, amount):
        print(f"{self.holder_name} paid ₹{amount} using Credit Card {self.get_card_number()}")


# Another class inheriting Payment
class UpiPayment(Payment):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"Payment of ₹{amount} made via UPI ({self.upi_id})")


# ---------------------------
# 3) Polymorphism
# ---------------------------
def make_payment(payment_method, amount):
    payment_method.pay(amount)   # Same method name, different behaviors


# ---------------------------
# MAIN PROGRAM
# ---------------------------
if __name__ == "__main__":
    # Create objects
    credit = CreditCardPayment("1234567890123456", "Manisha")
    upi = UpiPayment("manisha@upi")

    # Encapsulation check
    print("Card Number (secured):", credit.get_card_number())
    credit.set_card_number("9876543210123456")

    # Polymorphism in action
    make_payment(credit, 5000)
    make_payment(upi, 1200)
