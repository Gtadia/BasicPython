"""
https://youtu.be/RSl87lqOXDE

Inheritance
    Inheritance allows us to inherit attributes and methods from a parent class/allows us to write sub-classes.
    In other words, when a sub-class inherits from its parents class, Python will first search for attributes and methods in the subclass first and then in the parent class. 
"""

def func1():
    class Employee:
        raise_amt = 1.04

        def __init__(self, first, last, pay):
            self.employee_first = first
            self.employee_last = last
            self.email = first + "_" + last + "@gmail.com"
            self.employee_pay = pay

        def fullname(self):
            return f"{self.employee_first} {self.employee_last}"

        def apply_raise(self):
            self.employee_pay = int(self.employee_pay + self.raise_amt)


    class Developer(Employee): # You can add parentheses at the end of the class in order to state that you want THIS class ('Developer') to inherit from the 'Employee' class
        pass # We're going to add a 'pass' here to show that by just simply inheriting a class will give this class all the functionality of the 'Developer' class (It will inherit all the attributes and methods of the parent class)


    dev_1 = Employee('Monkey', 'Bananas', 50000)
    dev_2 = Employee('Test', 'Employee', 60000)

    print(dev_1.email)
    print(dev_2.email)

    dev_1 = Developer('Bill', 'Fence', 50000)
    dev_2 = Developer('Bucky', 'Gates', 60000)

    # The Method Resolution order shows the places that Python searches for attributes and methods. (In this example, when we created our two new 'Developers', it first looked at the developer class for the __init__ method. When it didn't find it there, then it went up to the Employee class and that's where it was executed. Now, if it hadn't found it in our 'Employee' class, the last place it would have looked would have been the object class and every class in Python inherists from this base object.)
    print(help(Developer)) # The 'help' function tells us all kinds of good information about the function we've just passed in, such as the parameters it takes in, the method resolution order, the methods inherited from Employee, data descriptors inherited from Employee, etc.

    print(dev_1.email)
    print(dev_2.email) # You can see that even though there is nothing inside the 'Developer' class, it does the same thing as the 'Employee' class because it was inherited.
    # In other words, when we instantiated our 'Developer' class, it looked for an __init__ method that can take three parameters. When it didn't find it, it walked up the chain of inheritance until it finds what it is looking for (This chain is called the METHOD RESOLUTION order), which is the __init__ method that takes in three parameters in the parent class.


def func2():
    """
    What would happen when we wanted to customize our subclass a little bit (instead of making it completely empty)?

    The thing to take away is that by adding/changing things inside of the subclass ('Developer') didn't have an impact on the original class that the 
    subclass inherited from/parent class.
    """
    class Employee:
        raise_amt = 1.04

        def __init__(self, first, last, pay):
            self.employee_first = first
            self.employee_last = last
            self.email = first + "_" + last + "@gmail.com"
            self.employee_pay = pay

        def fullname(self):
            return f"{self.employee_first} {self.employee_last}"

        def apply_raise(self):
            self.employee_pay = int(self.employee_pay * self.raise_amt)


    class Developer(Employee):
        raise_amt = 1.10

    dev_1 = Employee('Monkey', 'Bananas', 50000)
    dev_2 = Employee('Test', 'Employee', 50000)

    # The thing to take away is that by adding/changing things inside of the subclass ('Developer') didn't have an impact on the parent class.
    print(dev_1.employee_pay)
    dev_1.apply_raise()
    print(dev_1.employee_pay) # You can see that that the program used the 'Developer' 'raise_amt' and not the 'raise-amt' in the 'Employee' class

    print(dev_2.employee_pay) 
    dev_2.apply_raise()
    print(dev_2.employee_pay) # However, because the "raise_amt = 1.10" was applied in the Developer class, which the Employee class (the parent class) does not have acecss to, the new raise_amt value isn't seen by the .employee_pay method from the Employee class. 
    # In other words, any changes made to the subclasses don't affect the parent class


def func3():
    """
    Sometimes, we want to initiate our subclasses with more information than our parent class can handle. 
    For example,
    Let's say that when we created our developers ('dev_1' and 'dev_2'), we also wanted to pass in their main programming language as an attribute, but currently our 'Employee'
    class can only accept first name, last name, and pay. So if we also wanted to pass in a programming language, we are going to have to give the 'Developer' class/subclass 
    its own __init__ method. 
    """
    class Employee:
        raise_amt = 1.04 # raise_amt = raise amount

        def __init__(self, first, last, pay):
            self.employee_first = first
            self.employee_last = last
            self.email = first + "_" + last + "@gmail.com"
            self.employee_pay = pay

        def fullname(self):
            return f"{self.employee_first} {self.employee_last}"

        def apply_raise(self):
            self.employee_pay = int(self.employee_pay * self.raise_amt)


    class Developer(Employee):
        raise_amt = 1.1


        def __init__(self, first, last, pay, programming_lang):
            super().__init__(first, last, pay) # super().__init__() is going to pass 'first', 'last', and 'pay' to the 'Employee' class's __init__ method for it to handle.
            # Employee.__init__(self, first, last, pay) # This also works but 'super()' makes the code more maintainable when using multiple inheritance
            self.prog_lang = programming_lang
        """
        You might be tempted to copy all of the code from the 'Employee' class's __init__ method and paste it into the 'Developer' class's __init__ method. 
        The reason why we don't want to do that is because we want to keep our code "dry" and not have our code repeat code/logic in multiple places because we want it
        to be as maintainable as possible. 
        So instead of copy and pasting, we are going to just let our 'Employee' class's __init__ method handle the first name, last name, and pay and then we will let the 
        'Developer' class handle the programming language. 
        """


    dev_1 = Employee('Monkey', 'Bananas', 50000, "Python")

    print(dev_1.email)
    print(dev_1.prog_lang) # You can see that "Python" is returned


def func4():
    """
    Just another example of having constructors/__init__ methods inside of the subclasses
    """
    class Employee:
        raise_amt = 1.04

        def __init__(self, first, last, pay):
            self.employee_first = first
            self.employee_last = last
            self.email = first + "_" + last + "@gmail.com"
            self.employee_pay = pay

        def fullname(self):
            return f"{self.employee_first} {self.employee_last}"

        def apply_raise(self):
            self.employee_pay = int(self.employee_pay * self.raise_amt)


    class Developer(Employee):
        raise_amt = 1.1

        def __init__(self, first, last, pay, programming_lang):
            super().__init__(first, last, pay)
            self.prog_lang = programming_lang


    class Manager(Employee):
        def __init__(self, first, last, pay, employees=None): # We're setting the default argument for "employees" to None. This is because you never want to pass mutable data types (ex: list & dictionaries), even empty ones, as default arguments
            super().__init__(first, last, pay) # 'super()' is referring back to the parent class, which in this case is 'Employee'
            if employees is None: # If 'employees' is empty, then make 'self.employees' equal to an empty list.
                self.employees_list = [] # The reason why we did just pass in an empty list as the default argument instead of 'None' is because you don't want to have any mutable data types, such as a list or a dictionary, as default arguments.
            else:
                self.employees_list = employees

        def add_employee(self, employee):
            if employee not in self.employees_list:
                self.employees_list.append(employee)

        def remove_employee(self, employee):
            if employee in self.employees_list:
                self.employees_list.remove(employee)

        def print_employees(self):
            for employee in self.employees_list:
                print('-->', employee.fullname()) # 'e.fullname()' is going to try to find the function 'fullname' within the 'Manager' class but since it cannot find it, it will go search for it in the parent class 'Employee'


    dev_1 = Employee('Monkey', 'Bananas', 50000, "Python")
    dev_2 = Developer('Test', 'Employee', 60000, 'Java')

    manager_1 = Manager('Sue', 'Smith', 90000, [dev_1]) # the "employees" argument is a list, you can pass in more than one "dev" (EX: you could have passed in a list with both dev_1 and dev_2)

    print(manager_1.email) # You can see that everything inherited from the 'Employee' class works
    manager_1.print_employees()
    manager_1.add_employee(dev_2) # dev_2 added
    manager_1.print_employees() 
    manager_1.remove_employee(dev_1) # dev_1 removed
    manager_1.print_employees() # You can see that the stuff we included inside of the 'Manager' class is working fine


def func5():
    """
    'isinstance' and 'issubclass' are two built-in functions in Pythons that are useful when working with inheritance.

    isinstance(<object/class instance name>, <class name>)
    This will tell us if an object is an instance of a class.

    issubclass(<sub class name>, <parent class name>)
    This will tell us if a class is a subclass of another.
    """
    class Employee:
        raise_amt = 1.04

        def __init__(self, first, last, pay):
            self.employee_first = first
            self.employee_last = last
            self.email = first + "_" + last + "@gmail.com"
            self.employee_pay = pay

        def fullname(self):
            return f"{self.employee_first} {self.employee_last}"

        def apply_raise(self):
            self.employee_pay = int(self.employee_pay * self.raise_amt)


    class Developer(Employee):
        raise_amt = 1.1

        def __init__(self, first, last, pay, programming_lang):
            super().__init__(first, last, pay)
            self.prog_lang = programming_lang


    class Manager(Employee):

        def __init__(self, first, last, pay, employees=None):
            super().__init__(first, last, pay)
            if employees is None:
                self.employees_list = []
            else:
                self.employees_list = employees

        def add_employee(self, employee):
            if employee not in self.employees_list:
                self.employees_list.append(employee)

        def remove_employee(self, employee):
            if employee in self.employees_list:
                self.employees_list.remove(employee)

        def print_employees(self):
            for e in self.employees_list:
                print('-->', e.fullname())


    dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
    dev_2 = Developer('Test', 'Employee', 60000, 'Java')

    manager_1 = Manager('Sue', 'Smith', 90000, [dev_1])

    print(isinstance(manager_1, Manager)) # 'manager_1' is an instance of the class 'Manager' because has called that class
    print(isinstance(manager_1, Employee)) # 'manager_1' is an instance of the class 'Employee' because it is the parent class of 'Manager'.
    print(isinstance(manager_1, Developer)) # 'manager_1' is NOT an instance of the class 'Developer' since is neither called nor a parent class of 'Manager'

    print(issubclass(Developer, Employee)) # This is true since 'Developer' is a subclass of 'Employee'
    print(issubclass(Manager, Employee)) # This is also true since 'Manager' is a subclass of 'Employee'
    print(issubclass(Manager, Developer)) # This is false since 'Developer' and 'Manager' are not subclasses of one another (they are both just subclasses of 'Employee')
    print(issubclass(Employee, Manager)) # This is also false since 'Employee' is not a subclass of 'Manager' (it is the other way around/'Manager' is the subclass of 'Employee')`



# type the name of the function that you want to run here
func5()