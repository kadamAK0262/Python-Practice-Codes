class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

class Labrador(Dog):  # Labrador inherits from Dog
    def color(self):
        print("Labrador is golden")

labrador = Labrador()
labrador.speak()  # Inherits from Animal
labrador.bark()   # Inherits from Dog
labrador.color()  # Labrador-specific method
