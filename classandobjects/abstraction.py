from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    def drive(self):
        print("Driving the vehicle...")


class Car(Vehicle):
    def start_engine(self):
        print("Starting the car engine...")



def operate_vehicle(vehicle):
    vehicle.start_engine()



car = Car()
operate_vehicle(car)
