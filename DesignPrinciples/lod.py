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
