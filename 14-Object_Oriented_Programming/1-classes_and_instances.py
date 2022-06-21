"""
https://youtu.be/ZDa-Z5JzLYM

Object-Oriented Programming: Classes and Instances

What do classes do?
    They allow us to logically group data and functions to make it easier to reuse and build upon. It also allows us to create 
    objects/class instance, which are "objects" that are built using a specific class. 

    REMEMBER: data and functions that are associated with a specific class are called attributes and methods respectively 
    (data = attributes)
    (functions = methods)
"""

def func1(): # In Python, you makes classes inside of functions
    # Let's say that we want to create a class for Employees (we use this Employees class to create an Employee object)
    class Employee: # This is how you make a class in Python
        pass

    
def func2():
    class Employee:
        pass
    
    # These are Employee objects/instances of the Employee class
    employee_1 = Employee() 
    employee_2 = Employee()

    # You can see that each are Employee objects that have different locations in memory (because they're different objects)
    print(employee_1)
    print(employee_2)


def func3():
    # For each Employee object, we could manually create instance variables (attributes) for each employee
    class Employee:
        pass

    employee_1 = Employee() 
    employee_2 = Employee()

    employee_1.first_name = "Tiffany" # We just created a "first_name" attribute for employee_1
    employee_1.last_name = "Underarmor"
    employee_1.email = "TUnderarmor@email.com"
    employee_1.pay = 5000

    employee_2.first_name = "test" # We just created a "first_name" attribute for employee_1
    employee_2.last_name = "user"
    employee_2.email = "tuser@email.com"
    employee_2.pay = 1234
    employee_2.argh = "hi" # You can see that different objects don't need to have the same type/number of attributes

    print(employee_1.email) # You can get the values stored in certain attributes printed out 
    print(employee_2.argh)


def func4():
    # Automatically setting up which constructors can be set up
    # Basically constructors
    class Employee:
        def __init__(self, first_name, last_name, pay): # You should call the class instance/object "self" but you can call it anything else you can
            # Whatever gets passed in thorugh the class instance/object's parameter is being saved to that instance so that it can be referred back to later (just like any other constructor)
            self.first = first_name # the variable name that stores "first_name" doesn't have to be the same
            self.last = last_name
            self.pay = pay
            self.email = f"{self.first[0]}{last_name}@email.com" # You can either get the value saved in the instance or thought the parameter

    employee_1 = Employee("first-name", "last-name", 50000) # we don't need to pass in the class instance ("self")/object because it's passed automatically/the __init__ method is implicitly called when we create the Employee object
    employee_2 = Employee("Tiffany", "Underarmor", 12345)

    # You can see that the first_name attribute is different for the two objects
    print(employee_1.first) # "employee_1.first" == "self.first"
    print(employee_2.first)


def func5():
    # You can write functions/methods within a class to have special functionality specific to it
    class Employee:
        def __init__(self, first_name, last_name, pay): 
            self.first = first_name 
            self.last = last_name
            self.pay = pay
            self.email = f"{self.first[0]}{last_name}@email.com"
        
        # method within a class
        def fullname(self): # Every method (yes, this includes the constructor/"__init__") needs a parameter where the class instnace is passed though
            return f"{self.first} {self.last}"

        
        def findX(self): # Even a simple, dumb program that doesn't use any attribute info still needs "self" because the class instance (ex: "employee_2") passes it in regardless
            return "Found it --> X"

    
    # Outside of class
    employee_1 = Employee("first-name", "last-name", 50000) 
    employee_2 = Employee("Tiffany", "Underarmor", 12345)

    print(employee_1.fullname())
    print(employee_2.fullname()) # Because "fullname" is a method/funciton, it requires the parentheses

    print(employee_1.findX())
    print(employee_2.findX())


def func6():
    # Demonstrating why the instance of a class automastically passes the class instance when it is called/run
    class Employee:
        def __init__(self, first_name, last_name, pay): # You should call the class instance/object "self" but you can call it anything else you can
            # Whatever gets passed in thorugh the class instance/object's parameter is being saved to that instance so that it can be referred back to later (just like any other constructor)
            self.first = first_name # the variable name that stores "first_name" doesn't have to be the same
            self.last = last_name
            self.pay = pay
            self.email = f"{self.first[0]}{last_name}@email.com"

        def fullname(self):
            return f"{self.first} {self.last}"

    instance_of_the_employee_class = Employee("Mark", "Zuckerberg", 99999999999)

    print(instance_of_the_employee_class.fullname()) # This is the same as...
    print(Employee.fullname(instance_of_the_employee_class)) # This

# type the name of the function that you want to run here
func6()