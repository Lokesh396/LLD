import uuid
from abc import ABC, abstractmethod
from collections import defaultdict
import threading
import math
class User:

    def __init__(self, name:str, email:str):
        self.user_id = uuid.uuid4()
        self.name = name
        self.email = email
    

class Split:

    def __init__(self, user:User, amount:float):
        
        self.user = user
        self.amount = amount
    

class SplitStrategy(ABC):

    @abstractmethod
    def calaculate_splits(self,amount, participants,splits):
        pass


class EqualStrategy(SplitStrategy):

    def calaculate_splits(self, amount, participants, splits):

        share = amount / len(participants)
        return [Split(u, share) for u in participants]

class PercentSplit(SplitStrategy):

    def calaculate_splits(self, amount,  participants, splits):
        total_percent = sum(splits.values())
        if not math.isclose(total_percent, 100):
            raise ValueError('Invalid Splits')
        return [Split(u, (amount * v)/100) for u,v in splits.items()]

class ExactSplit(SplitStrategy):
    
   def calaculate_splits(self, amount,  participants, splits):
       total_amount = sum(splits.values())
       if not math.isclose(total_amount, amount):
           raise ValueError('Invalid Splits')
       return [Split(u, v) for u,v in splits.items()]
   

class Expense:

    def __init__(self, amount,paid_by,participants,splits):
        self.amount = amount
        self.paid_by = paid_by
        self.participants = participants
        self.splits = splits

class BalanceSheet:
    def __init__(self):
        self.balances = defaultdict(lambda: defaultdict(float))
        self._lock = threading.Lock()
    
    def update(self, expense):
        paid_by = expense.paid_by
        with self._lock:
            for split in expense.splits:
                if split.user == paid_by:
                    continue
                self.balances[split.user][paid_by] += split.amount
                self.balances[paid_by][split.user] -= split.amount

    def settle(self,debtor, creditor, amount):
        with self._lock:
            self.balances[creditor][debtor] += amount
            self.balances[debtor][creditor] -= amount
    
    def show_balances(self, user):
        for other, amt in self.balances[user].items():
            if amt > 0:
                print(f'{user.name} owes {other.name}: {amt}')
            elif amt < 0:
                print(f'{other.name} owes {user.name}: {amt}')
            else:
                print('settled')
class ExpenseManager:

    def __init__(self):
        self.expenses = []
        self.balance_sheet = BalanceSheet()
        self._lock = threading.Lock()
    
    def add_expense(self, amount, paid_by, split_input, participants,strategy):

        splits = strategy.calaculate_splits(amount, participants, split_input)
        expense = Expense(amount,paid_by,participants,splits)
        with self._lock:
            self.expenses.append(expense)
        
        self.balance_sheet.update(expense)
        return expense
   


