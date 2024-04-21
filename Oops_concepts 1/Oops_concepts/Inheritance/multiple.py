class Base1:
    def method1(self):
        print("Method 1 from Base1")

class Base2:
    def method2(self):
        print("Method 2 from Base2")

class Derived(Base1, Base2):  # Derived class inherits from Base1 and Base2
    def method3(self):
        print("Method 3 from Derived")

obj = Derived()
obj.method1()  # Inherits from Base1
obj.method2()  # Inherits from Base2
obj.method3()  # Derived-specific method
