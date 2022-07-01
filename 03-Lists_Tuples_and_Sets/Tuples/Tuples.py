"""
A tuple is a collection data type that is ordered, immutable, and allow duplicate elements.

The main difference between a list and a tuple is that it cannot be changed after its creation.
(You cannot edit the tuple so it can't have any other data other than the original data).
"""

def func1():
    mytuple = ("Max", 28, "Boston")
    print(mytuple)
    print(mytuple[0]) # How to access individual values in a tuple
    print(mytuple[-1]) # Last item in a tuple
    print(mytuple[-2]) # The second last item in a tuple


def func2():
    mytuple = "Max", 28, "Boston" # You can create a tuple with parentheses or without them entirely.
    print(mytuple)


def func3():
    mytuple = ("Max")
    print(type(mytuple)) # Even with the parentheses, if you have one value, it's not a tuple, but rather just a string


def func4():
    mytuple = "Max",
    print(type(mytuple)) # This is a tuple (You can have a single value tuple if you have a comma at the end)


def func5():
    mytuple = (["Max", 28, "Boston"])
    print(type(mytuple)) # This returns a list because there only one element inside of the parentheses, therefore Python thinks that it's a regular parentheses


def func6():
    # You can iterate through each index in tuple
    mytuple = ("Max", 28, "Boston")
    for x in mytuple:
        print(x)


def func7():
    # We can check if a certain value is in the tuple
    mytuple = ("Max", 28, "Boston")
    if "Max" in mytuple:
        print(True)
    else:
        print(False)


def func8():
    # We can print out the length of a tuple
    mytuple = ('a', 'b', 'c', 'd', 'e')
    print(len(mytuple))


def func9():
    # We can see how many times a certain element shows up in a tuple
    mytuple = ('a', 'p', 'p', 'l', 'e')
    print(mytuple.count('p')) # prints out 2
    print(mytuple.count('a')) # prints out 1
    print(mytuple.count('o')) # prints out 0


def func10():
    # We can also print out the index of a certain value
    mytuple = ('a', ["Hi", "Bye"], "a", 100, 5, True)
    print(mytuple.index(True))
    print(mytuple.index("a")) # It will print out the earliest instance of a variable (ex. In ("a", "a"), .index("a") will print out 0
    print(mytuple.index(["Hi", "Bye"]))
    # If you type in something that does not exist in the tuple, it will throw a ValueError/error


def func11():
    # We can easily convert a tuple to a list and vise versa
    mytuple = ('a', ["Hi", "Bye"], "a", 100, 5, True)
    mylist = list(mytuple) # tuple to a list
    print(type(mylist))
    mytuple2 = tuple(mylist) # tuple to a list
    print(type(mytuple2))


def func12():
    # We can slice a tuple
    a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    b = a[2:5] # includes indices 2, 3, and 4 (non-inclusive of 5)
    print(b)
    b = a[2:] # includes indices 2 to the very end
    print(b)
    b = a[2::2] # includes indices 2 to the end with a step (iteration) of 2
    print(b)
    b = a[::2] # includes the entire list but iterates by 2
    print(b)
    b = a[::-1] # iterates through the entire list but backwards
    print(b)
    b = a[-1:-7:-2] # iterates through indices 9 to 5 backwards with a step of -2/2 but backwards
    print(b)


def func13():
    # We can unpack a tuple (make each value in the tuple equal to individual variables)
    mytuple = "Max", 28, "Boston"
    name, age, city = mytuple # the number of variables must match the length of the tuple
    print(name)
    print(age)
    print(city)


def func14():
    # We can unpack the tuples so that the number of variables don't have to equal to the length of the tuple
    mytuple = (0, 1, 2, 3, 4)
    i1, *i2, i3 = mytuple # NOTICE that i2 has a * on it. That's makes i2 contain a list of all of the variables in the middle

    print(i1)
    print(i2)
    print(i3)


def func15():
    """
    Because tuples are immutable, working with a tuple can result in more efficient code, especially when you're
    working with large data. (it will run faster but you will not be able to edit the tuple so it depends on
    what your application for a data collection variable)
    """
    import sys
    import timeit

    # You can see that the tuples use less space than the list even though it has the same elements
    my_list = [0, 1, 2, "hello", True]
    my_tuple = (0, 1, 2, "hello", True)
    print(sys.getsizeof(my_list), "bytes")
    print(sys.getsizeof(my_tuple), "bytes")
    # You can also see that the tuples run faster than the list, even though both data collection has the same elements
    print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000)) # Creates a list 1 million times
    print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000)) # Creates a tuple 1 million times



# type the name of the function that you want to run here
func15()