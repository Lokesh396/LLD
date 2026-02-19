class TemperatureSensor:
    def __init__(self):
        self._readings: list[float] = []

    def add_reading(self, value: float) -> None:
        if -50 <= value <= 150:
            self._readings.append(value)

    def get_average(self) -> float:
        if not self._readings:
            return 0.0
        return round(sum(self._readings) / len(self._readings), 2)

    def get_reading_count(self) -> int:
        return len(self._readings)

    def get_readings(self) -> list[float]:
        return self._readings[::]
    
    def is_same(self, copList:list) -> bool:
        return copList is self._readings
    
class ShoppingCart:
    def __init__(self):
        self._items: dict[str, float] = {}
        self._discount_applied = False
        self._is_checked_out = False

    def add_item(self, name: str, price: float) -> None:
        # Add item to cart, but reject if already checked out
        if not self._is_checked_out:
            self._items[name] = price
            return
        print('Cannot modify a checked-out cart')

    def apply_discount(self, code: str) -> bool:
        # If code is "SAVE10" and no discount applied yet and not checked out,
        # mark discount as applied and return True. Otherwise return False.
        if not self._discount_applied and not self._is_checked_out and code == 'SAVE10':
            self._discount_applied = True
            return True
        return False

    def get_total(self) -> float:
        # Sum all item prices. If discount was applied, subtract 10%.
        total = 0
        for item in self._items:
            total += self._items[item]
        precent10 = total * 0.1
        if self._discount_applied:
            total -= precent10
        return round(total, 2)

    def checkout(self) -> None:
        # Mark cart as checked out (only if it has items and isn't already checked out)
        if not self._is_checked_out and len(self._items):
            self._is_checked_out = True


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Laptop", 999.99)
    cart.add_item("Mouse", 29.99)

    print(f"Total: ${cart.get_total():.2f}")                     # 1029.98

    print(f"Discount: {str(cart.apply_discount('SAVE10')).lower()}")          # true
    print(f"Total: ${cart.get_total():.2f}")                     # 926.98

    print(f"Discount: {str(cart.apply_discount('SAVE10')).lower()}")          # false

    cart.checkout()
    cart.add_item("Keyboard", 79.99)  # Should be rejected
    print(f"Total: ${cart.get_total():.2f}")                     # 926.98

    sensor = TemperatureSensor()
    sensor.add_reading(22.5)
    sensor.add_reading(23.1)
    sensor.add_reading(200.0)  # Should be rejected
    sensor.add_reading(-10.0)

    print(f"Count: {sensor.get_reading_count()}")  # 3
    print(f"Average: {sensor.get_average()}")       # 11.87

    copyList = sensor.get_readings()
    
    print(sensor.is_same(copyList))