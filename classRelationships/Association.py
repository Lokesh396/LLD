
"""
Association: Assocatiation represents a relationship when an object needs
 to know about the exisistence of other object to perform its responsibilities.

A doctor has patients
A driver has car
A student enroll in courses

If A class must communicate with another class B to fullfill its purpose,
then class A is associated with class B.

In an association
Both classes can existly independently
Their lifecycle doesn't depend on each other.

Association reflects a has-a or uses-a relationship.

It is indicated  with a straightline --------, and error is used for direction ->
No error indicated bidirectional.

The levels of association
1 to 1
o to 1
1 to *
*
"""


class CheckoutService:

    def __init__(self, payment_gateway):
        self._payment_gateway = payment_gateway

    def pay(self):
        self._payment_gateway.pay()


class PaymentService:

    def __init__(self, name):
        self._name = name
    
    def pay(self):
        print('I am procesing payment')


# here the relationship between checkout service to payment service 1 to 0, 
# checkout service references the payment service where as the payment
# service doesn't need to know about the existence of checkoutservice


class Profle:

    def __init__(self):
        self.user = None

    def set_user(self, user):
        self.user = user

class User:

    def __init__(self):
        self.profile =  None
    
    def set_profile(self, profile):

        self.profile = profile
        profile.set_user(self)


# for a many to one relationship think of a project and issues, 
# every issue is assocaited with one project, but one project 
# may have multiple issues.


# for a many to many relationship think of whatsapp groups 
# where each user can be in many groups and each group 
# can have many users.



# Hospital Appointment System


class Room:

    def __init__(self, roomno):
        self.roomno = roomno



class Doctor:

    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.appointments = []
    
    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def get_patients(self):
        seen = set()
        result = []
        for appointment in self.appointments:
            if id(appointment.patient) not in seen:
                seen.add(id(appointment.patient))
                result.append(appointment.patient)
        return result

class Patient:

    def __init__(self, name):
        self.name = name
        self.appointments = []
    
    def book_appointment(self, appointment):
        self.appointments.append(appointment)

    def get_doctors(self):
        seen = set()
        result = []
        for appointment in self.appointments:
            if id(appointment.doctor) not in seen:
                seen.add(id(appointment.doctor))
                result.append(appointment.doctor)
        return result

class Appointment:

    def __init__(self,  doctor:Doctor, patient:Patient,room,time:str,):
        self.room = room
        self.doctor = doctor
        self.patient = patient
        self.time = time
        doctor.add_appointment(self)
        patient.book_appointment(self)


dr_smith = Doctor("Dr. Smith", "Cardiology")
dr_patel = Doctor("Dr. Patel", "Neurology")

alice = Patient("Alice")
bob = Patient("Bob")

room_101 = Room("101")
room_205 = Room("205")

Appointment(dr_smith, alice, room_101, "9:00 AM")
Appointment(dr_smith, bob, room_101, "10:00 AM")
Appointment(dr_patel, alice, room_205, "2:00 PM")

print(f"{dr_smith.name}'s patients:")
for p in dr_smith.get_patients():
    print(f"  - {p.name}")

print(f"{alice.name}'s doctors:")
for d in alice.get_doctors():
    print(f"  - {d.name} ({d.specialization})")

print(f"{dr_smith.name}'s schedule:")
for a in dr_smith.appointments:
    print(f"  - {a.time} with {a.patient.name} in Room {a.room.roomno}")
