from abc import ABC, abstractmethod

# Before: Each processor duplicates tax calculation
class USOrderProcessor:
    def process_order(self, amount: float) -> None:
        tax = amount * 0.10  # Duplicated tax logic
        total = amount + tax
        print(f"US Order - Subtotal: ${amount:.2f}, Tax: ${tax:.2f}, Total: ${total:.2f}")

class EUOrderProcessor:
    def process_order(self, amount: float) -> None:
        tax = amount * 0.20  # Duplicated tax logic
        total = amount + tax
        print(f"EU Order - Subtotal: ${amount:.2f}, Tax: ${tax:.2f}, Total: ${total:.2f}")

class UKOrderProcessor:
    def process_order(self, amount: float) -> None:
        tax = amount * 0.15  # Duplicated tax logic
        total = amount + tax
        print(f"UK Order - Subtotal: ${amount:.2f}, Tax: ${tax:.2f}, Total: ${total:.2f}")

# TODO: Extract a TaxCalculator interface (ABC) and region implementations.
# TODO: Refactor OrderProcessor to accept a TaxCalculator.


class TaxCalculator(ABC):

    @abstractmethod
    def calculate_tax(self):
        pass

    @abstractmethod
    def get_region(self):
        pass
class UsTaxCalculator(TaxCalculator):
    
    def calculate_tax(self, amount):
        return amount * 0.10
    
    def get_region(self):
        return 'US'

class EuTaxCalculator(TaxCalculator):
    def calculate_tax(self, amount):
        return amount * 0.20
    
    def get_region(self):
        return 'EU'

class UkTaxCalculator(TaxCalculator):
    def calculate_tax(self, amount):
        return amount * 0.15
    
    def get_region(self):
        return 'UK'


class OrderProcessor():

    def __init__(self, processor):
        self.taxprocessor = processor

    def process_order(self, amount):
        tax = self.taxprocessor.calculate_tax(amount)
        total = tax + amount
        region = self.taxprocessor.get_region()
        print(f"{region} Order - Subtotal: ${amount:.2f}, Tax: ${tax:.2f}, Total: ${total:.2f}")


if __name__ == "__main__":
    # After refactoring, usage should look like:
    us_processor = OrderProcessor(EuTaxCalculator())
    us_processor.process_order(100.0)
    pass