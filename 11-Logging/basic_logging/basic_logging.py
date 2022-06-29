"""
https://youtu.be/-ARI4Cz-awo

Basic Logging 

When you log something, you can choose between 5 standard logging levels 
(As you go from 1 to 5, the problem becomes more severe)
    1. DEBUG       Detailed information, typically of interest only when diagnosing problems.
    2. INFO        Confirmation that things are working as expected.
    3. WARNING     An indication that something unexpected happened, or indicative of some problem in the near future (e.g., "disk space low"). The software is still working as expected.
    4. ERROR       Due to a more serious problem, the software has not been able to perform some function.
    5. CRITICAL    A serious error, indicating that the program itself may be unable to continue running.



Basic Logging for small applications is okay but once your applications starts getting bigger and more complicated (especially
when we start importin our other modules), some issues can start to arise (This is because all of these modules will all try to
share the same logger).


"""

def func1():
    """
    Basic Logging Example
        Use logging to check your code in place of print statements

    * REMEMBER: The default level for logging is set to warning, meaning that by default, it will capture anything that is a warning
    or above (It will catch "WARNING", "ERROR", and "CRITICAL").

    Also, the default is to log to the console, so it acts pretty much the same as the print statement (minus the fact that it 
    has the logging level tag before the output
    EX:
    "WARNING:root:Add: 6 + 5 = 11"
    ).
    """
    import logging # You have to import logging in order to use it

    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y
    
    num_1 = 6
    num_2 = 5

    # it won't log these because their level is "DEBUG", which is lower thsn the default level of "WARNING"
    add_result = add(num_1, num_2)
    logging.debug(f"Add: {num_1} + {num_2} = {add_result}")

    subtract_result = subtract(num_1, num_2)
    logging.debug(f"Subtract: {num_1} - {num_2} = {subtract_result}")

    multiply_result = multiply(num_1, num_2)
    logging.debug(f"Multiply: {num_1} * {num_2} = {multiply_result}")

    divide_result = divide(num_1, num_2)
    logging.debug(f"Divide: {num_1} / {num_2} = {divide_result}")


    # However, if we swtich over to "WARNING" or higher, then the log outputs to the console.
    add_result = add(num_1, num_2)
    logging.warning(f"Add: {num_1} + {num_2} = {add_result}")

    subtract_result = subtract(num_1, num_2)
    logging.warning(f"Subtract: {num_1} - {num_2} = {subtract_result}")

    multiply_result = multiply(num_1, num_2)
    logging.warning(f"Multiply: {num_1} * {num_2} = {multiply_result}")

    divide_result = divide(num_1, num_2)
    logging.warning(f"Divide: {num_1} / {num_2} = {divide_result}")


def func2():
    """
    We can change the logging level so that it can log lower levels or increase the level threshold. 

        logging.DEBUG             vs           logging.debug()
        - A constant                           - a function
        - secretly an integer 
          in the background 
          (increments of 10 
          so DEBUG = 10, 
          INFO = 20, ...)
    """
    import logging

    logging.basicConfig(level=logging.DEBUG) # lowering the logging level to "DEBUG"
    # logging.basicConfig(level=10)  # This basically does the same thing
    
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y
    
    num_1 = 6
    num_2 = 5

    add_result = add(num_1, num_2)
    logging.debug(f"Add: {num_1} + {num_2} = {add_result}")

    subtract_result = subtract(num_1, num_2)
    logging.debug(f"Subtract: {num_1} - {num_2} = {subtract_result}")

    multiply_result = multiply(num_1, num_2)
    logging.debug(f"Multiply: {num_1} * {num_2} = {multiply_result}")

    divide_result = divide(num_1, num_2)
    logging.debug(f"Divide: {num_1} / {num_2} = {divide_result}")


def func3():
    """
    We can store our logs to a file instead of having them output to the console.

    When you output to a log file, it will store both the previous values and the new values
    (It won't delete anything in the log file, just append new logs to it)
    """
    import logging

    logging.basicConfig(filename="basic_log_file.log", level=logging.DEBUG) # just include "filename='file.log'" to create the file.
    
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y
    
    num_1 = 6
    num_2 = 5

    add_result = add(num_1, num_2)
    logging.debug(f"Add: {num_1} + {num_2} = {add_result}")

    subtract_result = subtract(num_1, num_2)
    logging.debug(f"Subtract: {num_1} - {num_2} = {subtract_result}")

    multiply_result = multiply(num_1, num_2)
    logging.debug(f"Multiply: {num_1} * {num_2} = {multiply_result}")

    divide_result = divide(num_1, num_2)
    logging.debug(f"Divide: {num_1} / {num_2} = {divide_result}")


def func4():
    """
    You can change the logging format to whatever format that you want it to be.

    THE DEFAULT FORMAT:
    <Level>:root:<the message>

    EX:
        DEBUG:root:Add: 5 + 7 = 12

    
    You can refer to the list of special format codes in order to change the logging format to however we want it to be.
        https://docs.python.org/3/library/logging.html#logrecord-attributes
    """
    # FOR EXAMPLE
    import logging

    logging.basicConfig(level=logging.DEBUG, filename="basic_log_file.log", format="%(asctime)s:%(levelname)s:%(message)s") # You can change the format using "format="

    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y
    
    num_1 = 6
    num_2 = 5

    add_result = add(num_1, num_2)
    logging.debug(f"Add: {num_1} + {num_2} = {add_result}")

    subtract_result = subtract(num_1, num_2)
    logging.debug(f"Subtract: {num_1} - {num_2} = {subtract_result}")

    multiply_result = multiply(num_1, num_2)
    logging.debug(f"Multiply: {num_1} * {num_2} = {multiply_result}")

    divide_result = divide(num_1, num_2)
    logging.debug(f"Divide: {num_1} / {num_2} = {divide_result}")


def func5():
    """
    A Real World Example
    """
    import logging

    logging.basicConfig(filename="basic_example.log", level=logging.INFO, 
    format="%(levelname)s —— %(message)s")

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



# type the name of the function that you want to run here
func5()