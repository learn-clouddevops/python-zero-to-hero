#parent class

class Car:
    def __init__(self,windows,doors,enginetype):
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype

    def drive(self):
        print("The car is driving")



car1= Car(4,5,"petrol")
print(car1.drive())      




class Tesla(Car):
    def __init__(self,windows,doors,enginetype,is_selfdriving):
        super().__init__(windows,doors,enginetype)
        self.is_selfdriving = is_selfdriving

    def selfdriving(self):
        print(f"Tesla supports self driving: {self.is_selfdriving}")


tesla1= Tesla(4,4,"electric",True)
print(tesla1.selfdriving())        


### multiple inheritance


class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")    


class Pet:
    def __init__(self,owner):
        self.owner = owner

    def info(self):
        print(f"This pet belongs to {self.owner}")    


class Dog(Animal,Pet):
    def __init__(self,name,owner):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)

    def speak(self):
       return f"{self.name} says Woof!"


#create an object

dog1= Dog("Buddy","Alice")
print(dog1.speak())
print(f"dog owner is {dog1.owner}")
        
