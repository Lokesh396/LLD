'''
In software engineerig we often required classes that can only have one object.

Singleton is a creational design pattern that guarantees a class has only one instance
and provide a global access to it.

Two requirements:
1. single instance
2. global access

Singleton is useful in scenarios like
- managing shared resources
- co ordinating system wide actions
- managing state

To implement singleton pattern, we must prevent external objects from creating instances
of the singleton class. only the singleton class should be permitted to create its own
objects.


'''

class Singeton:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    

import threading

class SingletonSafe:

    _instance = None
    _lock = threading.Lock()


    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        
        return cls._instance
    

class singletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwds)
        
        return cls._instances[cls]


class SingletonMetasafe(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
    
class singleton(metaclss = singletonMeta):
    pass