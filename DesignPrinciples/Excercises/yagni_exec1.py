from abc import ABC, abstractmethod

class ValidationRule(ABC):
    @abstractmethod
    def check(self, input_str: str) -> bool:
        pass

class MinLengthRule(ValidationRule):
    def __init__(self, min_length: int):
        self.min_length = min_length

    def check(self, input_str: str) -> bool:
        return len(input_str) >= self.min_length

class HasUpperCaseRule(ValidationRule):
    def check(self, input_str: str) -> bool:
        for c in input_str:
            if c.isupper():
                return True
        return False

class HasDigitRule(ValidationRule):
    def check(self, input_str: str) -> bool:
        for c in input_str:
            if c.isdigit():
                return True
        return False

class PasswordValidator:
    def __init__(self, rules: list):
        self.rules = rules

    def is_valid(self, password: str) -> bool:
        for rule in self.rules:
            if not rule.check(password):
                return False
        return True
    


class PasswordValidator:
    def is_valid(self, password: str) -> bool:
        # Your implementation here
        return len(password) >= 8

validator = PasswordValidator()
print(str(validator.is_valid("short")).lower())
print(str(validator.is_valid("longenough")).lower())
print(str(validator.is_valid("12345678")).lower())
print(str(validator.is_valid("")).lower())