"""
They define what a component should do, not how it should do it.

At its core, an interface is a contract: a list of methods that any implementing class must provide.
It specifies a set of behaviors that a class agrees to implement but leaves the details of those
behaviors up to each implementation.

Benfits of Interfaces.
Services were decoupled.
service is dependent on Interfaces rather than Implementing Classes, we can add more implementing classes with out
modifying the strucure.

"""

from abc  import ABC, abstractmethod

class PaymentSerive(ABC):

    @abstractmethod
    def process_payment(self):
        pass

class phonepeProvider(PaymentSerive):
    def __init__(self, processor_name):
        self.processor_name = processor_name
    def process_payment(self):
        print(f'payment is processing through {self.processer_name}')


class razorPayProvider(PaymentSerive):
    def __init__(self, processor_name):
        self.processor_name = processor_name
    def process_payment(self):
        print('Initializing razor pay')
        print(f'payment is processing through {self.processer_name}')
        print('transcation succesfull')

class CheckOutservice():

    def __init__(self, paymentprovider):
        self.order = 'order'
        self.__paymentprovider = paymentprovider
    
    def processPayment(self):
        self.__paymentprovider.process_payment()

phonepe = phonepeProvider('phonepe')
razorpay = razorPayProvider('razorpay')

chekcout1 = CheckOutservice(phonepe)
chekcout1.processPayment()
chekcout12 = CheckOutservice(razorpay)
chekcout12.processPayment()