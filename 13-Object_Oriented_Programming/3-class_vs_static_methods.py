"""
https://youtu.be/rq8cL2XMM5M

Static Methods vs Class Methods (vs Regular Methods)


Regular Methods: Automatically take the class instance (by convention, this parameter is called "self") as the first argument  
Class Methods: A method with "@classmethod" decorator right above it

"""

def func1():
    class Employee:
        raise_amount = 1.04

        def __init__(self, first_name, last_name, pay):
            self.first = first_name 
            self.last = last_name
            self.pay = pay
            self.email = f"{self.first[0]}{last_name}@email.com"

        """Regular Method"""
        def apply_raise(self):
            self.pay = int(self.pay * self.raise_amount)
        
        """Class Method"""
        @classmethod # With the classmethod, we're working with the class isntead of the class instance 
        def set_raise_amount(cls, amount): # Since "class" is a keyword and therefore canoot be used as a variable/parameter varible, we're going to use "cls" instead
            cls.raise_amount = amount 

        """Static Method"""
        @staticmethod # This static method has a logical connection to the Employee class but it doesn't actually depend on any specific instance variable or class variable
        def is_workday(day): # We don't any arguments because staticmethods don't automatically get an argument passed in. Therefore, we can just pass in the parameters that we want
            return day.weekday() == 5 or day.weekday() == 6 # If you don't need to access any instance variables or class variables, then the method should be a static method


    
    emp_1 = Employee("Wall", "E", 50000)
    emp_2 = Employee("Carbon", "Dioxide", 2303044)

    
def func2():
    # Running the classmethod 
    class Employee:
        raise_amount = 1.04

        def __init__(self, first_name, last_name, pay):
            self.first = first_name 
            self.last = last_name
            self.pay = pay
            self.email = f"{self.first[0]}{last_name}@email.com"

        """Regular Method"""
        def apply_raise(self):
            self.pay = int(self.pay * self.raise_amount)
        
        """Class Method"""
        @classmethod 
        def set_raise_amount(cls, amount):
            cls.raise_amount = amount 

    
    emp_1 = Employee("Wall", "E", 50000)
    emp_2 = Employee("Carbon", "Dioxide", 2303044)

    Employee.set_raise_amount(1.05)
    """
    In other words, the classmethod is doing the same thing as...

        Employee.raise_amount = 1.05
    """

    # Returns the same new value of 1.05
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)

    """
    Also, the classmethod can be run with the class instances and it will still affects class variable/will run like it ran through the class
    """
    emp_1.set_raise_amount(1.05)

    # Returns the same new value of 1.05
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)


def func3(): 
    # You don't need any instance variables to run class methods (but you can still change the class variable)
    class Employee:
        raise_amount = 1.04

        def __init__(self, first_name, last_name, pay):
            self.first = first_name 
            self.last = last_name
            self.pay = pay
            self.email = f"{self.first[0]}{last_name}@email.com"

        """Regular Method"""
        def apply_raise(self):
            self.pay = int(self.pay * self.raise_amount)
        
        """Class Method"""
        @classmethod 
        def set_raise_amount(cls, amount):
            cls.raise_amount = amount 


    # As you can see, you don't need instance variables to run class methods
    Employee.set_raise_amount(1.05)
    print(Employee.raise_amount)


def func4part1():
    # Sometimes, you might want to parse a string and pass those values into a constructor
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


    emp_string_1 = "Wall, E, 50000"
    emp_string_2 = "Carbon, Dioxide, 2303044"

    first, last, pay = emp_string_1.split(", ") # You can split a string into separate variables
    emp_1 = Employee(first, last, pay)

    first, last, pay = emp_string_2.split(", ")
    emp_2 = Employee(first, last, pay)


def func4part2():
    # If parsing a string a common way people pass in attributes in thorugh the constructor, we can just create a new method that allows us to pass in the string and pass in the attributes
    class Employee:
        payrate_increase = 1.04

        def __init__(self, first_name, last_name, pay):
            self.first = first_name 
            self.last = last_name
            self.pay = pay
            self.email = f"{self.first[0]}{last_name}@email.com"

        def raise_ammount(self):
            self.pay = int(self.pay * Employee.payrate_increase)

        @classmethod # We are going to use a class method to create the altnerative constructor that passes in the attributes through a string
        def constructor_from_string(cls, emp_str):
            first, last, pay = emp_str.split(", ") # This line is going to split the string up into its separate attribute 
            return cls(first, last, pay) # This line is going to create a new employee instance and return it so that whatever called this method will be the object with these exact values

    
    emp_string_1 = "Wall, E, 50000"
    emp_string_2 = "Carbon, Dioxide, 2303044"

    new_emp_1 = Employee.constructor_from_string(emp_string_1) # Calling a classmethod will automatically pass in the class as one of the parameter
    new_emp_2 = Employee.constructor_from_string(emp_string_2)


def func5():
    # One might think that class methods and static methods are no different from each other. However, there is one big difference that sets them apart.
    """
    Regular methods automatically pass in the class instance/"self" as the first argument
    Class methods automatically pass in the class/"cls" as the first argument
    Static methods don't pass in anything automatically (They're just like regular functions except we include them in our classes because they have some logically connections with the class)
    """
    class Employee:
        payrate_increase = 1.04

        def __init__(self, first_name, last_name, pay):
            self.first = first_name 
            self.last = last_name
            self.pay = pay
            self.email = f"{self.first[0]}{last_name}@email.com"

        @staticmethod 
        def is_workday(day): # .weekday() is from the datetime library
            return not (day.weekday() == 5 or day.weekday() == 6) # 5 is Saturday and 6 is Sunday


    import datetime
    example_date = datetime.date(2022, 6, 19)
    print(Employee.is_workday(example_date)) # As you can see, we don't need any class instances for the function to run


func5()