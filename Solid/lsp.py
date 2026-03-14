"""
Liskov Substitution Principle (LSP) - "If S is a subtype of T, then objects 
of type T may be replaced with objects of type S without altering any of the 
desirable properties of that program (correctness, task performed, etc.)." — Barbara Liskov, 1987

Have you ever passed a subclass into a method expecting the parent class… and watched your program crash or behave in unexpected ways?

Or extended a class… only to find yourself overriding methods just to throw exceptions?
This is the direct voilation of LSP.


why does LSP Matter ?

1. Reliability and Predicatability
2. Reduced Bugs
3. Maintainability and extensibility
4. True Polymorphism
5. Testability

Just because we see a is a relationship we cant force inheritance
"""

# LSP Voilations 
class Document:
    def __init__(self, data):
        self.data = data

    def open(self):
        print("Document opened. Data:", self.data[:20] + "...")

    def save(self, new_data):
        self.data = new_data
        print("Document saved.")

    def get_data(self):
        return self.data
    
class ReadOnlyDocument(Document):
    def __init__(self, data):
        super().__init__(data)

    def save(self, new_data):
        raise TypeError("Cannot save a read-only document!")
    

class DocumentProcessor:
    def process_and_save(self, doc, additional_info):
        doc.open()
        current_data = doc.get_data()
        new_data = current_data + " | Processed: " + additional_info
        doc.save(new_data)  # Assumes all Documents are savable
        print("Document processing complete.")

if __name__ == "__main__":
    regular_doc = Document("Initial project proposal content.")
    confidential_report = ReadOnlyDocument("Top secret government data.")

    processor = DocumentProcessor()

    print("--- Processing Regular Document ---")
    processor.process_and_save(regular_doc, "Reviewed by Alice")

    print("\n--- Processing ReadOnly Document ---")
    try:
        processor.process_and_save(confidential_report, "Reviewed by Bob")
    except TypeError as e:
        print("Error:", str(e))

# Fixing with LSP

from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

class Editable(Document):
    @abstractmethod
    def save(self, new_data):
        pass

class EditableDocument(Editable):
    def __init__(self, data):
        self.data = data

    def open(self):
        print("Editable Document opened. Data:", self._preview())

    def save(self, new_data):
        self.data = new_data
        print("Document saved.")

    def get_data(self):
        return self.data

    def _preview(self):
        return self.data[:20] + "..."
    
class ReadOnlyDocument(Document):
    def __init__(self, data):
        self.data = data

    def open(self):
        print("Read-Only Document opened. Data:", self._preview())

    def get_data(self):
        return self.data

    def _preview(self):
        return self.data[:20] + "..."
    
class DocumentProcessor:
    def process(self, doc: Document):
        doc.open()
        print("Document processed.")

    def process_and_save(self, doc: Editable, additional_info: str):
        doc.open()
        current_data = doc.get_data()
        new_data = current_data + " | Processed: " + additional_info
        doc.save(new_data)
        print("Editable document processed and saved.")

if __name__ == "__main__":
    editable = EditableDocument("Draft proposal for Q3.")
    read_only = ReadOnlyDocument("Top secret strategy.")

    processor = DocumentProcessor()

    print("--- Processing Editable Document ---")
    processor.process_and_save(editable, "Reviewed by Alice")

    print("\n--- Processing Read-Only Document ---")
    processor.process(read_only)  # This works fine