# Before: Penguin extends Bird but can't fly
class Bird:
    def eat(self):
        print(f"{self.__class__.__name__} is eating")

    def fly(self):
        print(f"{self.__class__.__name__} is flying")

class Sparrow(Bird):
    pass

class Penguin(Bird):
    def fly(self):
        try:
            raise NotImplementedError("Penguins can't fly!")
        except NotImplementedError:
            print('Not Implemented')

def make_bird_fly(bird):
    bird.fly()  # Crashes for Penguin!

make_bird_fly(Sparrow())  # Works fine
make_bird_fly(Penguin())  # NotImplementedError!

# TODO: Split Bird into a Bird ABC (eat) and a FlyingBird ABC (fly).
# TODO: Sparrow implements FlyingBird, Penguin implements only Bird.


from abc import ABC, abstractmethod
class Bird(ABC):

    @abstractmethod
    def eat(self):
        pass

class FlyingBird(Bird):

    def eat(self):
        print('Eating grains and worms')

    def fly(self):
        print('Bird is flying')

class NonFlyingBird(Bird):

    def eat(self):
        print('Eating fish in the cold')

if __name__ == '__main__':

    sparrow = FlyingBird()
    sparrow.fly()
    sparrow.eat()

    penguin = NonFlyingBird()

    penguin.eat()