class BankAccount:
    def __init__(self, account_number: str, owner_name: str):
        # Initialize fields: account_number, owner_name, balance (starts at 0)
        self.account_number = account_number
        self.owner_name = owner_name
        self.amount = 0
    def deposit(self, amount: float) -> None:
        # Add amount to balance (only if amount is positive)
        if amount < 0:
            return 
        self.amount += float(amount)

    def withdraw(self, amount: float) -> bool:
        # Remove amount from balance if sufficient funds exist
        # Return True if successful, False otherwise
        if self.amount >= amount:
            self.amount -= amount
            return True
        return False

    def get_balance(self) -> float:
        # Return the current balance
        return self.amount
    
class Book:
    def __init__(self, title: str, author: str, isbn: str):
        # Initialize fields: title, author, isbn, is_available (starts as True)
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def borrow_book(self) -> bool:
        # Mark book as unavailable if currently available
        # Return True if successful, False if already borrowed
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self) -> None:
        # Mark book as available
        self.available = True

    def display_info(self) -> None:
        # Print: "Title by Author (ISBN: isbn) - Available" or "- Borrowed"
        print(f"{self.title} by {self.author} (ISBN: {self.isbn}) -",'Available' if self.available else 'Borrowed')


   
def main():
    account = BankAccount("123456", "John Doe")
    account.deposit(1000)
    print(account.get_balance())  # Should print 1000.0

    success = account.withdraw(500)
    print(str(success).lower())   # Should print true
    print(account.get_balance())  # Should print 500.0

    success = account.withdraw(1000)
    print(str(success).lower())   # Should print false

    book = Book("The Pragmatic Programmer", "David Thomas", "978-0135957059")
    book.display_info()

    success = book.borrow_book()
    print(f"Borrow successful: {str(success).lower()}")
    book.display_info()

    success = book.borrow_book()
    print(f"Borrow successful: {str(success).lower()}")

    book.return_book()
    book.display_info()

if __name__ == "__main__":
   main()

