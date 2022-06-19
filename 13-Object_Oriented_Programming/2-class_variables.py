"""
https://youtu.be/BJ-VvGyQxho

Class Variables
    Class variables are variables that are shared among all instance of a class (Like static methods and variables in Java).

    In other words, instance variables are specific to the class instance it belongs to (like the employee's name, email, and pay)
    but class variables are the same for every class instance (like the employee's company, or date of the payday, or the annual payrate increase) 
"""

def func1():
    # Class Variables
    payrate_increase = 1.04 # This is how you create a class variable

    class Employee:
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
                how can we
            """


    
    emp_1 = Employee("Wall", "E", 50000)
    emp_2 = Employee("Carbon", "Dioxide", 2303044)
