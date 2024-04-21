#  Run-Time Polymorphism (Method Overriding)

# Method overriding occurs when a subclass provides a specific implementation
# for a method that is already defined in its superclass. 
# This allows the subclass to customize the behavior of the method while
# still maintaining the same method signature.


class Animal:
    def speak(self):
        return "Generic animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animal = Animal()    # object of parent class 
dog = Dog()
cat = Cat()

# Call the speak method of each instance
print(animal.speak())    # parent class value.
print(dog.speak()) 
print(cat.speak()) 
