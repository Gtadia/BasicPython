"""
https://youtu.be/NIWwJbo-9_8

Error Handling
    - try
    - except
    - else
    - finally

Error handling allows for code to continue running even after it throws an exception.

There are many different types of errors and they are...
    Syntax Errors - Errors created when you typed something incorrectly (but does not apply to variable names)

    Exception Errors - Errors created when the code is executed, even if it is syntactically correct

    Type Errors - Errors created when you try to combine two different types of data, or declaring a different type of data than what the variable wants, or when you use a
    different data type than the one a function/class/parameters/(etc) need.

    Import Errors - Errors that are created when you try to import modules that does not exist (This is called a "ModuleNotFoundError")

    Name Error - Errors created when you call a variable name that has not been declared yet (this includes variables names that you misspelled, which is why misspelled names
    don't throw syntax errors)

    FileNotFoundError - Errors created when you try to open a file that does not exist

    Value Error - Errors created when you want to modify things like a list but you modify (remove or look for) elements that does not exist
    (ex: list = [1, 2, 3]
    list.remove(4) # Four does not exist and therefore throw an error)

    Index Error - Errors created when you want to modify things like a list but you modify (remove or look for) indices that does not exist.
    (EX: list = [1, 2, 3]
    list[4] # an index of 4 does not exist (an index of 3+ does not exist)
    )

    Key Error - Errors that arises when you try to access a key from a dictionary but the key does not exist.
    (EX: my_dict = {"name": "Max"}
    my_dict["age"] # This will throw an error because the key "age" does not exist in "my_dict")
"""

def func1():
    """
    try and except
    """
    try: 
        10/0 # Throws a "ZeroDivisionError: division by zero"
    except Exception: # In order for the except block to work, we technically don't need "Expcetion" (We can run the except block like this "except:")
        pass
        # Because of this except , the error caused by the code in the try  doesn't further get executed and instead runs the expcet 


def func2():
    """
    You can have the except  catch certain errors
    """
    try:
        10/0
        # stuff = a_variable_that_does_not_exist        # This throws a "NameError" but since we're only catching "ZeroDivisionError", this will break the code and have the error thrown
    except ZeroDivisionError:
        print("You've try to divide by 0. Sorry but we still haven't figured out how that works yet.")
    

def func3():
    """
    You can handle multiple exceptions

    Remember, the exceptions are handled from top to bottom.
    Therefore, if you put "expcet Expcetion" on the top, then every error would handled by that exception  instead of
    the other more specific exceptions (such as "except NameError").
    """
    try: 
        10/0
        stuff = a_variable_that_does_not_exist
    except ZeroDivisionError: 
        print("You've try to divide by 0. Sorry but we still haven't figured out how that works yet.")
    except NameError:
        print("You've try to use a variable that does not exist.")
    except Exception:
        print("Some sort or error occured but we're not sure what it is...")


def func4():
    """
    You can have the exception return what the error is
    """
    try: 
        10/0
        stuff = a_variable_that_does_not_exist
    except ZeroDivisionError as e: 
        print(e) # returns the following message: "division by zero"
    except NameError as e:
        print(e) # returns the following message: "name 'a_variable_that_does_not_exist' is not defined"
    except Exception as e:
        print(e)


def func5():
    """
    else clause
        Runs its code if the try clause doesn't raise an exception

    Sure we can just put the entire code in the try  instead of splitting it up between the try and else s but if we do
    split it up between the try and else s, it allows us to know exactly what we're trying to catch.
    """
    try:
        stuff = 10/1 # doesn't throw any errors
    except Exception as e:
        print(e)
    else:
        print(stuff) # Stuff declared in the try  can be accessed by the except, else and finally  (I don't know if the try  can access anything from the other s (in theory but it doesn't matter anyways because the try  is always the first to be run and the other s are always the last thing to run)


def func6part1():
    """
    finally clause
        Runs its code no matter what happens (whether or not there's an exception)

    One use case of the finally block is to release certain resources regradless of what happened.
    """
    try:
        stuff = 10/1 # doesn't throw any errors
    except Exception as e:
        print(e)
    else:
        print(stuff)
    finally:
        print("The Finally Clause")
    # The finally clause is basically the same thing as writing code outside of the error handling code.


def func6part2():
    """
    Has the same basic functionality of the finally clause
    """
    try:
        stuff = 10/1 # doesn't throw any errors
    except Exception as e:
        print(e)
    else:
        print(stuff)
    # Basically the finally clause 
    print("Essentially The Finally Clause")


def func7():
    """
    We can manually raise an exception.
    """
    try: 
        food = "Sandwich"
        if food == "Sandwich": # Manually raising exceptions doesn't have to down inside of an error handling clause!!!
            raise Exception
    except Exception as e:
        print(e) # When you raise an error manually, nothing is returned by default so "e" is equal to None


def func8():
    """
    We can manually raise an exception with an error message.
    """
    try: 
        food = "Sandwich"
        if food == "Sandwich": 
            raise Exception("This is an error message")
    except Exception as e:
        print(e)


def func9():
    """
    We can add an assertion error when something specific happens (A quick error that is thrown when it receives the boolean 
    value "True" in the parameter) but still add a custom message.

    An assertion error technically not a custom error because the errors above are "more customized" errors.

    In other words, "assert()" will throw an AssertionError if the conditional inputted as an argument to the assert method 
    is False. Otherwise, no error messages will be thrown. 
        The comma after "assert()" is the error message that it throws.
    """
    x = -5
    try: # A "try, except" statement is here to make sure that the other code gets run
        assert(x>=0), "x is not positive" # "x is not positive" is the error message if the conditional in the argument returns False (which is does)
    except Exception as e:
        print("error message:", e)


def func10():
    """
    We can define our own TRUE custom exceptions by creating our own exception classes by sub classing from the base exception class. 
    """
    class ValueTooHighError(Exception): # You can declare a class in the middle of the program
        def __init_(self, message, value):
            self.message = message
            self.value = value

    class ValueTooSmallError(Exception):
        def __init__(self, message, value):
            self.message = message
            self.value = value # The variable name after "self." doesn't have to be the name of the parameter value it is going to save

    class JustARandomError(Exception):
        pass

    def test_value(x):
        if x > 100:
            raise ValueTooHighError("Value is too high", x)
        if x < 5:
            raise ValueTooSmallError("value is too small", x) # the first parameter value is going to be saved as "message" and the second parameter value is going to be saved as "value" by the "__init__()" function but it will be remembered as "things" by the class itself
        if x == 6:
            raise JustARandomError()
    try:
        test_value(6)
    except ValueTooHighError as e:
        print(e.message, e.value)
    except ValueTooSmallError as e:
        print(e.message, e.value)
    except JustARandomError:
        print("Truely a random value, ey.")


# type the name of the function that you want to run here
func10()