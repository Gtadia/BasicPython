"""
https://youtu.be/3ohzBxoFHAY

Spcial Methods: (also known as magic methods)
*** Magic methods are always surrounded by double underscores called dunder (EX: __init__)*** 
    These special methods allow us to emulate some built-in behavior within Python.
    It's also how we implement operator overloading 
"""

def func1():
    # Example of what special methods will allow us to do
    class Employee:
        payrate_increase = 1.04

        def __init__(self, first_name, last_name, pay):
            self.first = first_name 
            self.last = last_name
            self.pay = pay
            self.email = f"{self.first[0]}{last_name}@email.com"

        def fullname(self):
            return f"{self.first} {self.last}"

        def raise_ammount(self):
            self.pay = int(self.pay * Employee.payrate_increase)

    
    emp_1 = Employee("Wall", "E", 50000)
    emp_2 = Employee("Carbon", "Dioxide", 2303044)

    print(emp_1) # Cureently, if we just print out a class instance, we get a vague info that it's an employee object (For example: "<__main__.func1.<locals>.Employee object at 0x10c918d90>")
    # With special methods, we can change this behavior to return something more useful

    print(1 + 2) # This does arithemtic operations (1 + 2 = 3)
    print("a" + "b") # This concatenates ("a" + "b" = "ab")


def func2():
    """
    Some common special methods

    def __repr__(self):
        pass
    # This special method is called anytime we run "repr(<object>)"
    # __repr__ is supposed to be an unambiguous (In other words, just a string) representation of the object and should be used for debugging, logging, etc.
    # It's really meant to be seen by other developers

    def __str__(self):
        pass
    # This special method is called anytime we run "str(<object>)"
    # __str__ is meant to be more of a readable representation of an object 
    # Is meant to be used as a display to the end-user


    In other words, they are functionally the same but by convention, they are used for different purposes
    """
    class Employee:
        payrate_increase = 1.04

        def __init__(self, first_name, last_name, pay):
            self.first = first_name 
            self.last = last_name
            self.pay = pay
            self.email = f"{self.first[0]}{last_name}@email.com"

        def fullname(self):
            return f"{self.first} {self.last}"

        def raise_ammount(self):
            self.pay = int(self.pay * Employee.payrate_increase)

        # A special method
        def __repr__(self):
            return f"Employee({self.first}, {self.last}, {self.pay})" # Basically a string representation of what the object declaration would look like

        # Another special method
        def __str__(self): # This is meant to be more readable to the end user (so no returning a string representation of the object)
            return f"{self.fullname()} - {self.email}" 

        
    emp_1 = Employee("Wall", "E", 50000)
    emp_2 = Employee("Carbon", "Dioxide", 2303044)


    print(emp_1) 
    print(repr(emp_1)) # This returns "Employee(Wall, E, 50000)""
    print(str(emp_1)) # This returns "Wall E - WE@email.com"

    # When we use "repr(emp_1)" and "str(emp_1)", these special functions are actually calling the following lines of code
    print(emp_1.__repr__())
    print(emp_1.__str__())


def func3():
    # There are also special methods for arithemtic
    print(1 + 2) # What this is doing in the basground is running a special method called "__add__" in the background
    print(int.__add__(1, 2)) # In other words, Python is basically doing this
    
    print("a" + "b") # Strings are also using "__add__" as well
    print(str.__add__("a", "b"))


def func4():
    # We can modify the "__add__" method so that it does what we want it to d0
    class Employee:
        payrate_increase = 1.04

        def __init__(self, first_name, last_name, pay):
            self.first = first_name 
            self.last = last_name
            self.pay = pay
            self.email = f"{self.first[0]}{last_name}@email.com"

        def fullname(self):
            return f"{self.first} {self.last}"

        def __add__(self, other): # self is going to be the first object that you add (because that's going to get callled first) and other is the second object that is going to be called
            # In other words, "emp_1 + emp_2" = "Employee.__add__(emp_1, emp_2)"
            return self.pay + other.pay

    
    emp_1 = Employee("Wall", "E", 50000)
    emp_2 = Employee("Carbon", "Dioxide", 50000)

    print(emp_1 + emp_2) # You can see that this added up the salaries together
    print(Employee.__add__(emp_1, emp_2)) # This is what is running in the background


    print(1 + 2) # As long as the arithmetic happens for objects in the Employee class, "__add__()" won't be affected 


def func5():
    # If you read through the documentation, you can see that there are special methods for not just addition but also for subtraction, multiplication, modulus, and statements, or statements, etc. 
    """
    
    """


def func6():
    # "len()" is also a special method running in the background
    print(len("test"))
    print("test".__len__()) # This is what is essentially running in the background
    # So if we wanted to create a "__len__" method for other objects other than strings, you can (if you add a custom "__len__" method in the class of that object/class instance)

    """For Example"""
    class Employee:
        payrate_increase = 1.04

        def __init__(self, first_name, last_name, pay):
            self.first = first_name 
            self.last = last_name
            self.pay = pay
            self.email = f"{self.first[0]}{last_name}@email.com"

        def fullname(self):
            return f"{self.first} {self.last}"

        def __len__(self):
            return len(self.fullname()) # Of course "__len__" really only works with strings but we can modify it so that we only have to pass in the class itself and not have to type extra stuff

    
    emp_1 = Employee("Wall", "E", 50000)
    emp_2 = Employee("Carbon", "Dioxide", 2303044)

    print(len(emp_1)) # returns 6


func6()