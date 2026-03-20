# Sequence Diagram

A **sequence diagram** is a behavioral UML diagram that shows how objects interact in a particular scenario over time, focusing on the sequence of messages exchanged.

## Diagram

![Sequence Diagram](uml/sequenceDiagram.drawio)

## Key Concepts

| Element | Meaning |
|---|---|
| Lifeline (vertical dashed line) | Represents an object or actor over time |
| Activation bar | Period when an object is active / executing |
| Synchronous message (solid arrow) | Caller waits for a response |
| Asynchronous message (open arrow) | Caller does not wait |
| Return message (dashed arrow) | Response back to the caller |
| Self-call | Object calling its own method |
| Combined fragment (alt/loop/opt) | Conditional or looping logic |
