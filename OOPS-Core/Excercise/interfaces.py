from abc import ABC, abstractmethod

class Formatter(ABC):
    @abstractmethod
    def format(self, message: str) -> str:
        pass

class PlainFormatter(Formatter):
    def format(self, message: str) -> str:
        return message

class JsonFormatter(Formatter):
    def format(self, message: str) -> str:
        return '{"log": "' + message + '"}'

class Logger:
    def __init__(self, formatter: Formatter):
        self._formatter = formatter

    def log(self, message: str) -> None:
        print(self._formatter.format(message))



class Validator(ABC):
    @abstractmethod
    def validate(self, input: str) -> bool:
        pass

class EmailValidator(Validator):
    def validate(self, input: str) -> bool:
        # Return True if "@" in input
        return '@' in input

class PasswordValidator(Validator):
    def validate(self, input: str) -> bool:
        # Return True if len(input) >= 8
        return len(input) >= 8

class RegistrationService:
    def __init__(self, validators: list[Validator]):
        self._validators = validators

    def register(self, input: str) -> None:
        # Run all validators on input. If all pass, print "input" - PASSED
        # If any fail, print "input" - FAILED
        for validator in self._validators:
            if not validator.validate(input):
                print(f'"{input}" - FAILED')
                return
        
        print(f'"{input}" - PASSED')



if __name__ == "__main__":
    email_reg = RegistrationService([EmailValidator()])
    email_reg.register("user@example.com")  # Should pass
    email_reg.register("invalid-email")      # Should fail

    pass_reg = RegistrationService([PasswordValidator()])
    pass_reg.register("strongpassword")  # Should pass
    pass_reg.register("short")            # Should fail

    plain_logger = Logger(PlainFormatter())
    plain_logger.log("Server started on port 8080")

    json_logger = Logger(JsonFormatter())
    json_logger.log("Server started on port 8080")