"""
Implements a contract relationship

This is where realization comes in. It represents a relationship between interface and the 
implementing class.

Realization is an "implements" relationship where a class fulfills a contract defined by an interface.

The relationship works like this:
 - An interface defines what must be done(the contract)
 - A class implements how its done
 - The implementing class must provide all methods declared in the interface
 - Multiple classes can realize the same interface differently.

 It is represented using dashed line with a hallow triangle pointing to the interface.

 Realization vs Inheritance

Inheritance models identity

 - The child inherits everything from the parent, including state and behavior
 - Dog is an Animal

Realization models capability
 - The implementing classes share what they are can do, not what they are. A bird and
 plane have nothing else in common.
 

"""

from abc import ABC, abstractmethod

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def get_flight_info(self):
        pass
		
class Bird(Flyable):
    def __init__(self, species, wing_span):
        self.species = species
        self.wing_span = wing_span

    def fly(self):
        print(f"{self.species} flaps its wings and takes off.")

    def get_flight_info(self):
        return f"{self.species} (wingspan: {self.wing_span}m, powered by muscle)"


class Airplane(Flyable):
    def __init__(self, model, max_altitude):
        self.model = model
        self.max_altitude = max_altitude

    def fly(self):
        print(f"{self.model} engines roar as it accelerates down the runway.")

    def get_flight_info(self):
        return f"{self.model} (max altitude: {self.max_altitude}ft, powered by jet engines)"


class Drone(Flyable):
    def __init__(self, battery_level, max_range):
        self.battery_level = battery_level
        self.max_range = max_range

    def fly(self):
        print(f"Drone propellers spin up. Battery at {self.battery_level}%.")

    def get_flight_info(self):
        return f"Drone (range: {self.max_range}km, battery: {self.battery_level}%)"
		
if __name__ == "__main__":
    flying_things = [
        Bird("Eagle", 2.3),
        Airplane("Boeing 737", 41000),
        Drone(85, 10.0),
    ]

    for flyer in flying_things:
        print(flyer.get_flight_info())
        flyer.fly()
        print()		