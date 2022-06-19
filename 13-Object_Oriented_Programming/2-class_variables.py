"""
https://youtu.be/BJ-VvGyQxho

Class Variables
    Class variables are variables that are shared among all instance of a class (Like static methods and variables in Java).

    In other words, instance variables are specific to the class instance it belongs to (like the employee's name, email, and pay)
    but class variables are the same for every class instance (like the employee's company, or date of the payday, or the annual payrate increase) 
"""

def func1():
    # Class Variables
    class Employee:
        payrate_increase = 1.04 # This is how you create a class variable

        def __init__(self, first_name, last_name, pay):
            self.first = first_name 
            self.last = last_name
            self.pay = pay
            self.email = f"{self.first[0]}{last_name}@email.com"

        def fullname(self):
            return f"{self.first} {self.last}"

        def raise_ammount(self):
            # self.pay = int(self.pay * payrate_increase) # However, if you want to use the class variable, I can't simply just use the variable as is or else a "name" error is thrown
            self.pay = int(self.pay * Employee.payrate_increase) # I can access the class variable using "<class name>.<class variable>"
            """
            Or I can use...
                self.payrate_increase as well

            However, this raises the question...
                how can we access them from the class instance?
                (The answer to this question is in func2)
            """
    
    emp_1 = Employee("Wall", "E", 50000)
    emp_2 = Employee("Carbon", "Dioxide", 2303044)


def func2():
    # Accessing class variables from the class itself or from the instance of the class 
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


    # You can see that all of them print out the same value 
    # This works because when we try to access an attribute on an instance, it will first check if that instance contains that attribute. Once it can't find the attribute in the instance variables, it will then check for the attribute in the class variables within its class or any class that it inherits from.
    print(Employee.payrate_increase)
    print(emp_1.payrate_increase)
    print(emp_2.payrate_increase)


def func3(): 
    # We can check to see if an attribute exists within the instance variables and/or within the class
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

    
    print(Employee.__dict__) # Returns all of the attributes and the values associate with it located in the class (along with some other attributes that we don't really care about)
    print(emp_1.__dict__) # Returns all of the attributes  and the values associated with them located in emp_1, the instance of the Employee class


def func4():
    # If you change the value of the class variable within the class, it changes the value of the class variable for everything (both the class and the instance classes)
    # However, if you change the value of the class variable within an instance of the class, it only changes the value for THAT INSTANCE ONLY
    """The reason for this is that when you try to change the class variable through an instance of the class, it actually creates an attribute with the same name as the class variable and when this attribute is called, Python finds this pseudo class variable first because it first searches the instance variables before the class"""

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
            self.pay = int(self.pay * Employee.payrate_increase) # Because changing the class variable changes differently based on whether or not you changed the variable through the class or thorugh the class instance (In other words, using "<class name/Employee>.payrate_increase" will not be the same as "self.payrate_increase" if you change the class variable thorugh a class instance)

    
    emp_1 = Employee("Wall", "E", 50000)
    emp_2 = Employee("Carbon", "Dioxide", 2303044)


    Employee.payrate_increase = 1.05 # Changed the class variable throuhg the class
    # Both the class and the class instances returns the same value ("1.05")
    print(Employee.payrate_increase)
    print(emp_1.payrate_increase) 
    print(emp_2.payrate_increase)


    emp_1.payrate_increase = 1.05
    # Only emp_1 returns the new value (CHECK THE EXPLANATION IN TRIPLE QUOTES IN FUNC4 (this function))
    print(Employee.payrate_increase)
    print(emp_1.payrate_increase) 
    print(emp_2.payrate_increase)
    # After reading the TRIPLE QUOTE explanation, the following print statement should make a lot of sense
    print(emp_1.__dict__)


def func5():
    # EXAMPLE CODE: Incrementing the number of total employees everytime a new Employee object is created
    class Employee:
        num_of_employees = 0

        def __init__(self, first_name, last_name, pay):
            self.first = first_name 
            self.last = last_name
            self.pay = pay
            self.email = f"{self.first[0]}{last_name}@email.com"

            Employee.num_of_employees += 1 # Since the constructor/__init__ function runs everytime a new object/class instance is created, the incrementor should go here (also, it wouldn't really make much since to use self because it would increment the total employee count for a single instance (in other words, every new employee created will have 1 employee each))

        def fullname(self):
            return f"{self.first} {self.last}"


    print(Employee.num_of_employees) # returnes 0
    
    emp_1 = Employee("Wall", "E", 50000)
    emp_2 = Employee("Carbon", "Dioxide", 2303044)

    print(Employee.num_of_employees) # returns 2


# type the name of the function that you want to run here\
func5()

