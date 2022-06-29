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


def func3_1():
    """
    The regular function version of what was achieved in func3_2

    Instead of sorting by the 2nd index, we can also sort by the sum of the tuples, the difference of the log of the tuples, etc.
    """
    position2D = [(1, 2), (5, 15), (9, 21), (6, 87)]

    def sort_by_index_1(x):
        return x[1]

    position2D_sorted_with_function = sorted(position2D, key=sort_by_index_1)

    print(position2D)
    print(position2D_sorted_with_function)


def func3_2():
    """
    Lambdas with the "sorted" method
    """
    position2D = [(1, 2), (5, 15), (9, 21), (6, 87)]
    
    position2D_sorted = sorted(position2D) # The default was sorting the values based off of the first index (index 0)
    position2D_sorted_with_lambda = sorted(position2D, key=lambda x: x[1]) # The sorted value will sort based off the second value (index 1) of the tuples
    
    print(position2D)
    print(position2D_sorted)
    print(position2D_sorted_with_lambda)


def func4():
    """
    MAP
        The map function transfrom each element in a list by running each element through the func and storing that new value/the return value of the func
        in a new list/iterator.

    map + lambda basically achieves the same thing as the list comprehension

    map(func, seq)
        - func = function (lambda or regular function)
        - seq = sequence (any iterators, such as lists)
    """
    a = [1, 2, 3, 4, 5]
    b = map(lambda x: x*2, a) # multiplies every element by 2

    print(b) # returns as map object "<map object at ...>"
    print(list(b)) # In order to see the result, we can convert the map object to a list first


def func5():
    """
    FILTER
        The filter function will only store values when the func returns True. 

    filter + lambda is basically the same thing as a list comprehension with a conditional

    filter(func, seq)
        - func = function (lambda or regular function)
        - seq = sequence (any iterators, such as lists)
    """
    a = [1, 2, 3, 4, 5]
    b = filter(lambda x: x%2==0, a) # only stores even numbers

    print(b) # returns as filter object
    print(list(b)) # returns as a list 


def func6():
    """
    REDUCE
        The reduce function repeatedly applies the functionn to the elements and returns a single value.

    For Example:
    a = [1024, 16, 8, 4, 2]
    b = reduce(lambda x, y: x/y, a)
    
    RESULTS IN...
    1024/16 = 64
    64/8 = 8
    8/4 = 2
    2/2 = 1

    b = 1

    reduce(func, seq)
        - func = function (with 2 arguments)
        - seq = sequence (any iterators, such as lists)
    """
    from functools import reduce # You have to import "reduce" from the functools standard library in order to use it
    a = [1, 2, 3, 4, 5]
    product_of_a = reduce(lambda x,y: x*y, a)
    print(product_of_a)


# type the name of the function that you want to run here
func6()
