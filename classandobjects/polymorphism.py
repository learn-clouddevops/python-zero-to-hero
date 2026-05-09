#polymorphysn from ABC

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def startengine(self):
        pass

class  Car(Vehicle):
   

    def startengine(self):
        print("Car engine started")

class Bike(Vehicle):
    

    def startengine(self):
        print("Bike engine started")



car = Car()
motorcycle = Bike()
car.startengine()
motorcycle.startengine()
