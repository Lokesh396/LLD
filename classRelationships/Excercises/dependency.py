class FileReader:
    def read(self, file_path):
        # TODO: Simulate reading a file and return its content
        return f"{file_path}"

class FormatParser:
    def parse(self, content, target_format):
        # TODO: Simulate converting content to the target format
        print(f'converting to target format: {target_format}')
        return content

class FileWriter:
    def write(self, file_path, content):
        # TODO: Simulate writing content to a file
        print(f'writing to a file: {file_path} with content: {content}')

class FileConverter:
    def convert(self, source_path, target_path, target_format,
                reader, parser, writer):
        # TODO: Use reader to read, parser to parse, writer to write
        # Print each step so you can verify the flow
        content = reader.read(source_path)
        content = parser.parse(content, target_format)
        writer.write(target_path, content)



class InventoryChecker:
    def check_stock(self, item_name, quantity):
        # TODO: Simulate checking inventory
        # Return True if available, False otherwise
        if quantity & 1 and item_name:
            return True
        
        return False

class PriceCalculator:
    def calculate(self, item_name, quantity):
        # TODO: Simulate calculating the price
        return quantity * 100.0

class InvoiceGenerator:
    def generate(self, item_name, quantity, total):
        # TODO: Simulate generating an invoice string
        return f"Invoice for {item_name} - {quantity}: ${total}"

class OrderProcessor:
    def process_order(self, item_name, quantity, checker, calculator, generator):
        # TODO: Check stock, calculate price, generate invoice
        # Return the invoice string, or an error message if out of stock
        if checker.check_stock(item_name, quantity):
            price = calculator.calculate(item_name, quantity)
            return generator.generate(item_name, quantity, price)
        return ''

if __name__ == "__main__":
    processor = OrderProcessor()

    checker = InventoryChecker()
    calculator = PriceCalculator()
    generator = InvoiceGenerator()

    invoice = processor.process_order("Laptop", 3, checker, calculator, generator)
    print(invoice)

    converter = FileConverter()

    reader = FileReader()
    parser = FormatParser()
    writer = FileWriter()

    converter.convert("data.csv", "output.json", "JSON", reader, parser, writer)