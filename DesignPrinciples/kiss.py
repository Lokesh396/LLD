"""
Keep it simple and stupid.

The idea was simple, the systems works well when we keep it simple.

In software kiss means writing code that is
 - Easy to read
 - Easy to understand
 - Easy to change

The Complexity Cycle
it starts innoncently, when a class is bit hard to understand, so a bug slips in. The
bug gets patced with a workaround instead of proper fix, the work around adss more 
complexity, now the class is even harder to understand.

Why Complexity is Dangerous
1. Harder to Read
2. More places for Bugs to Hide
3. Slower Onboarding
4. Poor Debuggability

Signs you are violating kiss

 - You added an interface before you need a second implemntation
 - you used reflection for something a simple method could handle
 - your methods have five optional parametes and deeply nested conditions
 - you used recursion where a simple loop can achieve that.
 - a new developer cannot understand your class wihtout reading three other classes
 first.
 - your code has more boilerplate than business logic.

How to Apply the kiss principle

1. Write code for humans
2. Avoid premature abstraction
3. Favor composition over-inheritance
4. keep functions short
5. use familiar data structures

When not to simplify

 - Dont oversimplify critical systems
 - Avoid duplicating logic just to keep things simple
 - Know your audience
"""

# Before Kiss

from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def calculate(self, a: float, b: float) -> float:
        pass

class Addition(Operation):
    def calculate(self, a: float, b: float) -> float:
        return a + b

class Subtraction(Operation):
    def calculate(self, a: float, b: float) -> float:
        return a - b

class Multiplication(Operation):
    def calculate(self, a: float, b: float) -> float:
        return a * b

class Division(Operation):
    def calculate(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

class Calculator:
    def execute(self, op: Operation, a: float, b: float) -> float:
        return op.calculate(a, b)
    


# After kiss

class Calculator:
    def calculate(self, operator, a, b):
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            if b == 0:
                raise ValueError("Division by zero")
            return a / b
        else:
            raise NotImplementedError(f"Unknown operator: {operator}")