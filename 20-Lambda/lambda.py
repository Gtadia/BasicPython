"""
https://youtu.be/D2TJ9wvSP94

Lambda
(along with)
    - map
    - filter
    - reduce


A lambda function is...
    a small (and restricted) one line anonymous function (function with no name).
    Just like a normal function, it can have multiple arguments with one expression
"""


def func1_1():
    """
    What a basic function will basically achieve using normal functions
    """
    def add10(x):
        return x+10
    
    add10(5) # returns 15


def func1_2():
    """
    func1_1 but achieving the same results using lambdas

    How to create a lambda function:
        lambda <arguments>: <expression>


        This creates a function with arguments and it evalulates the expression and returns the result.
    """
    add10 = lambda x: x+10 # The argument is "x" and the expression is "x+10"

    print(add10(5)) # returns 15


def func2():
    """
    Lambda with multiple arguments
    """
    multi_argu = lambda x, y: x * y

    print(multi_argu(5, 10)) # Returns 50 


def func3():
    """
    Lambdas with the "sorted" method
    """
    position2D = [(1, 2), (5, 15), (9, 21), (6, 87)]
    
    position2D_sorted = sorted(position2D) # The default was sorting the values based off of the first index (index 0)
    position2D_sorted_with_lambda = sorted(position2D, key=lambda x: x[1]) # The sorted value will sort based off the second value (index 1) of the tuples
    
    print(position2D)
    print(position2D_sorted)
    print(position2D_sorted_with_lambda)



# type the name of the function that you want to run here
func3()
