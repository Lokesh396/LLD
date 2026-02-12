
class BankAccount:
    """
    Encapsulation is one of the four foundational principles of object-oriented design. It is the practice of grouping data (variables) and behavior (methods) that operate on that data into a single unit (typically a class) and restricting direct access to the internal details of that class.

    Encapsulation focuses on how to protect and control access to data within a class. But what if we extend that idea. Not just hiding data, but also hiding complexity itself?

    That's where Abstraction comes in.

    """

    def __init__(self) -> None:
        self.__amount = 0

    
    def _getmoney(self) -> float:
        return f"Balance: {self.__amount}"
    
    def _deposit(self, money:float) -> None:
        if money <= 0:
            raise ValueError('money should be positive')
        self.__amount += money
        print("Money deposit successfull:", money)

    def _withDraw(self, money:float) -> None:
        if money <=0 :
            raise ValueError("Money should be positive")
        elif money > self.__amount:
            raise ValueError('Insufficient Balance')
        else:
            self.__amount -= money
            print(f'Money withdraw successfull:',money)

account = BankAccount()
account._deposit(1000)

print(account._getmoney())
account._withDraw(120)
print(account._getmoney())