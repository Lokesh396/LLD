'''
Every piece of knowledge must have a single, unambigous, authoritative represntation
within a system. -- The Pragmatic Programmer

The quote says knowlege not code, it is not avoiding duplicated line of code.
It applies to -
 - Business rules
 - configuration
 - Data models
 - Documentation
 - Tests

The Rule of three- before extracting every bit of repeated code into a shared utility,
there is an important guide line rule of three, wait until you see the same pattern
three times.

Why Reptetion is a problem
1. Hard to maintain
2. Higher risk of Bugs
3. Bloated codebase
4. poor test coverage

when it is okay to repeat
1. Avoid premature Abstractions:
    Duplication is far chepaer than the wrong abstraction - Sandi Metz
2. Keep Tests Readble
3. Keep it simple
'''

# Before Dry

class OrderService:
    def notify_order_confirmation(self, user_id: str, order_id: str) -> None:
        # Duplicated: message formatting
        message = f"[Order] Hi {user_id}, your order {order_id} has been confirmed."
        formatted = message[0].upper() + message[1:]

        # Duplicated: sending logic
        print("Connecting to notification API...")
        print(f"Sending to {user_id}: {formatted}")
        print("Notification sent successfully.")

class ShippingService:
    def notify_shipment_update(self, user_id: str, tracking_id: str) -> None:
        # Duplicated: message formatting
        message = f"[Shipping] Hi {user_id}, your shipment {tracking_id} is on its way."
        formatted = message[0].upper() + message[1:]

        # Duplicated: sending logic
        print("Connecting to notification API...")
        print(f"Sending to {user_id}: {formatted}")
        print("Notification sent successfully.")

class SupportService:
    def notify_ticket_resolution(self, user_id: str, ticket_id: str) -> None:
        # Duplicated: message formatting
        message = f"[Support] Hi {user_id}, your ticket {ticket_id} has been resolved."
        formatted = message[0].upper() + message[1:]

        # Duplicated: sending logic
        print("Connecting to notification API...")
        print(f"Sending to {user_id}: {formatted}")
        print("Notification sent successfully.")

# After Dry

class MessageFormatter:
    @staticmethod
    def format(category: str, user_id: str, detail: str) -> str:
        message = f"[{category}] Hi {user_id}, {detail}"
        return message[0].upper() + message[1:]

class NotificationSender:
    @staticmethod
    def send(user_id: str, message: str) -> None:
        print("Connecting to notification API...")
        print(f"Sending to {user_id}: {message}")
        print("Notification sent successfully.")

class OrderService:
    def notify_order_confirmation(self, user_id: str, order_id: str) -> None:
        message = MessageFormatter.format(
            "Order", user_id, f"your order {order_id} has been confirmed.")
        NotificationSender.send(user_id, message)

class ShippingService:
    def notify_shipment_update(self, user_id: str, tracking_id: str) -> None:
        message = MessageFormatter.format(
            "Shipping", user_id, f"your shipment {tracking_id} is on its way.")
        NotificationSender.send(user_id, message)

class SupportService:
    def notify_ticket_resolution(self, user_id: str, ticket_id: str) -> None:
        message = MessageFormatter.format(
            "Support", user_id, f"your ticket {ticket_id} has been resolved.")
        NotificationSender.send(user_id, message)

# single source of truth for formatting and sending.
# Each service focuses on its own responsibility
# East to test
# East to extend

