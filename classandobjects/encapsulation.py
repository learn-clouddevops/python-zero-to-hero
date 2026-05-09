#

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.__age = age  # Private attribute
        self._gender = gender

    def get_age(self):
        return self.__age  # Getter method to access the private attribute

    def set_age(self, age):
        if age > 0:
            self.__age = age  # Setter method to modify the private attribute
        else:
            print("Age must be positive.")
    def getname(self):
        return self.name


class Employee(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def display_info(self):
        print(f"Name: {self.getname()}, Age: {self.get_age()}, Gender: {self._gender}")          
        

person = Person ("Alice", 30, "Female")

print(person.getname())
 # Accessing the private attribute using the getter method



emp = Employee("Bob", 25, "Male")
emp.display_info()

print(person.get_age())
 
person.age = 35  # This will not change the private attribute __age
person.set_age(40)
print(person.get_age())


emp.__age=999
print(emp.set_age(100))
print(emp.get_age())

print(emp._gender)
