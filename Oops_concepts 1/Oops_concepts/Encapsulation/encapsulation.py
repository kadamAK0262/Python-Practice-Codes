
# Encapsulation allows you to restrict access to certain components of objects, 
# typically the attributes and methods, and prevent direct modification from outside the class. 
# Encapsulation helps in achieving data hiding and abstraction, making the code easier to manage
# and less prone to errors.


class Car:
    def __init__(self, make, model, year):
        self._make = make                   # Protected attribute
        self.__model = model                # Private attribute       access Modifiers.
        self.year = year                    # Public attribute

    def get_make(self):                     # Getter 
        return self._make
    
    def set_make(self, make):               # Setter
        self._make = make

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def display_info(self):
        print(f"Make: {self._make}, Model: {self.__model}, Year: {self.year}")

car = Car("Toyota", "Camry", 2022)

# Accessing public attributes directly
print("Year:", car.year)

# Accessing protected attributes indirectly using getter method
print("Make:", car.get_make()) 

print("Model:", car.get_model())  

# Modifying protected attribute using setter method
car.set_make("Honda")

car.set_model("Corolla")

# Displaying car information
car.display_info()  
