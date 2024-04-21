class Person:
    # Constructor in python
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating object of Person class
person1 = Person("Alice", 30)

print("Name:", person1.name)
print("Age:", person1.age)

# Calling method
person1.intro()

# for delete the object
# del person1
