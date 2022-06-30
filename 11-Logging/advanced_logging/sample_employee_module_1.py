"""
The real world example code from "basic_logging.py"

For func1 on "advanced_logging.py"
"""


import logging

logging.basicConfig(filename="advanced_example.log", level=logging.INFO, 
format="%(levelname)s:%(name)s —— %(message)s")

class Employee:
    # A sample Employee class
    def __init__(self, first, last): 
        self.first = first
        self.last = last

        logging.info(f"Created Employee: {self.fullname} - {self.email}")

    @property
    def email(self): 
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Han", "Solo")
emp_3 = Employee("Albert", "Einstein")