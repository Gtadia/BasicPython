"""
https://youtu.be/kr0mpwqttM0

First-Class Functions:
"A programming language is said to have first-class functions if it treats functions as first-class citizens."
In other words, it allows us to treat functions like any other object.

First-Class Citizen (Programming):
"A first-class citizen (sometimes called first-class objects) in a programming language is an entity which supports all the operations generally available to other
entities. These operations typically include being passed as an argument, returned from a function, and assigned to a variable."


All this means that we should be able to treat functions just like any other object or variable.
"""

def func1():
    """
    The code below is how we are used to doing with functions
    """


    def square(x):
        return x * x


    f = square(5)

    print(square)  # This prints out the function 'square'
    print(f)  # This prints out the variable 'f'


def func2():
    """
    We can assign functions to a variable
    """
    def square(x):
        return x * x

    f = square  # Make sure you remove the parentheses because if you include the parentheses, you are telling the program that you want to execute the function, not make the variable equal to the function

    print(square)
    print(f)
    # Now we can treat the variable 'f' as a function. In other words, I can use 'f' just like how I would use 'square'
    print(square(5))
    print(f(5))


def func3():
    """
    We can pass functions as arguments and return functions as the result of other functions.
    (If a function accepts other functions as arguments or returns functions as their result, this is what you would call higher-order function)
    """
    # Passing a function as an argument to another function
    # A great example of this would be the map function (the map function takes in a function and an array/list as its arguments and it runs each value of that array/list through the provided function and then returns a new array of those results
    def my_map(func, arg_list):  # This isn't the built-in map function but we are going to use one that we create on our own.
        result = []
        for i in arg_list:
            result.append(func(i)) # This is gong to run the function 'square' with the variable i from the list of 1 to 5 and saving the returned value from function in result
        return result


    def square(x):
        return x * x

    squares = my_map(square, [1, 2, 3, 4, 5])

    print(squares)

    def cube(x):
        return x * x * x

    # Just another example using the custom map function ('my_map') with a new function passed in
    print(my_map(cube, [1, 2, 3, 4, 5]))

    # Returning a function from another function
    def logger(myMessage):

        def log_message():
            print('Log:', myMessage)

        return log_message # As you can see, we are returning a function that is inside of another function

    log_hi = logger('Hi!') # We called the function 'logger' with the parameter 'Hi!'. Once that happened, log_message was returned (log_message() did not get executed yet because nobody called it yet) back to 'log_hi = logger('Hi!')' and 'log_hi' now can behave like a function because a function was passed into it
    log_hi() # The reason why we don't pass the value "Hi!" into the parameters is because 'log_hi' remembered our initial message that we passed into it. This behavior is what we call a "closure"


def func4():
    """
    An example code to show why we would ever need to return a function in a function 

    For example, when we call 'print_h1 = html_tag('h1')', we are calling the function 'html_tag(tag):' with the string 'h1'. We are then returning the 
    function 'wrap_text(msg):' (we are not going to execute it because there are no parentheses). Now 'print_h1' will have the function 'wrap_text(msg)' 
    passed into it, meaning that it will behave like a function. And because of closure, it will remember the value 'h1' that was passed into it. 
    Now, when we call 'print_h1' like a function with the string in the parameter, it will take on the roll of 'wrap_text(msg):' and it will take in the 
    value that as passed into the parameter ('msg') and then through the formatting of the string below, will print out the message like an html line of code. 
    """
    def html_tag(tag):

        def wrap_text(msg):
            print('<{0}>{1}</{0}>'.format(tag, msg)) # the 'tag' is going to take the place of {0} and the msg (message) is going to take the place of {1}

        return wrap_text

    print_h1 = html_tag('h1')
    print_h1("Test Headline!")
    print_h1("Another Headline!")

    print_p = html_tag("p")
    print_p("Test Paragraph!")
