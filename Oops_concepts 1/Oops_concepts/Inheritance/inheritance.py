#  Inheritance is a fundamental concept in object-oriented programming (OOP) that
#  allows a new class (called a subclass or derived class) to inherit properties
#    and methods from an existing class (called a superclass or base class). 
#    This promotes code reuse and enables the creation of a hierarchy of classes.


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Subclass
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Subclass
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create instances of subclasses
dog = Dog("Luffy")
cat = Cat("Zoro")

# Call the speak method 
print(dog.speak()) 
print(cat.speak()) 


