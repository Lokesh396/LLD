
import threading
class Counter:
    # TODO: Implement as singleton (module-level or __new__)
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.count = 0
                    cls._instance.count_lock = threading.Lock()
        return cls._instance

    def increment(self):
        with self.count_lock:
            self.count += 1

    def get_count(self):
        # TODO: Return current count
        return self.count


if __name__ == "__main__":
    # After implementing, usage should look like:
    c1 = Counter()  # or Counter()
    c2 = Counter()
    print(f"Same instance: {c1 is c2}")
    for _ in range(5):
        c1.increment()
    print(f"Count after 5 increments: {c1.get_count()}")
    pass