# Polymorphism is a fundamental concept in object-oriented programming (OOP) that
# allows objects of different classes to be treated as objects of a common superclass.
# It enables code to be written in a way that is more generic and flexible,
# allowing for the same method to behave differently depending on the type of object it is called on.

#  Compile-Time Polymorphism (Method Overloading)

# Method overloading refers to defining multiple methods with the
# same name but with different parameters or arguments

class Calculator:
    def add(self, x, y=4):
        return x + y

calc = Calculator()

# Call the add method with different arguments
print(calc.add(2, 3))    
print(calc.add(2))       



# Below class takes a variable-length argument list *args, 
# which allows it to accept any number of arguments. 
# Inside the method, sum(args) calculates the sum of all the arguments passed to the method.

class Calculator2:
    def add(self, *args):
        return sum(args)

calc2 = Calculator2()

# Call the add method with different arguments/ parameters
print(calc2.add(2, 3, 4))    
print(calc2.add(2, 3))        
print(calc2.add(2))           
