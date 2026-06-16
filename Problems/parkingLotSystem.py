import threading
from enum import Enum
import uuid
from collections import defaultdict
import time
from abc import ABC, abstractmethod
from typing import List

class VehicleSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Vehicle:

    def __init__(self, license_number:str, size:VehicleSize):
        self.license_number = license_number
        self.size = size
    
    def get_vehicle_size(self):
        return self.size

class ParkingSpot:

    def __init__(self, id, size:VehicleSize):
        self.id = id
        self.size = size
        self.parked_vehicle = None
        self.occupied = False
        self._lock = threading.Lock()
    
    def is_spot_occupied(self):
        return self.occupied
    
    def occupy_spot(self, vehicle):
        with self._lock:
            if not self.occupied:
                self.parked_vehicle = vehicle
                self.occupied = True
    
    def release_spot(self):
        with self._lock:
            self.parked_vehicle = None
            self.occupied = False

    def get_spot_size(self):
        return self.size
    def can_fit_vehicle(self, vehicle:Vehicle):
        if self.occupied:
            return False

        if vehicle.get_vehicle_size() == VehicleSize.SMALL:
            return self.size == VehicleSize.SMALL
        elif vehicle.get_vehicle_size() == VehicleSize.MEDIUM:
            return self.size == VehicleSize.MEDIUM or self.size == VehicleSize.LARGE
        elif vehicle.get_vehicle_size() == VehicleSize.LARGE:
            return self.size == VehicleSize.LARGE
        else:
            return False
class ParkingFloor:
    def __init__(self, floor_no):
        self.floor_no = floor_no
        self._spots:list[ParkingSpot] = []
        self._lock = threading.Lock()
    
    def add_spot(self, spot:ParkingSpot):
        self._spots.append(spot)
   
    def display_availability(self):
        print(f'--- floor No. {self.floor_no} ---')
        available_spots = defaultdict(int)
        for spot in self._spots:
            if not spot.is_spot_occupied():
                available_spots[spot.get_spot_size()] += 1
        
        for size in VehicleSize:
            print(f" {size.name} spots: {available_spots[size]}")

    def find_available_spot(self, vehicle:Vehicle):
        with self._lock:
            available_spots = []
            for spot in self._spots:
                if not spot.is_spot_occupied() and spot.can_fit_vehicle(vehicle):
                    available_spots.append(spot)
            
            if available_spots:
                available_spots.sort(key=lambda x: x.get_spot_size().value)
                return available_spots[0]
            return None
class ParkingTicket:

    def __init__(self, vehicle:Vehicle, spot:ParkingSpot, payment_strategy):
        self.ticket_no = uuid.uuid4()
        self.start_time = int(time.time() * 1000)
        self.end_time = None
        self.spot = spot
        self.vehicle = vehicle
        self.payment_strategy = payment_strategy
    
    def get_entry_time(self):
        return self.start_time
    
    def update_exit_time(self):
        self.end_time = int(time.time() * 1000)

    def get_exit_time(self) -> int:
        return self.end_time
    def get_vehicle_size(self) -> VehicleSize:
        return self.vehicle.get_vehicle_size()

    def get_parking_spot(self) -> ParkingSpot:
        return self.spot
    
    def get_payment_strategy(self):
        return self.payment_strategy

    def get_ticket_no(self):
        return self.ticket_no
    
class ParkingStrategy(ABC):

    @abstractmethod
    def find_spot(self,floors:ParkingFloor, vehicle:Vehicle):
        pass

class NearestFirstStrategy(ParkingStrategy):
    def find_spot(self, floors:List[ParkingFloor], vehicle:Vehicle):
        for floor in floors:
            spot = floor.find_available_spot(vehicle)
            if spot is not None:
                return spot
        
        return None

class FarthestFirstStrategy(ParkingStrategy):
    def find_spot(self, floors:ParkingFloor, vehicle:Vehicle):
        reversed_floors = list(reversed(floors))
        for floor in reversed_floors:
            spot = floor.find_available_spot(vehicle)
            if spot is not None:
                return spot
        
        return None

class PaymentStrategy(ABC):

    @abstractmethod
    def calculate_payment(self,parking_ticket:ParkingTicket):
        pass

class FlatFeeStrategy(PaymentStrategy):
    RATE_HOUR = 10.0
    
    def calculate_payment(self, parking_ticket:ParkingTicket):
        start_time = parking_ticket.get_entry_time()
        end_time = parking_ticket.get_exit_time()
        diff = end_time-start_time
        hours = (diff/(1000*60*60))
        return float(hours * self.RATE_HOUR)

class VehicleBasedStrategy(PaymentStrategy):
    PAY_RATES = {
        VehicleSize.LARGE : 50,
        VehicleSize.MEDIUM : 30,
        VehicleSize.SMALL : 10
    }
    
    def calculate_payment(self, parking_ticket:ParkingTicket):
        start_time = parking_ticket.get_entry_time()
        end_time = parking_ticket.get_exit_time()
        vehicle_size = parking_ticket.get_vehicle_size()
        diff = end_time-start_time
        hours = (diff/(1000*60*60))
        return float(hours * self.PAY_RATES[vehicle_size])
    
class ParkingLot:

    _instance = None
    _lock = threading.Lock()

    def __init__(self, payment_strategy:PaymentStrategy, parking_strategy:ParkingStrategy):

        self.floors = []
        self.active_tickets = dict()
        self.payment_strategy = payment_strategy
        self.parking_strategy = parking_strategy
        self._main_lock = threading.Lock()

    @staticmethod
    def get_instance(payment_strategy, parking_strategy):
        if ParkingLot._instance is None:
            with ParkingLot._lock:
                if ParkingLot._instance is None:
                    ParkingLot._instance = ParkingLot(payment_strategy,parking_strategy )
        
        return ParkingLot._instance

    def add_floor(self, floor):
        self.floors.append(floor)
    

    def park_vehicle(self, vehicle:Vehicle) -> ParkingTicket:
        with self._main_lock:
            spot = self.parking_strategy.find_spot(self.floors, vehicle)
            if spot:
                ticket = ParkingTicket(vehicle, spot, self.payment_strategy)
                self.active_tickets[vehicle] = ticket
                spot.occupy_spot(vehicle)
                return ticket
            return None
    
    def unpark_vehicle(self, vehicle:Vehicle)->float:
        with self._main_lock:
            ticket = self.active_tickets.pop(vehicle, None)
            if ticket is None:
                return 'unknown vehicle'
            ticket.update_exit_time()
            ticket.get_parking_spot().release_spot()
            return ticket.get_payment_strategy().calculate_payment(ticket)