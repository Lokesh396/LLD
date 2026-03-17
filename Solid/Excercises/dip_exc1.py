# Before: OrderService is tightly coupled to MySQLDatabase
class MySQLDatabase:
    def insert(self, table: str, data: str) -> None:
        print(f"MySQL: Inserting into {table} -> {data}")

    def query(self, table: str, id: str) -> str:
        print(f"MySQL: Querying {table} for id {id}")
        return f"{{ id: {id}, item: 'Widget' }}"

class OrderService:
    def __init__(self):
        self.database = MySQLDatabase()  # Direct dependency!

    def place_order(self, order_id: str, order_data: str) -> None:
        print(f"Placing order: {order_id}")
        self.database.insert("orders", order_data)
        print("Order placed successfully.")

    def get_order(self, order_id: str) -> str:
        return self.database.query("orders", order_id)

if __name__ == "__main__":
    service = OrderService()
    service.place_order("ORD-001", "{ item: 'Widget', qty: 3 }")
    order = service.get_order("ORD-001")
    print(f"Order: {order}")

# TODO: Create a Database ABC with insert() and query() methods.
# TODO: Make MySQLDatabase implement the interface.
# TODO: Create a PostgresDatabase that prints "PostgreSQL: ..." instead of "MySQL: ...".
# TODO: Refactor OrderService to accept a Database via its constructor.


from abc import ABC, abstractmethod

class Database(ABC):

    @abstractmethod
    def insert(table, data):
        pass
    
    @abstractmethod
    def query(self, table, id):
        return

class NewOrderService:
    def __init__(self, database):
        self.database = database  # dependency inversion

    def place_order(self, order_id: str, order_data: str) -> None:
        print(f"Placing order: {order_id}")
        self.database.insert("orders", order_data)
        print("Order placed successfully.")

    def get_order(self, order_id: str) -> str:
        return self.database.query("orders", order_id)

class MySQLDatabaseV1(Database):
    def insert(self, table: str, data: str) -> None:
        print(f"MySQL: Inserting into {table} -> {data}")

    def query(self, table: str, id: str) -> str:
        print(f"MySQL: Querying {table} for id {id}")
        return f"{{ id: {id}, item: 'Widget' }}"


class PSQLDatabaseV1(Database):
    def insert(self, table: str, data: str) -> None:
        print(f"PSQL: Inserting into {table} -> {data}")

    def query(self, table: str, id: str) -> str:
        print(f"PSQL: Querying {table} for id {id}")
        return f"{{ id: {id}, item: 'Widget' }}"

if __name__ == "__main__":
    service = OrderService()
    service.place_order("ORD-001", "{ item: 'Widget', qty: 3 }")
    order = service.get_order("ORD-001")
    print(f"Order: {order}")

    database = MySQLDatabase()
    servicenew = NewOrderService(database)
    servicenew.place_order("ORD-001", "{ item: 'Widget', qty: 3 }")
    order1 = service.get_order("ORD-001")
    print(f"Order: {order}")