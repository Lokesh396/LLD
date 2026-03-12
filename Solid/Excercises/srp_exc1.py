# Before: One class doing three unrelated jobs
class GodOrderService:
    def __init__(self):
        self.inventory = {"LAPTOP": 10, "PHONE": 25, "TABLET": 15}
        self.orders = []

    def place_order(self, product_id: str, quantity: int, customer_email: str):
        # Responsibility 1: Inventory check
        stock = self.inventory.get(product_id, 0)
        if stock < quantity:
            print(f"Insufficient stock for {product_id}")
            return

        # Responsibility 2: Order processing
        price_per_unit = 100.0
        total = price_per_unit * quantity
        order_id = f"ORD-{len(self.orders) + 1}"
        self.orders.append(order_id)

        # Responsibility 3: Update inventory
        self.inventory[product_id] = stock - quantity

        # Responsibility 4: Send notification
        print(f"Email to {customer_email}: Order {order_id} confirmed. Total: ${total}")

# TODO: Refactor into OrderProcessor, InventoryManager, and NotificationService.


class InventoryService:

    def __init__(self, products):
        self._products = products
    
    def check_product(self, product, quantity):
        if self._products[product] >= quantity:
            return True
        return False

    def updateInventory(self, product, quantity):

        if self.check_product(product, quantity):
            self._products[product] -= quantity
            return True
        return False
    
class NotificationService:
    
    def send_notification(self,customer_email,order_id, total):
        print(f"Email to {customer_email}: Order {order_id} confirmed. Total: ${total}")

    
class OrderService:

    def __init__(self, inventory:InventoryService, notifications:NotificationService):
        self._inventory = inventory
        self._notificaions = notifications
        self.orders = []
    
    def place_order(self, product_id:int, quantity:int, customer_email:str):
        stockExists = self._inventory.check_product(product=product_id, quantity=quantity)
        if not stockExists:
            print(f"Insufficient stock for {product_id}")
            return
        price_per_unit = 100.0
        total = price_per_unit * quantity
        order_id = f"ORD-{len(self.orders) + 1}"
        self.orders.append(order_id)
        if not self._inventory.updateInventory(product=product_id, quantity=quantity):
            print(f"Insufficient stock for {product_id}")
            return

        self._notificaions.send_notification(customer_email=customer_email, order_id=order_id, total=total)

        
if __name__ == "__main__":
    # After refactoring, usage should look like:
    inventory = InventoryService({"LAPTOP": 10, "PHONE": 25, "TABLET": 15})
    notifications = NotificationService()
    processor = OrderService(inventory, notifications)
    processor.place_order("LAPTOP", 2, "alice@example.com")