from abc import ABC, abstractmethod
import threading
from collections import deque, defaultdict
from time import time
class RateLimitStrategy(ABC):

    @abstractmethod
    def allow(self, user_id):
        pass

class SlidingWindowStrategy(RateLimitStrategy):
    

    def __init__(self, limit, window):
        self.limit = limit
        self._lock = threading.Lock()
        self.window = window
        self.requests = defaultdict(deque)

    
    def allow(self, user):
        now = time()
        with self._lock:
            dq = self.requests[user]
            while dq and dq[0] <= now - self.window:
                dq.popleft()
            
            if len(dq) < self.limit:
                dq.append(now)
                return True
        
        return False

class TokenBucketStrategy(RateLimitStrategy):
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self._lock = threading.Lock()
        self.buckets = {}
    
    def allow(self, user_id):
        now = time()
        with self._lock:
            if user_id not in self.buckets:
                self.buckets[user_id] = [self.capacity, now]
            lastfill = (now - self.buckets[user_id][1])
            self.buckets[user_id] = [min(self.capacity , self.buckets[user_id][0]+(lastfill*(self.refill_rate))), now]
            if self.buckets[user_id][0] >= 1:
                self.buckets[user_id][0] -= 1
                return True
  
            return False

class RateLimitService:

    _instance = None
    _lock = threading.Lock()

    def __init__(self, strategies, default):
        self.strategies = strategies
        self.default = default
    
    @staticmethod
    def get_instance(strategies, default):
        if RateLimitService._instance is None:
            with RateLimitService._lock:
                if RateLimitService._instance  is None:
                    RateLimitService._instance = RateLimitService(strategies, default)
                

        return RateLimitService._instance
    
    def send_reqs(self,user, user_type='free'):
        strategy = self.strategies.get(user_type, self.default)
        print(strategy.allow(user), user_type, time())


if __name__ == '__main__':

    strategies = {
        'free' : SlidingWindowStrategy(3, 10),
        'premium' : SlidingWindowStrategy(10, 10),
        'burst': TokenBucketStrategy(20,1)
    }

    service = RateLimitService.get_instance(strategies=strategies, default=strategies['free'])


    for i in range(23):
        service.send_reqs('1', 'free')
        service.send_reqs('2', 'premium')
        service.send_reqs('3', 'burst')