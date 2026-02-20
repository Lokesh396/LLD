class BankAccount:
    def __init__(self, owner_name: str, account_number: str, balance: float):
        # TODO: initialize self._owner_name, self._account_number, and self._balance
        self._owner_name = owner_name
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount: float) -> bool:
        # TODO: add amount to balance if amount > 0, return True if successful
        return False

    def withdraw(self, amount: float) -> bool:
        # TODO: subtract amount from balance if balance >= amount, return True
        return False

    def display_account(self):
        # TODO: print "owner_name (account_number) | Balance: $balance"
        # Hint: use f"${self._balance:.2f}" for formatting
        print(f"{self._owner_name} ({self._account_number}) | Balance: ${self._balance:.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, owner_name: str, account_number: str,
                 balance: float, interest_rate: float):
        super().__init__(owner_name, account_number, balance)
        # TODO: initialize self._interest_rate
        self._interest_rate = interest_rate

    def withdraw(self, amount: float) -> bool:
        # TODO: only allow if (balance - amount) >= 100
        if(self._balance - amount) >= 100:
            self._balance -= amount
            return True
        return False

    def apply_interest(self):
        # TODO: add (balance * interest_rate / 100) to balance
        self._balance += ((self._balance * self._interest_rate) / 100)


class CheckingAccount(BankAccount):
    def __init__(self, owner_name: str, account_number: str,
                 balance: float, overdraft_limit: float):
        super().__init__(owner_name, account_number, balance)
        # TODO: initialize self._overdraft_limit
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> bool:
        # TODO: allow if (balance + overdraft_limit) >= amount
        if(self._balance + self._overdraft_limit) >= amount:
            self._balance -= amount
            return True
        return False


import math


class Shape:
    def __init__(self, name: str):
        self._name = name

    def area(self) -> float:
        # TODO: return 0 by default
        return 0

    def perimeter(self) -> float:
        # TODO: return 0 by default
        return 0

    def describe(self):
        # TODO: print "Shape: name, Area: area, Perimeter: perimeter"
        # Hint: use f"{value:.2f}" for formatting
        print(f"Shape: {self._name}, Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}")


class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__("Circle")
        self._radius = radius
        # TODO: initialize self._radius

    def area(self) -> float:
        # TODO: return math.pi * radius * radius
        return round(math.pi * (self._radius ** 2), 2)

    def perimeter(self) -> float:
        # TODO: return 2 * math.pi * radius
        return round(2 * math.pi * self._radius, 2)

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__("Rectangle")
        self._width = width
        self._height = height
        # TODO: initialize self._width and self._height

    def area(self) -> float:
        # TODO: return width * height
        return round(self._width * self._height, 2)

    def perimeter(self) -> float:
        # TODO: return 2 * (width + height)
        return round(2 * (self._width + self._height), 2)




if __name__ == "__main__":
    savings = SavingsAccount("Alice", "SAV-001", 1000, 2.0)
    savings.display_account()
    print(f"Withdraw $950: {str(savings.withdraw(950)).lower()}")
    savings.apply_interest()
    savings.display_account()

    print()

    checking = CheckingAccount("Bob", "CHK-002", 500, 300)
    checking.display_account()
    print(f"Withdraw $700: {str(checking.withdraw(700)).lower()}")
    checking.display_account()

    circle = Circle(5.0)
    circle.describe()

    rect = Rectangle(4.0, 6.0)
    rect.describe()