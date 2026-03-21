# State Diagram

A **state diagram** (also called a state machine diagram) is a behavioral UML diagram that models the different states an object can be in during its lifecycle and the transitions triggered by events.

## Diagram

![State Diagram](uml/stateDiagram.drawio)

## Key Concepts

| Element | Meaning |
|---|---|
| Initial pseudostate (filled circle) | Starting point of the state machine |
| State (rounded rectangle) | A condition or situation of an object |
| Transition (arrow) | Change from one state to another triggered by an event |
| Guard condition `[condition]` | A boolean condition that must be true for the transition to fire |
| Action `/action` | Behavior executed during a transition |
| Final state (circle + filled circle) | End of the state machine |
| Composite state | A state that contains nested sub-states |

## Example: Order Lifecycle

```
Placed → [payment confirmed] → Confirmed → [items packed] → Shipped → [delivered] → Delivered
                                                                                    ↓
                                                                              [return requested] → Returned
```

## When to Use

- Modeling an object with a well-defined lifecycle (orders, tickets, sessions)
- Showing how external events drive state changes
- Documenting protocol behavior (TCP connections, UI component states)
