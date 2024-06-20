from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def maxSpeed(self):
        pass

    @abstractmethod
    def __init__(self,name):
        pass


class Tesla(Car):

    def maxSpeed(self):
        return 300
    def __init__(self,name):
        self.name = name
        print(f"{self.name}")

class Audi(Car):
    def maxSpeed(self):
        return 360
    def __init__(self,name):
        self.name = name
        print(f"{self.name}")


class Mercedes(Car):
    def maxSpeed(self):
        return 340
    def __init__(self,name):
        self.name = name
        print(f"{self.name}")
        pass

myNewCar = Tesla("Model X")
myNewCar.maxSpeed()
