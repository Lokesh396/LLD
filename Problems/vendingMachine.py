from abc import ABC, abstractmethod

class VendingState(ABC):

    @abstractmethod
    def insert_coin(self, machine, amount):
        pass

    @abstractmethod
    def select_item(self, machine, code):
        pass

    @abstractmethod
    def dispense(self, machine):
        pass

class SelectState(VendingState):

    def insert_coin(self, machine, amount):
        print(f'Inserting coin amt: {amount}')
        machine.set_balance(amount)
    
    def select_item(self, machine, code):
        print(f'Item was selected')
        product = machine.inventory.get(code)
        if product is None or product[2] < 1:
            raise Exception('Item is unavailable')
        if machine.balance < product[1]:
            raise Exception('Insufficient Balance')
        machine.selected_item(code)
        machine.set_state(DispenseState())

    def dispense(self, machine):
        raise Exception('Invalid State Transisition')

class IdleState(VendingState):

    def insert_coin(self, machine, amount):
        print(f'Inserting coin amt:{amount}')
        machine.set_state(SelectState())
        machine.set_balance(amount)
    
    def select_item(self, machine, code):
        raise  Exception('Invalid State Transisition')
    
    def dispense(self, machine):
        raise  Exception('Invalid State Transisition')
        

class DispenseState(VendingState):

    def insert_coin(self, machine, amount):
        raise  Exception('Invalid State Transisition')
    
    def select_item(self, machine, code):
        raise  Exception('Invalid State Transisition')
    
    def dispense(self, machine):
        print(f'Dispensing product')
        machine._vend()
        machine.set_state(IdleState())

class VendingMachine:

    def __init__(self, inventory):
        self.inventory = inventory
        self.state = IdleState()
        self.balance = 0
        self.selected = None
    
    # --- public API: delegate every action to the current state ---
    def insert_coin(self, amount):
        self.state.insert_coin(self, amount)

    def select_item(self, code):
        self.state.select_item(self, code)

    def dispense(self):
        self.state.dispense(self)

    # --- helpers the states call ---
    def set_state(self, state):
        self.state = state

    def set_balance(self, amount):
        self.balance += amount

    def selected_item(self, code):
        self.selected = code

    # --- internal worker, called by DispenseState ---
    def _vend(self):
        product = self.inventory[self.selected]
        if self.balance < product[1] or product[2] <= 0:
            raise Exception('Amount is not sufficient or Product not available')
        self.set_balance(-product[1])
        product[2] -= 1
        print("Dispense completed")
        if self.balance > 0:
            print(f"Dispensing Change: {self.balance}")
            self.balance = 0
        self.selected = None


if __name__ == '__main__':
    products = {
        '#mixture' : ['mixture', 10, 10],
        '#coke' : ['coke', 30, 10],
        '#proteinBar' : ['ProteinBar', 10, 10],
        '#moong' : ['Moong dal', 10, 10]
    }

    machine = VendingMachine(products)

    # happy path: insert -> select -> dispense (with change)
    machine.insert_coin(50)          # idle -> select, balance 50
    machine.select_item('#coke')     # select -> dispense (coke = 30)
    machine.dispense()               # vends, returns 20 change, back to idle

    print("---")

    # illegal action: dispense straight from idle
    try:
        machine.dispense()
    except Exception as e:
        print("Rejected:", e)


    
