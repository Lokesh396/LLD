"""
Have you ever called a method on object.. then chained another.. and another.. until
the line looked like a trail of dots ?.
or made a small internal change in one class, and suddeny you had to update code
across five other layers ?.

It is a voilation of design principle 'Law of delimeter' 

Voilation

price = customer.get_shopping_cart().get_items()[0].get_product().get_price()

If any thing changes in any of the classes like cusomter, shopping cart or the 
way the return the price, the main order service which has nothing to do with order
processing.

This is called train-wreck or dot-chaining
"""

def display_first_item_price(customer):
    price = (customer.get_shopping_cart()
                     .get_items()[0]
                     .get_product()
                     .get_price())
    print("Price of the first item:", price.get_amount())

# Whats wrong in this

"""
1. High coupling
2. Encapsulation Voilation
3. Maintaince nightmare
4. Testablity Issues
"""


# 3. Enter: The Law of Demeter(LoD)

# only talk to your immediate friends - Law of delimeter
"""
It is also known as principal of least knowledge

The rule is straight forward. A method M on a object o should only call method on

1. Itself( the object O)
2. its own fields (objects that O holds as instance variables)
3. Its method parameters (objects passed into M)
4. objects its creates (objects instantiated within M)


"""

# Refactoring with LOD in mind

# step 1 Adding method to shopping cart
class ShoppingCart:
    def __init__(self):
        self._items = []

    # ... other methods ...

    def get_first_item_price(self):
        if not self._items:
            return 0
        return self._items[0].get_product().get_price()

#  step 2 Add a method to the customer

class Customer:
    def __init__(self, shopping_cart):
        self._shopping_cart = shopping_cart

    # ... other methods ...

    def get_first_cart_item_price(self):
        return self._shopping_cart.get_first_item_price()

# step 3 update the order service
def display_first_item_price(customer: Customer):
    price = customer.get_first_cart_item_price()
    print("Price of the first item:", price.get_amount())


# order service only talks to customer, customer only talks to shopping car 
# shoping card to cartitem


"""
5. Benefits of Law of Delimeter

Low Coupling
Better Encapsulation
Easier Refactoring
Improved Testability
Cleaner APIs

6. when it is ok to voilate law of delimeter

stable, Low-Level Libraries
DTOs / Value obects
Fluent APIs / Builders
"""

# Notification Service

class NotificationService:
    def send_ride_update(self, ride):
        # Train wreck 1: reaching through Driver -> Profile to get name
        driver_name = (ride.get_driver()
                           .get_profile()
                           .get_full_name())

        # Train wreck 2: reaching through Driver -> Vehicle -> Registration
        plate = (ride.get_driver()
                     .get_vehicle()
                     .get_registration()
                     .get_license_plate())

        # Train wreck 3: reaching through Passenger -> ContactInfo
        phone = (ride.get_passenger()
                     .get_contact_info()
                     .get_phone_number())

        message = f"Your driver {driver_name} is arriving in a {plate}. Contact: {phone}"
        print(f"SMS to {phone}: {message}")


class Ride:
    def __init__(self, driver, passenger):
        self._driver = driver
        self._passenger = passenger

    # ... other methods ...

    def get_driver_name(self):
        return self._driver.get_profile().get_full_name()

    def get_vehicle_plate(self):
        return self._driver.get_vehicle().get_registration().get_license_plate()

    def get_passenger_phone(self):
        return self._passenger.get_contact_info().get_phone_number()

class NotificationService:
    def send_ride_update(self, ride):
        driver_name = ride.get_driver_name()
        plate = ride.get_vehicle_plate()
        phone = ride.get_passenger_phone()

        message = f"Your driver {driver_name} is arriving in a {plate}. Contact: {phone}"
        print(f"SMS to {phone}: {message}")