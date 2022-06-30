"""
The real world example code from "basic_logging.py"

For func3, func4, func5, and func6 on "advanced_logging.py"
"""
import logging

new_logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("advanced_employee.log")
new_logger.addHandler(file_handler)
file_handler.setFormatter(logging.Formatter("%(levelname)s:%(name)s —— %(message)s"))
new_logger.setLevel(20)


class Employee:
    # A sample Employee class
    def __init__(self, first, last): 
        self.first = first
        self.last = last

        new_logger.info(f"Created Employee: {self.fullname} - {self.email}")

    @property
    def email(self): 
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Han", "Solo")
emp_3 = Employee("Albert", "Einstein")