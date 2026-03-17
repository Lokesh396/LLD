"""
Have you ever tried to swap out a database, switch an email provider,
or replace a third-party API, only to realize that your business logic
was so tangled with the implementation details that changing one thing
meant rewriting half the class?

If so, you have run into a violation of one of the most practical 
design principles in software engineering: the Dependency Inversion Principle (DIP).
"""

# Bad 

class GmailClient:
    def send_gmail(self, to_address, subject_line, email_body):
        print("Connecting to Gmail SMTP server...")
        print(f"Sending email via Gmail to: {to_address}")
        print(f"Subject: {subject_line}")
        print(f"Body: {email_body}")
        # ... actual Gmail API interaction logic ...
        print("Gmail email sent successfully!")

class EmailService:
    def __init__(self):
        self.gmail_client = GmailClient()

    def send_welcome_email(self, user_email, user_name):
        subject = f"Welcome, {user_name}!"
        body = "Thanks for signing up to our awesome platform. We're glad to have you!"
        self.gmail_client.send_gmail(user_email, subject, body)

    def send_password_reset_email(self, user_email):
        subject = "Reset Your Password"
        body = "Please click the link below to reset your password..."
        self.gmail_client.send_gmail(user_email, subject, body)

# If we need to swap to outlook we need to modify  the email service too or else if
# we need to support multiple mailing services we need to write multiple condistions 
# in the code.


# The dependency inversion principle
"""
High-level modules should not depend on low-level modules. Both should depend on abstractions (e.g., interfaces).
Abstractions should not depend on details. Details (concrete implementations) should depend on abstractions.
In plain English:

Business logic should not rely directly on implementation details.
Instead, both should depend on a common interface or abstraction."""

# Applying dip
from abc import ABC, abstractmethod

class EmailClient(ABC):
    @abstractmethod
    def send_email(self, to, subject, body):
        pass


class GmailClientImpl(EmailClient):
    def send_email(self, to, subject, body):
        print("Connecting to Gmail SMTP server...")
        print(f"Sending email via Gmail to: {to}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
        # ... actual Gmail API interaction logic ...
        print("Gmail email sent successfully!")


class OutlookClientImpl(EmailClient):
    def send_email(self, to, subject, body):
        print("Connecting to Outlook Exchange server...")
        print(f"Sending email via Outlook to: {to}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
        # ... actual Outlook API interaction logic ...
        print("Outlook email sent successfully!")


class EmailService:
    def __init__(self, email_client: EmailClient):
        self.email_client = email_client

    def send_welcome_email(self, user_email, user_name):
        subject = f"Welcome, {user_name}!"
        body = "Thanks for signing up to our awesome platform. We're glad to have you!"
        self.email_client.send_email(user_email, subject, body)

    def send_password_reset_email(self, user_email):
        subject = "Reset Your Password"
        body = "Please click the link below to reset your password..."
        self.email_client.send_email(user_email, subject, body)



if __name__ == "__main__":
    print("--- Using Gmail ---")
    gmail_service = EmailService(GmailClientImpl())
    gmail_service.send_welcome_email("test@example.com", "Alice")

    print("\n--- Using Outlook ---")
    outlook_service = EmailService(OutlookClientImpl())
    outlook_service.send_welcome_email("test@example.com", "Alice")