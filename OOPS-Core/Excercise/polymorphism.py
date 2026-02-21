from abc import ABC, abstractmethod


class Discount(ABC):
    def __init__(self, label: str):
        self._label = label

    @abstractmethod
    def apply(self, price: float) -> float:
        pass

    def describe(self, original_price: float):
        # TODO: call self.apply(original_price) and print:
        #   "label: $original_price -> $discounted_price"
        # Hint: use f"{value:.2f}" for formatting
        discount_price = self.apply(original_price)
        print(f"{self._label}: ${original_price} -> ${discount_price:.2f}")


class PercentageDiscount(Discount):
    def __init__(self, percentage: float):
        super().__init__(f"{percentage:.1f}% off")
        # TODO: initialize self._percentage
        self._percentage = percentage

    def apply(self, price: float) -> float:
        # TODO: return price * (1 - percentage / 100)
        return price * (1-self._percentage/100)


class FlatDiscount(Discount):
    def __init__(self, amount: float):
        super().__init__(f"${amount:.1f} off")
        # TODO: initialize self._amount
        self._amount = amount

    def apply(self, price: float) -> float:
        # TODO: return max(price - amount, 0)
        return max(price-self._amount, 0)


class BuyOneGetOneFree(Discount):
    def __init__(self):
        super().__init__("Buy 1 Get 1 Free")

    def apply(self, price: float) -> float:
        # TODO: return price / 2
        return price / 2


class OrderProcessor:
    def process_order(self, item_name: str, price: float, discount: Discount):
        # TODO: print "Item: item_name" then call discount.describe(price)
        print(f"Item: {item_name}")
        discount.describe(price)

from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, level: str, message: str) -> None:
        pass

    @abstractmethod
    def get_destination(self) -> str:
        pass


class ConsoleLogger(Logger):
    def log(self, level: str, message: str) -> None:
        # TODO: print "[level] message" to console
        print(f"[{level}] {message}")

    def get_destination(self) -> str:
        # TODO: return "Console"
        return "Console"


class FileLogger(Logger):
    def __init__(self, file_path: str):
        # TODO: initialize self._file_path
        self.file_path = file_path

    def log(self, level: str, message: str) -> None:
        # TODO: print "Writing to file_path: [level] message"
        print(f"Writing to {self.file_path}: [{level}] {message}")

    def get_destination(self) -> str:
        # TODO: return "File: file_path"
        return f"File: {self.file_path}"


class DatabaseLogger(Logger):
    def __init__(self, table_name: str):
        # TODO: initialize self._table_name
        self._table_name = table_name

    def log(self, level: str, message: str) -> None:
        # TODO: print "INSERT INTO table_name: [level] message"
        print(f"INSERT INTO {self._table_name}: [{level}] {message}")

    def get_destination(self) -> str:
        # TODO: return "Database: table_name"
        return f"Database: {self._table_name}"


class Application:
    def __init__(self, logger: Logger):
        # TODO: initialize self._logger
        self._logger = logger
        pass

    def run(self):
        # TODO: log three messages with level "INFO":
        #   "Application starting..."
        #   "Processing data..."
        #   "Application shutting down."
        self._logger.log('INFO', "Application starting...")
        self._logger.log('INFO', "Processing data...")
        self._logger.log('INFO',  "Application shutting down.")
        pass




if __name__ == "__main__":
    processor = OrderProcessor()

    processor.process_order("Laptop", 999.99, PercentageDiscount(20))
    processor.process_order("Headphones", 49.99, FlatDiscount(15))
    processor.process_order("Keyboard", 79.98, BuyOneGetOneFree())

    loggers = [
        ConsoleLogger(),
        FileLogger("/var/log/app.log"),
        DatabaseLogger("app_logs"),
    ]

    for logger in loggers:
        print(f"--- Using {logger.get_destination()} ---")
        app = Application(logger)
        app.run()
        print()