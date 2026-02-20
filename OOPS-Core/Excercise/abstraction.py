from abc import ABC, abstractmethod

class DataExporter(ABC):
    def validate(self, data: list) -> bool:
        # Return False and print "Export failed: No data to export." if data is empty
        # Return True and print "Validation passed. Exporting N records." otherwise
        if not data:
            print("Export failed: No data to export.")
            return False
        print(f"Validation passed. Exporting {len(data)} records.")
        return True

    @abstractmethod
    def export(self, data: list) -> None:
        pass

class CSVExporter(DataExporter):
    def export(self, data: list) -> None:
        # Call self.validate(data) first. If validation fails, return early.
        # Otherwise, print CSV format: "CSV: Alice,Bob,Charlie"
        # Hint: use ",".join(data)
        if not self.validate(data):
            return
        print("CSV:", ",".join(data))
        

class JSONExporter(DataExporter):
    def export(self, data: list) -> None:
        # Call self.validate(data) first. If validation fails, return early.
        # Otherwise, print JSON array format: JSON: ["Alice", "Bob", "Charlie"]
        if not self.validate(data):
            return
        items = ", ".join(f'"{item}"' for item in data)
        print(f'JSON: [{items}]')

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def describe(self) -> None:
        # Print: "Shape: [name], Area: [area], Perimeter: [perimeter]"
        # Use f-string with :.2f for formatting
        print(f"Shape: {self._name}, Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}")

class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__("Circle")
        self._radius = radius

    def area(self) -> float:
        # Area = pi * r^2
        return round(math.pi * (self._radius ** 2), 2)

    def perimeter(self) -> float:
        # Perimeter = 2 * pi * r
        return round(2 * math.pi * self._radius, 2)

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__("Rectangle")
        self._width = width
        self._height = height

    def area(self) -> float:
        # Area = width * height
        return round(self._width * self._height, 2)

    def perimeter(self) -> float:
        # Perimeter = 2 * (width + height)
        return round(2 * (self._width + self._height), 2)

if __name__ == "__main__":
    csv = CSVExporter()
    csv.export(["Alice", "Bob", "Charlie"])

    print()

    json_exp = JSONExporter()
    json_exp.export(["Alice", "Bob", "Charlie"])

    print()

    csv.export([])  # Should fail validation

    circle = Circle(5.0)
    circle.describe()

    rectangle = Rectangle(4.0, 6.0)
    rectangle.describe()