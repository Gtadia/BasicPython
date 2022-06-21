"""
https://youtu.be/swU3c34d2NQ

Closures:
"A closure is  record storing a function together with an environment: a mapping associating each free variable of the function with the value or storage location to
which the name was bound when the closure was created. A closure, unlike a plain function, allows the function to access those captured variables through the
closure's reference to them, even when the function is invoked outside their scope."
"""


def func1():
    """
    When we run 'outer_func()', it will execute the function 'outer_func' (because that's what 'outer_func()' is supposed to do). The first thing the function is going to
    do is assign the variable 'message' with the value "Hi". 
    Then the function is going to run the return statement, which returns 'inner_func()' but because 'inner_func()' has the parentheses, it means that the python program 
    is supposed to execute the function 'inner_func' and therefore the function 'inner_func' will run and print out the value in 'message' (which contains the value "Hi").
    """
    def outer_func():
        message = "Hi" # free variable

        def inner_func():
            print(message) # accessing 'message' in the inner function is what is called the "free variable" because the variable is not actually defined in the inner function but we still have access to it within the outer function.

        return inner_func()

    outer_func()
    print(outer_func())


def func2():
    """
    Instead of executing the inner function and then returning it, like what the example above did, we can just return the function without executing it (which we can do by
    just taking away the parentheses).

    The code below does everything almost exactly like the code example above except that when we return 'inner_func', we are not executing it and just returning the 
    entire 'inner_func' function. So when we do 'my_func = outer_func()', we are making the variable 'my_func' take in the function 'inner_func' as the value. In this 
    'first-class' function, we are able to make 'my_func', a variable, into like a function. 
    """
    def outer_func():
        message = "Hi"

        def inner_func():
            print(message)

        return inner_func

    my_func = outer_func()
    print(my_func) # You can see that this is a function
    print(my_func.__name__) # You can print out the name of a function using '.__name__'. Also, you can see that the name of 'my_func' returns the name of the function it received ('inner_func')


def func3():
    """
    Even though we are done with the execution of the outer function, the inner function that we returned still has access to stuff inside of the outer function.

    In simple terms, a closure is an inner function that remembers and has access to variables in the local scope in which it was created (for example, the inner function was
    created inside of the the outer function, which is its local scope for it belongs inside of it), even after the outer function has finished executing. 
    """
    def outer_func():
        message = "Hi"

        def inner_func():
            print(message)

        return inner_func

    my_func = outer_func()

    my_func()
    my_func()
    my_func()
    # You can see that even after 'outer_func' is finished executing, we can still access 'inner_func' that was returned and 'inner_func' can still access the 'message' variable inside of the 'outer_func', which has finished executing.


def func4():
    """
    Things get a little interesting when we add parameters to our functions.

    For example, 
    When we run 'hi_function = outer_func('Hi'), it will run the function 'outer_func(myMessage)' and make the parameter variable 'myMessage' take the value of 'Hi'. After 
    that, the variable 'message' inside of 'outer_func' will take the value of the parameter variable 'myMessage'. After that, 'outer_func' will return 'inner_func' back to 
    'hi_function'. So 'hi_function' becomes a function (more specifically, the 'inner_func'). Now, when we call 'hi_function()', the program will remember that 'myMessage'
    equals to "Hi" (and therefore 'message' equals to "Hi"). So 'hi_function()' will return "Hi".

    One way you can remember closures is that...
    a closure CLOSES over the free variables from the environment. 
    In this case
    """
    def outer_func(myMessage):
        message = myMessage # free variable ('message' is a free variable because 'inner_func' is for the variable that has been declared in the 'outer_func' in its local scope but not declared inside of the function.

        def inner_func():
            print(message)

        return inner_func

    hi_function = outer_func('Hi')
    hello_function = outer_func('Hello')

    hi_function()
    hello_function()


def func5():
    """
    We can also have parameters inside of the inner function

    The code below is similar to the code above with only the outer function having the parameters. Basically the only difference between the two (fundamental-wise) is 
    that 'inner_func' has a parameter so when you go to run 'hi_function()', you have to enter in a value for the parameter because 'inner_func' takes in a parameter.
    """
    def outer_func(myMessage):
        message = myMessage

        def inner_func(userName):
            print(myMessage, userName)

        return inner_func

    hi_function = outer_func("Hi,")
    hi_function("Paul!")


def func6():
    """
    A complex example of closure

    youtube.com/watch?v=swU3c34d2NQ

    For example,
    when we run the code 'add_logger = logger(add)', we are calling the 'logger' function and passing in the function 'add' as a parameter. When this happens, we are 
    basically calling the outer function ('logger') that takes in a parameter 'func'.

    Then, the program will return the inner function ('log_func') instead of running the function because there are no parentheses and therefore it is informing the program
    to run execute the function. So the variable 'add_logger' now becomes the function 'log_func'.

    Then, when we run the code 'add_logger(4, 5)', we are running 'log_func' with the parameters 4 and 5. 
    The inner function, called 'log_func' takes in any number of arguments (that's what the '*' does/represent (the '*' is saying that you can pass in any number of 
    arguments to the function it is within (and in this case, the function is 'log_func')).)

    Within the inner function, we are logging that we are running the function with the arguments that were passed into the inner function/'log_func' (We are not actually
    running the function but we are printing out that we are running the function by printing out the function name. We are going to run the function in the next line of
    code 'print(func(*args))'.) In this example, the function that we passed in is 'add'.
    We are logging "Running "add" with the arguments (4, 5)" into the file 'example.log', which we had specified outside of the outer function ('logger')

    Then, we run 'print(func(*args))', which will run the function ('add') that was passed into the outer function ('logger') with the arguments (4, 5) that were passed into 
    the inner function ('log_func'). Once it finishes running the function that was passed in, it will print out what the function ('add') had returned, which is 9.
    """
    import logging
    logging.basicConfig(filename="example.log", level=logging.INFO)

    def logger(func):
        def log_func(*args): # '*args' means that the parameter will take in any number of parameters/arguments
            logging.info('Running "{}" with arguments {}'.format(func.__name__, args)) # this is the same as 'logging.info(f"Running \"{func.__name__}\" with arguments {args})'
            print(func(*args))
        return log_func

    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    add_logger = logger(add)
    sub_logger = logger(sub)

    add_logger(3, 3)
    add_logger(4, 5)

    sub_logger(10, 5)
    sub_logger(20, 10)



# type the name of the function that you want to run here
func1()