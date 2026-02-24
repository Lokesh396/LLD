class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Catalog:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        # TODO: Add product to catalog
        self.products.append(product)

    def find_by_name(self, name: str):
        # TODO: Find and return product by name, return None if not found
        for product in self.products:
            if product.name == name:
                return product
        return None

    def get_product_count(self):
        return len(self.products)

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product: Product):
        # TODO: Add product to cart
        self.items.append(product)

    def clear_cart(self):
        # TODO: Remove all items (don't destroy the products!)
        self.items = []

    def get_total(self):
        # TODO: Sum prices of all items
        total = 0
        for product in self.items:
            total += product.price
        return total

    def get_item_count(self):
        return len(self.items)

class Customer:
    def __init__(self, name: str, cart: Cart):
        self.name = name
        self.cart = cart

    def checkout(self):
        # TODO: Print cart items and total, then clear cart
        print(f'{self.name} checking out:')
        for p in self.cart.items:
            print(f"  - {p.name}: ${p.price}")
        print(f"  Total: ${self.cart.get_total()}")
        self.cart.clear_cart()

class Employee:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.teams = []

    def add_team(self, team):
        # TODO: Add team to employee's team list
        self.teams.append(team)

    def remove_team(self, team):
        # TODO: Remove team from employee's team list
        self.teams.remove(team)

    def get_team_names(self):
        # TODO: Return list of team names this employee belongs to
        out = []
        for team in self.teams:
            out.append(team.name)
        return out

class Team:
    def __init__(self, name: str):
        self.name = name
        self.members = []

    def add_member(self, employee: Employee):
        # TODO: Add employee to team and register this team on the employee
        self.members.append(employee)
        employee.add_team(self)

    def dissolve(self):
        # TODO: Remove all members, don't destroy employees
        for member in self.members:
            member.teams.remove(self)
        self.members = []

    def get_member_count(self):
        return len(self.members)

class Company:
    def __init__(self, name: str):
        self.name = name
        self.employees = []
        self.teams = []

    def add_employee(self, employee: Employee):
        # TODO: Add employee to company
        self.employees.append(employee)

    def add_team(self, team: Team):
        # TODO: Add team to company
        self.teams.append(team)

    def dissolve_team(self, team: Team):
        # TODO: Dissolve the team and remove it from the company's team list
        team.dissolve()
        self.teams.remove(team)

    def get_employee_count(self):
        return len(self.employees)

    def get_team_count(self):
        return len(self.teams)

if __name__ == "__main__":
    company = Company("TechCorp")

    alice = Employee("Alice", "Engineer")
    bob = Employee("Bob", "Designer")
    charlie = Employee("Charlie", "Engineer")

    company.add_employee(alice)
    company.add_employee(bob)
    company.add_employee(charlie)

    backend = Team("Backend")
    frontend = Team("Frontend")

    company.add_team(backend)
    company.add_team(frontend)

    backend.add_member(alice)
    backend.add_member(charlie)
    frontend.add_member(alice)
    frontend.add_member(bob)

    print("Before dissolving:")
    print(f"  {alice.name}'s teams: [{', '.join(alice.get_team_names())}]")
    print(f"  Backend has {backend.get_member_count()} members")
    print(f"  Company has {company.get_team_count()} teams, {company.get_employee_count()} employees")

    company.dissolve_team(backend)

    print("\nAfter dissolving Backend:")
    print(f"  {alice.name}'s teams: [{', '.join(alice.get_team_names())}]")
    print(f"  {charlie.name}'s teams: [{', '.join(charlie.get_team_names())}]")
    print(f"  Company has {company.get_team_count()} teams, {company.get_employee_count()} employees")
    print(f"  {alice.name} still exists: {alice.role}")

    laptop = Product("Laptop", 999.99)
    mouse = Product("Mouse", 29.99)
    keyboard = Product("Keyboard", 79.99)

    catalog = Catalog()
    catalog.add_product(laptop)
    catalog.add_product(mouse)
    catalog.add_product(keyboard)

    cart1 = Cart()
    cart2 = Cart()

    alice = Customer("Alice", cart1)
    bob = Customer("Bob", cart2)

    cart1.add_item(laptop)
    cart1.add_item(mouse)
    cart2.add_item(laptop)
    cart2.add_item(keyboard)

    print(f"Alice's cart: {cart1.get_item_count()} items, ${cart1.get_total()}")
    print(f"Bob's cart: {cart2.get_item_count()} items, ${cart2.get_total()}")

    alice.checkout()

    print(f"Catalog still has {catalog.get_product_count()} products")
    print(f"Bob's cart still has {cart2.get_item_count()} items")
    print(f"Laptop still exists: {laptop.name}")