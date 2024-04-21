class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal(Animal):  # Mammal inherits from Animal
    def milk(self):
        print("Mammal produces milk")

class Dog(Mammal):  # Dog inherits from Mammal
    def bark(self):
        print("Dog barks")

class Bat(Mammal):  # Bat inherits from Mammal
    def fly(self):
        print("Bat flies")

class Whale(Mammal):  # Whale inherits from Mammal
    def swim(self):
        print("Whale swims")

class Bird(Animal):  # Bird inherits from Animal
    def fly(self):
        print("Bird flies")

class Parrot(Bird):  # Parrot inherits from Bird
    def talk(self):
        print("Parrot talks")

class Penguin(Bird):  # Penguin inherits from Bird
    def swim(self):
        print("Penguin swims")

dog = Dog()
bat = Bat()
whale = Whale()
parrot = Parrot()
penguin = Penguin()

dog.speak()    # Inherits from Animal
dog.bark()     # Inherits from Dog
dog.milk()     # Inherits from Mammal
bat.speak()    # Inherits from Animal
bat.milk()     # Inherits from Mammal
bat.fly()      # Inherits from Bat
whale.speak()  # Inherits from Animal
whale.milk()   # Inherits from Mammal
whale.swim()   # Whale-specific method
parrot.speak() # Inherits from Animal
parrot.fly()   # Inherits from Bird
parrot.talk()  # Parrot-specific method
penguin.speak()# Inherits from Animal
penguin.fly()  # Inherits from Bird
penguin.swim() # Penguin-specific method
