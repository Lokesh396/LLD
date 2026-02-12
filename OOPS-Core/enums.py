from enum import Enum

class OrderStatus(Enum):
    """
    They allow you to define a fixed set of named constants
      that improve clarity, type safety, and maintainability in your system.
    It helps us avoid using magic values or numbers and self documenting.
    """
    CREATED = 'CREATED'
    SHIPPED = 'SHIPPED'
    DELIVERED = 'DELIVERED'

status = OrderStatus.CREATED
print(OrderStatus.CREATED == status)
print(OrderStatus.SHIPPED.value, OrderStatus.SHIPPED.name)

class Coin(Enum):
    PENNY = 1
    NICKEL = 5
    DIME = 10
    QUARTER = 25
    
    
    def get_value(self):
        return self.value
    
total = Coin.DIME.get_value() + Coin.QUARTER.get_value()  # 35
print(total)