"""
The separation of concerns (SoC) is one of the most fundamental principles
 in software development.

It is so crucial that 2 out of 5 SOLID principles (Single Responsibility 
and Interface Segregation) are direct derivations from this concept.

The principle is simple: don't write your program as one solid block, 
instead, break up the code into chunks that are finalized tiny pieces of 
the system each able to complete a simple distinct job

The application of the Separation of Concerns involves two processes: reduction of 
coupling and increasing cohesion.

A quick way to remember which attribute should be increased or decreased:

Decoupling is good - so we need to aim for a loose coupling
Cohesive code is good - we need to aim for a high cohesion

Benefits of Loose Coupling and High Cohesion

- Better code clarity
- Better Reusability (DRY)
- Better testability

"""

# Bad code
import sqlite3

def get_user_total_price(user_id):
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT price FROM orders WHERE user_id=?", (user_id,))
    rows = cursor.fetchall()

    total = 0
    for row in rows:
        total += row[0]

    print("Total price:", total)

# Good code
import sqlite3

def fetch_orders(user_id):
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()
    cursor.execute("SELECT price FROM orders WHERE user_id=?", (user_id,))
    return cursor.fetchall()

def calculate_total(orders):
    return sum(price for (price,) in orders)

def display_total(total):
    print("Total price:", total)


orders = fetch_orders(1)
total = calculate_total(orders)
display_total(total)