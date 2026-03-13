from abc import ABC, abstractmethod
"""
Open Closed Principle - Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification. — Bertrand Meyer

Open for extension - The behaviour of the entity can be extended. As new requirements comes in (likes new payment types), you should be able to add new behavor without 
changing already existing code.

Closed for Modification - The existing, working code should not be changed. Once it is
written, tested, and working, you should not need to go back and alter it too add new
features. 
we can achieve this using interfaces, polymorphism etc.

Why OCP Matter.

1. Improved Maintainability
2. Enhanced Scalability
3. Reduced Risk
4. Better Testability
5. Increased Reusability
6. Clearer Code

Common Pifalls

1. over enginerring / premature abstraction
2. Abstraction Hell
3. Forgetting the why(maintainability, scalability)
4. not anticipating the right extension points
"""


# Bad Code

class PaymentProcessor:
    def process_credit_card_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")
        # Complex logic for credit card processing

    def process_paypal_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")
        # Logic for PayPal processing

class CheckoutService:
    def process_payment(self, payment_type):
        processor = PaymentProcessor()

        if payment_type == "CreditCard":
            processor.process_credit_card_payment(100.00)
        elif payment_type == "PayPal":
            processor.process_paypal_payment(100.00)

# OCP Compilent Code

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")
        # Complex logic for credit card processing

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")
        # Logic for PayPal processing

class UPIPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing UPI payment of ₹{amount * 80}")  # Assuming conversion rate
        # Logic for UPI processing

class PaymentProcessor:
    def process(self, payment_method: PaymentMethod, amount):
        # No more if-else! The processor doesn't care about the specific type.
        # It just knows it can call processPayment.
        payment_method.process_payment(amount)

class CheckoutService:
    def process_payment(self, method: PaymentMethod, amount):
        processor = PaymentProcessor()
        processor.process(method, amount)

# Usage
checkout = CheckoutService()
checkout.process_payment(CreditCardPayment(), 100.00)
checkout.process_payment(PayPalPayment(), 100.00)
checkout.process_payment(UPIPayment(), 100.00)