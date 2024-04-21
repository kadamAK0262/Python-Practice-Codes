class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

class Cat(Animal):  # Cat inherits from Animal
    def purr(self):
        print("Cat purrs")

dog = Dog()
cat = Cat()
dog.speak()  # Inherits from Animal
dog.bark()   # Dog-specific method
cat.speak()  # Inherits from Animal
cat.purr()   # Cat-specific method
