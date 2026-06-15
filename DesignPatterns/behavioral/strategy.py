"""
The strategy design pattern is a behavioral pattern that lets you define a family of
algorithms, encapsulates each one in its own class, and make them interchangeable at
runtime.
"""


from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, expiry_date: str):
        self.card_number = card_number
        self.expiry_date = expiry_date

    def pay(self, amount: float) -> bool:
        print(f"Charging ${amount} to credit card ending in {self.card_number[-4:]}")
        return True

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float) -> bool:
        print(f"Sending ${amount} via PayPal to {self.email}")
        return True

class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def pay(self, amount: float) -> bool:
        print(f"Transferring ${amount} in crypto to {self.wallet_address}")
        return True

class CheckoutService:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount: float) -> bool:
        return self.payment_strategy.pay(amount)

# Usage
checkout = CheckoutService(CreditCardPayment("4111111111111111", "12/26"))
checkout.checkout(99.99)

checkout.set_payment_strategy(PayPalPayment("user@example.com"))
checkout.checkout(49.99)

checkout.set_payment_strategy(CryptoPayment("0xABC123..."))
checkout.checkout(149.99)