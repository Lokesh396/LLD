from datetime import datetime 
class NotificationService:

    """
    Inheritance applies when there is a clear is a relationship.

    Inheritance allows to use all public methods and properties of the parent class, Inheritance is used to group common
    logic at one place.
    """

    def __init__(self, recipient, message):

        self.recipient = recipient
        self.message = message
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def formatHeader(self):
        return f"{self.timestamp} To: {self.recipient}"

    def send(self):
        header = self.formatHeader()
        print('Sending Notification:', header)

class EmailService(NotificationService):
    
    def __init__(self, recipient, message, subject):
        super().__init__(recipient, message)
        self.subject = subject
    
    def send(self):
        print(self.formatHeader())
        print(self.subject)
        print(self.message)
        print('Email sent succesfully')

class SMSService(NotificationService):
    MAX_LENGTH = 160
    def __init__(self, recipient, message, phonenumber):
        super().__init__(recipient, message)
        self.phonenumber = phonenumber
        
    
    def send(self):
        print(self.formatHeader())
        print(self.phonenumber)
        smsbody = self.message[:-3] + '...' if len(self.message) > self.MAX_LENGTH else self.message
        print(smsbody)
        print('SMS sent successfully')


emailService = EmailService('lokesh.c@gmail.com', 'Offer Details',' We are excited to offer a job to you at google')

emailService.send()

smsService = SMSService('Lokesh', 'Thank you for shopping at amazon, please find your order details at this link', 9876543210)
smsService.send()