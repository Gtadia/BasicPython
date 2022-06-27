"""
https://youtu.be/NIWwJbo-9_8

Error Handling
    - try
    - except
    - else
    - finally

Error handling allows for code to continue running even after it throws an exception.
"""

def func1():
    """
    try and except s
    """
    try: 
        10/0 # Throws a "ZeroDivisionError: division by zero"
    except Exception: 
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



# type the name of the function that you want to run here
func8()