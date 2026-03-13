from abc import ABC, abstractmethod
class ShippingCostCalculator:
    def calculate(self, shipping_type: str, weight: float) -> float:
        if shipping_type == "Standard":
            return weight * 1.5
        elif shipping_type == "Express":
            return weight * 3.0
        elif shipping_type == "Overnight":
            return weight * 5.0
        elif shipping_type == "International":
            return weight * 10.0
        raise ValueError(f"Unknown shipping type: {shipping_type}")

# Usage
calculator = ShippingCostCalculator()
print(f"Standard: ${calculator.calculate('Standard', 2.0)}")
print(f"Express: ${calculator.calculate('Express', 2.0)}")

# TODO: Define a ShippingStrategy interface (ABC) with a calculate_cost(weight) method.
# TODO: Create concrete implementations for each shipping type.
# TODO: Refactor ShippingCostCalculator to accept a ShippingStrategy.


class ShippingStrategy(ABC):

    @abstractmethod
    def calculate_cost(self, weight):
        pass


class StandardShipping(ShippingStrategy):

    def calculate_cost(self, weight):
        print(f"Standard: ${1.5 * weight}")

class ExpressShipping(ShippingStrategy):
    
    def calculate_cost(self, weight):
        print(f"Express: ${3 * weight}")


class OvernightShipping(ShippingStrategy):

    def calculate_cost(self, weight):
        print(f"Overnight: ${5 * weight}")

    
class InternationalShipping(ShippingStrategy):

    def calculate_cost(self, weight):
        print(f"International: ${10 * weight}")

    

class ShippingCalculatorv2:

    def __init__(self, shippingmethod:ShippingStrategy):
        self.shippingmethod = shippingmethod
    
    def calculate_cost(self, weight):
        self.shippingmethod.calculate_cost(weight)

if __name__ == '__main__':
    weight = 10

    calculator1 = ShippingCalculatorv2(InternationalShipping())
    calculator1.calculate_cost(weight)