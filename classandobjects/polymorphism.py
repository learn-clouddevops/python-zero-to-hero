#

class Animal:
    def speak(self):
        return "Animal speaks"
    
class Dog(Animal):
    def speak(self):
        return  "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"        
    

#function that demonstartes polymorphism
def animal_speak(animal):
    print(animal.speak())  

cat = Cat()
dog = Dog()
print(cat.speak())
print(dog.speak())  
animal_speak(dog)  

class Shape:
    def area(self):
        return "The area of the figure"

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    

def calculate_area(shape):
    print(shape.area())

rect = Rectangle(5, 3)
circle = Circle(4)
sh = Shape()
calculate_area(rect)
calculate_area(circle)
calculate_area(sh)


#polymorphism with abstract base class

