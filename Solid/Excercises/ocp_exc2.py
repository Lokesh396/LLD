from abc import ABC, abstractmethod

class NotificationService:
    def send_notification(self, channel: str, message: str) -> None:
        if channel == "Email":
            print(f"Sending EMAIL: {message}")
            # Email-specific logic (SMTP, templates, etc.)
        elif channel == "SMS":
            print(f"Sending SMS: {message}")
            # SMS-specific logic (Twilio, carrier API, etc.)
        else:
            raise ValueError(f"Unknown channel: {channel}")

# Usage
service = NotificationService()
service.send_notification("Email", "Your order has shipped!")
service.send_notification("SMS", "Your order has shipped!")

# TODO: Define a NotificationChannel interface (ABC) with a send(message) method.
# TODO: Create EmailChannel, SMSChannel, PushChannel, and SlackChannel.
# TODO: Refactor NotificationService to accept a NotificationChannel.


class NotificationChannel(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailChannel(NotificationChannel):

    def send(self, message):
        print(f"Sending Email: {message}")

class SMSChannel(NotificationChannel):

    def send(self, message):
        print(f"Sending SMS: {message}")

class PushChannel(NotificationChannel):

    def send(self, message):
        print(f"Sending Push: {message}")

class SlackChannel(NotificationChannel):

    def send(self, message):
        print(f"Sending Slack: {message}")


class NotificationServiceV1:

    def __init__(self, channel:NotificationChannel):
        self._channel = channel

    def sendMessage(self, message):
        self._channel.send(message)

if __name__ == '__main__':

    message = 'Order Placed'
    slack  = SlackChannel()
    notificationservice = NotificationServiceV1(slack)
    notificationservice.sendMessage(message=message)