from abc import ABC, abstractmethod

# Before: Fat interface forces BasicPrinter to implement everything
class MultiFunctionDevice(ABC):
    @abstractmethod
    def print_doc(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

    @abstractmethod
    def fax(self, document, number):
        pass

    @abstractmethod
    def staple(self, document):
        pass

class BasicPrinter(MultiFunctionDevice):
    def print_doc(self, document):
        print(f"Printing: {document}")

    def scan(self, document):
        raise NotImplementedError("BasicPrinter cannot scan.")

    def fax(self, document, number):
        raise NotImplementedError("BasicPrinter cannot fax.")

    def staple(self, document):
        raise NotImplementedError("BasicPrinter cannot staple.")

# if __name__ == "__main__":
#     printer = BasicPrinter()
#     printer.print_doc("report.pdf")

# TODO: Create Printable, Scannable, Faxable, and Stapleable interfaces.
# TODO: Refactor BasicPrinter to implement only Printable.
# TODO: Create an OfficePrinter that implements Printable, Scannable, and Faxable.
# TODO: Create a FullDevice that implements all four interfaces.


class Printable(ABC):

    @abstractmethod
    def print_doc(self, document):
        pass

class Faxable(ABC):

    @abstractmethod
    def fax(self, document, number):
        pass

class Stapleable(ABC):

    @abstractmethod
    def staple(self, document):
        pass

class Scannable(ABC):

    @abstractmethod
    def scan(self, documnent):
        pass

class NormalPrinter(Printable):

    def print_doc(self, document):
        print(f'Printing doc: {document}')

class OfficePrinter(Printable, Scannable, Faxable):

    def print_doc(self, document):
        print(f'Printing doc: {document}')

    def scan(self, documnent):
        print('Scanning document')
        return documnent

    def fax(self, document, number):
        print(f'sending fax to {number} with {document}')


if __name__ == '__main__':

    basicprinter  = NormalPrinter()
    basicprinter.print_doc('Hello world!')
    officeprinter = OfficePrinter()
    document = 'Hello there'
    officeprinter.scan(document)
    officeprinter.print_doc(document)
    officeprinter.fax(document, '1221')