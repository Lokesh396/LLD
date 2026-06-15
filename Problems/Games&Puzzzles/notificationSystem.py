import random
from abc import ABC, abstractmethod


class Notification:

    def __init__(self, message: str, user):
        self.user = user
        self.message = message


class Subscriber(ABC):

    @abstractmethod
    def update(self, topic_name, message):
        pass


class User(Subscriber):

    def __init__(self, name: str, channels: list[str], notification_service):
        self.name = name
        self.channels = channels          # preferred channels, e.g. ["email", "sms"]
        self.notification_service = notification_service

    # Observer hook: the topic calls this when it publishes
    def update(self, topic_name, message):
        self.notification_service.notify(self, f"[{topic_name}] {message}")


class NotificationChannel(ABC):

    # fail_rate simulates a flaky channel (0.0 = never fails, 1.0 = always fails)
    fail_rate = 0.0

    @abstractmethod
    def send(self, notification):
        pass

    def _maybe_fail(self):
        if random.random() < self.fail_rate:
            raise Exception("network error")


class EmailChannel(NotificationChannel):
    fail_rate = 0.6                       # flaky: fails ~60% of the time

    def send(self, notification):
        self._maybe_fail()
        print(f" Email-> {notification.user.name} {notification.message}")


class SMSChannel(NotificationChannel):
    fail_rate = 0.3

    def send(self, notification):
        self._maybe_fail()
        print(f" SMS-> {notification.user.name} {notification.message}")


class WhatsappChannel(NotificationChannel):

    def send(self, notification):
        self._maybe_fail()
        print(f" Whatsapp-> {notification.user.name} {notification.message}")


class ChannelFactory:

    channels = {
        "email": EmailChannel,
        "whatsapp": WhatsappChannel,
        "sms": SMSChannel
    }

    @classmethod
    def get_channel(cls, channel):
        if channel not in cls.channels:
            raise Exception('channel not available')
        return cls.channels[channel]()


class RetryService:

    @staticmethod
    def execute(fn, retries=3):
        for attempt in range(retries):
            try:
                fn()
                return
            except Exception as e:
                print(f"Retry {attempt + 1} after error: {e}")
        raise Exception("failed after retries")


class NotificationService:

    def notify(self, user: User, message: str):
        notification = Notification(message, user)
        for channel_type in user.channels:
            channel = ChannelFactory.get_channel(channel_type)
            try:
                RetryService.execute(lambda: channel.send(notification))
            except Exception:
                print(f" Giving up on {channel_type} for {user.name}")


class Topic:
    """Subject in the Observer pattern: users subscribe, publish fans out to all."""

    def __init__(self, name: str):
        self.name = name
        self._subscribers: list[Subscriber] = []

    def subscribe(self, subscriber: Subscriber):
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)

    def publish(self, message: str):
        for subscriber in self._subscribers:
            subscriber.update(self.name, message)


if __name__ == "__main__":
    service = NotificationService()

    alice = User("Alice", ["email", "sms"], service)
    bob = User("Bob", ["whatsapp"], service)

    orders = Topic("orders")
    orders.subscribe(alice)
    orders.subscribe(bob)

    print("--- publishing to 'orders' ---")
    orders.publish("Your order has shipped!")

    print("--- Bob unsubscribes ---")
    orders.unsubscribe(bob)
    orders.publish("Order delivered!")
