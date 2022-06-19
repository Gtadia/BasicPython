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
    pass

func2()