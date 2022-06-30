"""
https://youtu.be/jxmzY9soFXg

Advanced Logging
Create separate logger (for the different modules so that those modules don't try to share the same logger)
Add handlers and formatters to those loggers
Log our information to multiple locations


What does "root" mean?
    Since we haven't specified a specific logger, we're working with teh root logger.
    This isn't necessarily a bad thing when working with smaller applications and specific files but it's best to get into the 
    habit of logging to specific loggers that can all be configured separately.
"""

def func1():
    """
    Example of why the "root" logger isn't the best idea.

    When we run this code, the "sample_employee_module.py" is going to run first and therefore create the "advanced_employee.log"
    but since func1 is also using the root logger, it can't create the "advanced_log_file.log" and therefore doesn't log anything 
    within func1. 

    In other words, whichever module first runs ".basicConfig" will configure the root logger with the default level, filename, and format.
    Any other modules with a basic logger will SHARE the same root logger that was set up first. 
    (REMEMBER: We can't reconfigure the root logger/we can't overwrite the initial values.)

    In other words, as long as the level is equal or higher to the root logger, the logs from other modules are going to be saved
    to the file that the root logger was configured to.
    """
    import logging
    import sample_employee_module_1 # importing the employee class that we've created (that also uses the root logger)

    logging.basicConfig(level=logging.DEBUG, filename="advanced_log_file.log", format="%(name)s:%(levelname)s:%(message)s")

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
    logging.info(f"Add: {num_1} + {num_2} = {add_result}")

    subtract_result = subtract(num_1, num_2)
    logging.info(f"Subtract: {num_1} - {num_2} = {subtract_result}")

    multiply_result = multiply(num_1, num_2)
    logging.info(f"Multiply: {num_1} * {num_2} = {multiply_result}")

    divide_result = divide(num_1, num_2)
    logging.info(f"Divide: {num_1} / {num_2} = {divide_result}")


def func2():
    """
    More Advanced Logging
        Separate loggers for each of our modules so that we can configure both of them separately. 

    REMEMBER: Instead of using "logging.<function>", you have to use the new variable name (so in this case, it's 
    "my_new_non_root_logger")
    """
    import logging
    import sample_employee_module_2 # importing the employee class that we've created (that also uses the root logger)

    my_new_non_root_logger = logging.getLogger(__name__) # We can hard code a name for the logger (so intead of root, we can make it "chicken nuggets") but by convention, we use "__name__" (__name__ gives the function that the user runs "__main__" and any modules that was imported whatever their module name is)

    logging.basicConfig(level=logging.DEBUG, filename="advanced_log_file.log", format="%(name)s:%(levelname)s:%(message)s") # However, we're still configuring the root logger. We can instead configure our specific logger ("my_new_non_root_logger") to be configured instead of configuring the root logger

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
    my_new_non_root_logger.info(f"Add: {num_1} + {num_2} = {add_result}")

    subtract_result = subtract(num_1, num_2)
    my_new_non_root_logger.info(f"Subtract: {num_1} - {num_2} = {subtract_result}")

    multiply_result = multiply(num_1, num_2)
    my_new_non_root_logger.info(f"Multiply: {num_1} * {num_2} = {multiply_result}")

    divide_result = divide(num_1, num_2)
    my_new_non_root_logger.info(f"Divide: {num_1} / {num_2} = {divide_result}")


def func3():
    """
    "logging.basicConfig(level=logging.DEBUG, filename="advanced_log_file.log", format="%(asctime)s:%(levelname)s:%(message)s")"

        We're still configuring the root logger if we use this specific line of code.
        We can instead configure our specific logger ("my_new_non_root_logger") to be configured instead of configuring the root logger. 

    REMEMBER: YOU CAN STILL USE THE ROOT LOGGER AS LONG AS ONLY ONE MODULE IS USING IT

    
    To specify the employee log file that we want to log to, we have to add a file handler.
        Format:
        "<file_handler_variable> = logging.FileHandler("<log_file_name>")"

        THEN

        <my_new_non_root_logger>.addHandler(<file_handler_variable>)

        # You can also add the formatting to ".addHandler" using "logging.Formatter()" in conjunction with "<my_new_non_root_logger>.setFormatter()"
        # REMEMBER: WE USE THE FILE_HANDLER, NOT <my_new_non_root_logger>
        file_handler.setFormatter("<format>")

        # You can also set the logging level as well
        <my_new_non_root_logger>.setLevel(<logging_level>)
    """
    import logging
    import sample_employee_module_3

    my_new_non_root_logger = logging.getLogger(__name__) 

    file_handler = logging.FileHandler("advanced_log_file.log")
    my_new_non_root_logger.addHandler(file_handler)

    file_handler.setFormatter(logging.Formatter("%(name)s:%(levelname)s:%(message)s"))
    my_new_non_root_logger.setLevel(logging.DEBUG)


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
    my_new_non_root_logger.info(f"Add: {num_1} + {num_2} = {add_result}")

    subtract_result = subtract(num_1, num_2)
    my_new_non_root_logger.info(f"Subtract: {num_1} - {num_2} = {subtract_result}")

    multiply_result = multiply(num_1, num_2)
    my_new_non_root_logger.info(f"Multiply: {num_1} * {num_2} = {multiply_result}")

    divide_result = divide(num_1, num_2)
    my_new_non_root_logger.info(f"Divide: {num_1} / {num_2} = {divide_result}")


def func4():
    """
    The thing about file_handlers is that they are modular, which means that we can log certain logs of a certain level.
    In other words, we can set levels on the file handlers themselves.

    For Example: 
        If we want to keep the logging level to DEBUG but have our log file catch logs with ERROR or above in a specific file_handler,
        then we can achieve that by doing the following: 

            "file_handler.setLevel(logging.ERROR)"

            (NOT:
            my_new_non_root_logger.setLevel(logging.ERROR)
                This sets the default log to the entire module
            )
    """
    import logging
    import sample_employee_module_3

    my_new_non_root_logger = logging.getLogger(__name__) 

    file_handler = logging.FileHandler("advanced_log_file.log")
    file_handler.setFormatter(logging.Formatter("%(name)s:%(levelname)s:%(message)s"))
    file_handler.setLevel(logging.ERROR) # The "advanced_log_file.log" will only catch logs with ERROR messages or higher

    my_new_non_root_logger.setLevel(logging.DEBUG)
    my_new_non_root_logger.addHandler(file_handler)


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


    # Because the file_handler is only catching logs with ERROR messages or higher, these INFO log messages are not caught by the file_handler
    add_result = add(num_1, num_2)
    my_new_non_root_logger.info(f"Add: {num_1} + {num_2} = {add_result}")

    subtract_result = subtract(num_1, num_2)
    my_new_non_root_logger.info(f"Subtract: {num_1} - {num_2} = {subtract_result}")

    multiply_result = multiply(num_1, num_2)
    my_new_non_root_logger.info(f"Multiply: {num_1} * {num_2} = {multiply_result}")

    divide_result = divide(num_1, num_2)
    my_new_non_root_logger.info(f"Divide: {num_1} / {num_2} = {divide_result}")

    # Since this log message is ERROR, it can be caught by the file_handler
    my_new_non_root_logger.error("This message should be caught by the file_handler, which is handling 'advanced_log_file.log'")


def func5():
    """
    We can have a traceback (the error message that shows which line caused the error) logged into our logger so that it's easier to figure out what went wrong. 
        Format:
        "<my_new_non_root_logger>.exception("<message>")"

    REMEMBER:
    ".exception()" is a special logging method that has the "ERROR" logging level.
    """
    import logging
    import sample_employee_module_3

    my_new_non_root_logger = logging.getLogger(__name__) 

    file_handler = logging.FileHandler("advanced_log_file.log")
    file_handler.setFormatter(logging.Formatter("%(name)s:%(levelname)s:%(message)s"))
    file_handler.setLevel(logging.ERROR) # The "advanced_log_file.log" will only catch logs with ERROR messages or higher

    my_new_non_root_logger.setLevel(logging.DEBUG)
    my_new_non_root_logger.addHandler(file_handler)


    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        try:
            result = x / y
        except ZeroDivisionError: 
            my_new_non_root_logger.exception("You tried to divide by zero") # Returns the error message and the callback/error message
        else:
            return result
    
    num_1 = 6
    num_2 = 0 # When we try to run the "divide()" function, we are going to run into a "ZeroDivisionError"

    # Because the file_handler is only catching logs with ERROR messages or higher, these INFO log messages are not caught by the file_handler
    add_result = add(num_1, num_2)
    my_new_non_root_logger.info(f"Add: {num_1} + {num_2} = {add_result}")

    subtract_result = subtract(num_1, num_2)
    my_new_non_root_logger.info(f"Subtract: {num_1} - {num_2} = {subtract_result}")

    multiply_result = multiply(num_1, num_2)
    my_new_non_root_logger.info(f"Multiply: {num_1} * {num_2} = {multiply_result}")

    divide_result = divide(num_1, num_2)
    my_new_non_root_logger.info(f"Divide: {num_1} / {num_2} = {divide_result}")


def func6():
    """
    Another thing about modular file handlers is that it allows to have multiple file handlers

    For Example:
        Let's say that along with the file handler logging any log messages with the "ERROR" level or higher, we also wanted to 
        see the DEBUG log messages but in the console (but it can just as easily be another log file).

    REMEMBER: 
    If we're going to log to the console, then we're going to need a STREAM HANDLER, not a file handler. 
    """
    import logging
    import sample_employee_module_3

    my_new_non_root_logger = logging.getLogger(__name__) 

    file_handler = logging.FileHandler("advanced_log_file.log")
    file_handler.setFormatter(logging.Formatter("%(name)s:%(levelname)s:%(message)s"))
    file_handler.setLevel(logging.ERROR) # The "advanced_log_file.log" will only catch logs with ERROR messages or higher

    my_new_non_root_logger.setLevel(logging.DEBUG)
    my_new_non_root_logger.addHandler(file_handler)

    # Stream Handler
    stream_handler = logging.StreamHandler() # We don't need to input anything into the parentheses (Since there can logically only be one console)
    stream_handler.setFormatter(logging.Formatter("%(name)s:%(levelname)s:%(message)s")) # The stream handler (and any additional file handlers) needs their format to be set
    stream_handler.setLevel(logging.INFO) # You can set the logging level on a stream handler
    my_new_non_root_logger.addHandler(stream_handler) # The stream handler has been added to our logger for this module.

    # Second File Handler that logs any log messages with the level INFO or higher
    file_handler_2 = logging.FileHandler("advanced_log_file_2.log")
    file_handler_2.setFormatter(logging.Formatter("%(name)s:%(levelname)s:%(message)s"))
    file_handler_2.setLevel(logging.INFO) # The "advanced_log_file.log" will only catch logs with ERROR messages or higher
    my_new_non_root_logger.addHandler(file_handler_2)



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


    # Because the file_handler is only catching logs with ERROR messages or higher, these INFO log messages are not caught by the file_handler
    add_result = add(num_1, num_2)
    my_new_non_root_logger.info(f"Add: {num_1} + {num_2} = {add_result}")

    subtract_result = subtract(num_1, num_2)
    my_new_non_root_logger.info(f"Subtract: {num_1} - {num_2} = {subtract_result}")

    multiply_result = multiply(num_1, num_2)
    my_new_non_root_logger.info(f"Multiply: {num_1} * {num_2} = {multiply_result}")

    divide_result = divide(num_1, num_2)
    my_new_non_root_logger.info(f"Divide: {num_1} / {num_2} = {divide_result}")

    # Since this log message is ERROR, it can be caught by the file_handler
    my_new_non_root_logger.error("This message should be caught by the file_handler, which is handling 'advanced_log_file.log'")


def func7():
    """
    You can get the name of the logger that the code that you're running is using (EX: __main__, advanced_logging, etc.) by using
        "logging.getLogger(__name__)"

    REMEMBER: It won't say that you're using "root" but rather just the module that the logger is being run from.
    
    It also gives us the default logging level that it's set to 
    """
    import logging

    logging.basicConfig()

    print(logging.getLogger(__name__)) # This should return <Logger  __main__ (warning)>


def func8():
    """
    """



# type the name of the function that you want to run here
func8()