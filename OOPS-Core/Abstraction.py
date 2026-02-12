from abc import ABC, abstractmethod
"""
Abstraction is the process of hiding complex internal implementation details and exposing only the relevant, high-level functionality to the outside world. It allows developers to focus on what an object does, rather than how it does it.
"""
class Vehicle(ABC):

    def __init__(self, model,engine):
        self.model = model
        self.engine = engine

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    
    def start(self):
        print("Car is started")
class Tractor(Vehicle):
    
    def start(self):
        print("Tractor is starting")

tractor = Tractor('massey fergusion', '241')
car = Car('Tata nexon', 'revtron 1.2')