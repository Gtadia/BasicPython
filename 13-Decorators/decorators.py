"""
https://youtu.be/FsAPt_9Bf3U

Decorators:
A decorator is just a function that takes another function as an argument, add some kind of functionality and then returns another function. 
(All of this without altering the source code of the original function that you passed in.)
"""

def func1():
    """
    Example of first-class functions (we are using functions like a variable by returning it) and closures (we are able 
    to access the free variable even after the outer function is finished executing it) 
    """
    def outer_function(msg):
        message = msg # Free Variable (because the inner function has access to it)

        def inner_function():
            print(message) 
        # This retrun statement is an example of a first-class function
        return inner_function # By removing the parentheses, we are able to return the function without executing it (in other words, the inner_function is retruned waiting to be executed)

    hi_func = outer_function("Hi") # the inner funciton has been returned and assigned to "hi_func" but isn't run because the function was returned without the parentheses, which causes it to not execute
    bye_func = outer_function("Bye") # the same thing occurs here too

    hi_func() # Since "hi_func" is equal to "inner_function", the inner_function can be executed if you put parentheses after "hi_func"
    bye_func() # This is what a closure is (the inner function remembered the outer function's 'message' variable even after it's already been executed)


def func2():
    """
    We can access the parameter from the outer function without the use of a free variable
    """
    def outer_function(msg): # We can see that the free variable isn't there anymore but we can still access the parameters that were passed into the outer function
        def inner_function():
            print(msg)

        return inner_function

    hi_func = outer_function("Hi")
    bye_func = outer_function("Bye")

    hi_func()
    bye_func()


def func3():
    """
    Now that we are done reviewing first-class functions and closures, we are finally talk about decorators.
    """
    def decorator_function(message): # These outer and inner functions are similar to the ones up above except that the names are different to make it easier to understand decorators
        def wrapper_function():
            print(message)
        return wrapper_function

    hi_func = outer_function("Hi")
    bye_func = outer_function("Bye")

    hi_func()
    bye_func()


def func4():
    """
    So instead of printing a message that we passed in, what if we instead execute a function that we passed in? 
    This is what a decorator does.

    To do this, instead of a message, we are going to accept a function as an argument (In this example, it's "original_function").
    """
    def decorator_function(original_function): # This is a basic decorator
        def wrapper_function():
            return original_function() # You can see that instead of a message, we are actually executing and returning what the inputted function returned.
        return wrapper_function

    def display():
        print('\'Display\' function ran')

    decorated_display = decorator_function(display) # We are passing in the 'display' function into the decorator function ('decorator_function')
    decorated_display() # Because the variable 'decorated_display' is now equal to 'wrapper_function', it will just have the 'original_function', which was the function 'display' returned to it.


def func5():
    """
    Decorating our functions allows us to easily add functionality to our existing functions by adding that functionality inside of our wrapper.

    For example, 
    Without modifying our original 'display' function in any way, I can come inside of the 'wrapper' function  and add any kind of code that I want. So for example,
    I can write a print statement inside of the 'wrapper' function that says that the 'wrapper executed this before <original_function name> before the return statement.'
    This allows the 'wrapper_function' to run the print statement before returning 'original_function'.
    """
    def decorator_function(original_function):
        def wrapper_function():
            print('wrapper executed this before {}'.format(original_function.__name__))
            return original_function()
        return wrapper_function

    def display():
        print('\'Display\' function ran')

    decorated_display = decorator_function(display)
    decorated_display()


def func6():
    """
    @<decorator function> 
    is how we usually see decorators in Python

    REMEMBER:
        @decorator
        def function():
            ...
    is equivalent to: 
        function = decorator(function).             # Technically we don't need to use the function name as the variable name but it's a good convention that reduces confusion


    EX:
        @decorator_function
        def display():
    IS EXACTLY THE SAME THING AS:
        display = decorator_function(display)
    """
    def decorator_function(original_function):
        def wrapper_function():
            print('wrapper executed this before {}'.format(original_function.__name__))
            return original_function()
        return wrapper_function

    @decorator_function # This is the same as saying 'display = decorator_function(display)'
    def display():
        print('\'Display\' function ran')

    display() # Now instead of calling the variable that had the 'wrapper_function' returned to it (such as 'decoarted_display'), I can just call the function that was going to be passed into the decorator function (which in this case is 'display').


def func7():
    """
    You can decorate two or more different functions with the same decorator function (as long as they have the same number of parameters/arguments).
    """
    def decorator_function(original_function):
        def wrapper_function(yep):
            print('wrapper executed this before {}'.format(original_function.__name__))
            return original_function(yep)
        return wrapper_function

    @decorator_function
    def display(hi):
        print('\'Display\' function ran', hi)

    @decorator_function   # We can just call the second function with the same decorator function like normal
    def display2(bye):
        print("display2, the function, ran", bye)

    display("hi")
    display2("bye")


def func8():
    """
    If we have multiple functions that is getting passed into the same decorator function but take in different numbers of parameters/arguments, 
    then our decorators would throw a TypeError
    """
    def decorator_function(original_function):
        def wrapper_function():
            print('wrapper executed this before {}'.format(original_function.__name__))
            return original_function()
        return wrapper_function

    @decorator_function
    def display():
        print('\'Display\' function ran')  

    @decorator_function
    def display_info(name, age):
        print('display_info ran with arguments ({}, {})'.format(name, age))


    display_info("Jonna", 25) # Throw the following error: "TypeError: wrapper_function() takes 0 positional arguments but 2 were given"


def func9():
    """
    In order to make multiple functions that are getting passed into the same decorator function and allow each function to have differet numbers 
    of parameters/arguments, do the following... 
    """
    def decorator_function(original_function):
        # '*args' and '**kwargs' allow us to accept any arbitrary number of positional or keyword arguments for our functions.
        def wrapper_function(*args, **kwargs):
            print('wrapper executed this before {}'.format(original_function.__name__))
            return original_function(*args, **kwargs) # Since *args and **kwargs aren't being used to define a funciton but rather to call it, the "*" and "**" tells Python to unpack the tuple/dictionary 
        return wrapper_function

    @decorator_function
    def display_info(name, age):
        print('display_info ran with arguments ({}, {})'.format(name, age))

    @decorator_function
    def display(): # Because the wrapper function can take any number of arguments, it is also able to run any other functions with more, less, or no paramter values.
        print('display function ran')

    # The same decorator works for both of the functions, even though they don't have the same number of arguments
    display_info('John', 25)
    display()


def func10():
    """
    You can use classes as decorators instead of using functions as decorators. 

    In other words, we're passing in functions into a class and then have it return the same results as the wrapper function
    """
    class decorator_class(object):
        def __init__(self, original_function): # In order to get a function passed into the decorator class, we need to use an __init__ method with a parameter of 'self' and 'original_function'.
            self.my_original_function = original_function 

        def __call__(self, *args, **kwargs): # This will behave like our wrapper function and add more functionality to the function that calls this decorator class.
            print('__call__ method executed this before {}'.format(self.my_original_function.__name__))
            return self.my_original_function(*args, **kwargs) # If the functions that you are passing in as arguments don't have parameters, then you don't have to put in '*args, **kwargs' in the parameters of this return statement but if the function does have parameters and you don't have '*args, **kwargs', then you will get an error

    @decorator_class
    def display():
        print('display function ran')

    @decorator_class
    def display_info(name, age):
        print('display_info ran with arguments ({}, {})'.format(name, age))

    display()
    display_info('John', 25)


def func11():
    """
    Practical Example of decorators: (Logging)
    """
    def my_logger(orig_func):
        import logging
        logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO) # Sets up a log file that matches the name of our original function 

        def wrapper(*args, **kwargs):
            logging.info(
                'Ran with args: {}, and kwargs: {}'.format(args, kwargs)
            )
            return orig_func(*args, **kwargs)

        return wrapper

    @my_logger
    def display_info(name, age):
        print('display_info ran with arguments ({}, {})'.format(name, age))

    display_info('John', 25)
    """
    Now you can reuse the 'my_logger' decorator anytime you want to add the logging functionality to any new function that you create. 

    Now you can see how repetitive and error-prone this process would be if you wanted to add the functionality to multiple functions by manually trying to add in the 
    logging code with each individual function. 
    Thankfully, the decorator allows us to maintain our added functionality in one location and easily apply is anywhere that we want within our code base.

    In other words, the decorator function 'my_logger' helps you save time and memory by preventing you from having to type the same code again and again (by allowing you to 
    just write it once and calling it again).
    """


def func12():
    """
    Another Practical Example of decorators: (Timing how long a function takes to run)
    """
    import time as t

    def my_timer(orig_func):
        def wrapper(*args, **kwargs):
            t1 = t.time() # Takes the current time before the code runs
            result = orig_func(*args, **kwargs) # Runs the function that was passed with the arguments (that were also passed in)
            t2 = t.time() - t1 # Takes the time the function finished executing so and subtracts that it from the time the function began to get how long the function ran for.
            print('{} ran in: {} sec'.format(orig_func.__name__, t2))
            return result

        return wrapper

    @my_timer
    def display_info(name, age):
        t.sleep(1) # Pauses for 1 second before running so that the program runs long enough for us to see the time difference in our 'my_timer' decorator.
        print('display_info ran with arugments ({}, {})'.format(name, age))

    display_info("Hank ", 30)


def func13():
    """
    You can chain decorators together.

    For example, 
    What if you wanted to chain the decorators 'my_logger' and 'my_timer' together?
    This process is just as easily as stacking the decorators on top of each other. 
    However, doing this will result in weird results.
    For example, if we executed the code below:
    _____
    @my_timer 
    @my_logger
    def display_info(name, age):
        time.sleep(1)
        print('display_info ran with arugments ({}, {})'.format(name, age))

    display_info("Hank ", 30)
    _____

    We would get the following output:
    _____
    display_info ran with arguments (Hank, 30)
    wrapper ran in: 1:0053560123245345 sec          
    _____

    We don't want 'wrapper ran in: <x> sec' but rather want 'display_info' or whatever the name of the function that we passed in was. 
    (If we had '@my_logger' first and '@my_timer' second, we would get the correct output to the console but we would get a file called 'wrapper.log'. )

    To understand this problem, we need to know how calling decorators work. 
    When we put @<decorator_name> on top of the function, we are inputting that function into the decorator. 
    So, when we stack decorators, the decorator on top is inputting the decorator below it into the parameter of its own decorator.
    In other words,
    _____
    @my_logger
    def display_info(name, age)
    _____
    is the same as
    _____
    display_info = my_timer(display_info)
    _____

    So therefore
    _____
    @my_logger
    @my_timer
    def display_info(name, age)
    _____
    is the same as
    _____
    display_info = my_logger(my_timer(display_info))
    _____

    In order to see why this is an issue, take a look at the following line of code...
    -----
    display_info = my_timer(display_info)
    print(display_info.__name__)        # __name__ is a special method that returns the name of the function
    -----
    
    returns the value "wrapper" because the wrapper function was the one returned.

    Which means wrapper gets inserted into "my_logger" and uses that as the original function's name instead. 
    (The same is true for my_logger is the order was flipped)
    """
    def my_logger(orig_func):
        import logging
        logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

        def wrapper(*args, **kwargs):
            logging.info(
                'Ran with args: {}, and kwargs: {}'.format(args, kwargs)
            )
            return orig_func(*args, **kwargs)

        return wrapper


    def my_timer(orig_func):
        import time

        def wrapper(*args, **kwargs):
            t1 = time.time() # Takes the current time before the code runs
            result = orig_func(*args, **kwargs) # Runs the function that was passed with the arguments (that were also passed in)
            t2 = time.time() - t1 # Takes the time the function finished executing so and subtracts that it from the time the function began to get how long the function ran for.
            print('{} ran in: {} sec'.format(orig_func.__name__, t2))
            return result

        return wrapper

    import time

    @my_timer # See, chaining decorators are just as easy as stacking the decorator "declarers". However, doing this will result in weird results.
    @my_logger
    def display_info(name, age):
        time.sleep(1)
        print('display_info ran with arugments ({}, {})'.format(name, age))

    display_info("Hank ", 30)


def func14():
    """
    In order to fix this, we can use the 'functools' module (specifically the 'wraps' module)

    So, what we are going to do is to use a decorator inside of a decorator (all we have to do is to decorator all our wrappers with the 'wrap' decorator 
    (in short, we type '@wraps(<original function>)' on top of the wrapper functions inside of a decorator)
    """
    from functools import wraps

    def my_logger(orig_func):
        import logging
        logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

        @wraps(orig_func) # You have to put this on top of the wrapper functions
        def wrapper(*args, **kwargs):
            logging.info(
                'Ran with args: {}, and kwargs: {}'.format(args, kwargs)
            )
            return orig_func(*args, **kwargs)

        return wrapper



    def my_timer(orig_func):
        import time

        @wraps(orig_func)
        def wrapper(*args, **kwargs):
            t1 = time.time()
            result = orig_func(*args, **kwargs)
            t2 = time.time() - t1
            print('{} ran in: {} sec'.format(orig_func.__name__, t2))
            return result

        return wrapper

    import time

    @my_timer
    @my_logger
    def display_info(name, age):
        time.sleep(1)
        print('display_info ran with arugments ({}, {})'.format(name, age))

    display_info = my_timer(display_info)
    print(display_info.__name__) # Now you can see that the decorators are actually returning the original function that was passed in and not the wrapper function
    
    display_info("Tom", 22) # Now the stacked operator returns the correct function name for both my_logger and my_timer



# type the name of the function that you want to run here
func14()