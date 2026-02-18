from enum import Enum

class TrafficLight(Enum):
    # Set values to duration: RED = 30, YELLOW = 5, GREEN = 25
    RED = 30
    YELLOW = 5
    GREEN = 25

    def next(self) -> "TrafficLight":
        # Return next light: RED->GREEN, GREEN->YELLOW, YELLOW->RED
        if self.value == 30:
           return TrafficLight.GREEN
        elif self.value == 25:
            return TrafficLight.YELLOW
        return TrafficLight.RED

    def display(self) -> None:
        # Print: "COLOR (Xs)" e.g. "RED (30s)"
        print(f'{self.name} ({self.value}s)')


class HttpStatus(Enum):
    # Set values to (code, message) tuples:
    # OK = (200, "OK"), BAD_REQUEST = (400, "Bad Request"),
    # NOT_FOUND = (404, "Not Found"), INTERNAL_SERVER_ERROR = (500, "Internal Server Error")
    OK = (200, "OK")
    BAD_REQUEST = (400, "Bad  Request")
    NOT_FOUND = (404, "Not Found")
    INTERNAL_SERVER_ERROR = (500, "Internal Server Error")

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

    def is_success(self) -> bool:
        # Return True if code < 400
        if self.code < 400:
            return True
        return False

    def display(self) -> None:
        # Print: "CODE MESSAGE" e.g. "200 OK"
        print(f'{self.code} {self.message}')

    @staticmethod
    def from_code(code: int):
        # Return the HttpStatus matching the code, or None if not found
        if code == 200:
            return HttpStatus.OK
        elif code == 400:
            return HttpStatus.BAD_REQUEST
        elif code == 404:
            return HttpStatus.NOT_FOUND
        elif code == 500:
            return HttpStatus.INTERNAL_SERVER_ERROR
        return None


if __name__ == "__main__":
    HttpStatus.OK.display()
    HttpStatus.NOT_FOUND.display()

    print(f"Is 200 success? {str(HttpStatus.OK.is_success()).lower()}")
    print(f"Is 404 success? {str(HttpStatus.NOT_FOUND.is_success()).lower()}")

    found = HttpStatus.from_code(500)
    if found is not None:
        print("Found by code 500: ", end="")
        found.display()
    

    light = TrafficLight.RED
    for _ in range(6):
        light.display()
        light = light.next()
    