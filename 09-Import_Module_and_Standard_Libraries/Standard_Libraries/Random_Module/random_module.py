"""
Because we can't really generate truely random variables (unless you have millions of dollars to throw away to create a 
random variable generator), python generates pseudo random variables because the numbers seem random but they are actually 
reproducible. 
"""
import random # We first need to import the random module from the standard library in order to use it

def func1():
    a = random.random() # generates a random float variable from 0 to 1
    print(a)


def func2():
    a = random.uniform(1, 10) # generates a random float variable from a specific range, such as 1 to 10 (inclusive for both 1 and 10)
    print(a)


def func3():
    a = random.randint(1, 10) # generates a random integer from a specific range, such as 1 to 10 (inclusive for both 1 and 10)
    print(a)


def func4():
    a = random.randrange(1, 10) # generates a random integer from a specific range, such as 1 to 9 (is not inclusive of the upperbound number (in this case, it's 10))
    print(a)


def func5():
    # For a visual representation of the standard deviation, open "Normal Distribution deviation.jpeg"
    a = random.normalvariate(0, 1) # generates a random variable from a normal distribution with a mean of 0 and a standard deviation of 1
    print(a)


def func6():
    mylist = list("ABCDEFGH")
    a = random.choice(mylist) # random.choice will pick a random element from a list/iterable
    print(a)


def func7():
    mylist = list("ABCDEFGH")
    a = random.sample(mylist, 3) # random.sample is similiar to random.choice in that it randomly chooses variables from a list but it has a second parameter that allows it to pick multiple elements from a list (but it can't choose the same element twice)
    print(a)


def func8():
    mylist = list("ABCDEFGH")
    a = random.choices(mylist, k=3) # random.choices basically does the same thing as random.sample but it allows itself to choose the same element again
    print(a)


def func9():
    mylist = list("ACBDEFGH")
    random.shuffle(mylist) # random.shuffle shuffles a list in a randomize fashion and it doesn't require you to declared it through a variable
    print(mylist)


def func10():
    """
    Because "random" in Python is actually pseudo random and therefore reproducible, you can see this happening with the random.seed method
        If you have the same seed, you are going to get the smae output
    """
    random.seed(1)
    print(random.random())
    print(random.randint(1, 10))

    random.seed(2)
    print(random.random())
    print(random.randint(1, 10))

    random.seed(1)
    print(random.random())
    print(random.randint(1, 10))

    random.seed(2)
    print(random.random())
    print(random.randint(1, 10)) # You can see that if you have the same seed, you will get the same output


def func12():
    """
    Because "random" is reproducible, it is not recommended to be used for security purposes. Therefore, it is recommended that you use "secrets" module instead. 

    The secrets module only has three functions and they are used for things like passwords, or security tokens, or account authentication, etc.

    The disadvantage of secrets are that it takes more time for the algorithms to run but they will generate a nearly true random number.
    """
    import secrets

    a = secrets.randbelow(10) # This will generate a random integer from 0 to 9 (not inclusive of the upperbound number, which in this case is 10)
    print(a)

    a = secrets.randbits(4) # This will generate a random integer that fits into k bit value (in this case, it will generate a random integer that contains 4 bits)
    # 4 bits => 0001 = 1, 1010 = 10, 1111 = 15          (in other words, 4 bits means that you will generate a random integer from 0 to 15)
    print(a)

    mylist = list("ACBDEFGH")
    a = secrets.choice(mylist) # Chooses a random element from a list
    print(a)


def func13():
    """
    If you are working with arrays, you should use the NumPy module (you have to install numpy in order to use it because it's not included natively). 
    In order to download NumPy, you just type 'pip install numpy'
    """
    import numpy as myNumPy # 'as' allows you to refer to numpy using a different name, such as 'myNumPy'

    a = myNumPy.random.rand(3) # You can generate an array of floats using 'np.random.rand()' (the value in the parameter tells you how many elements you want in the array)
    print(a)

    a = myNumPy.random.rand(3, 3) # If you have 2 parameters, it will generate a 2 dimensional array (a 3 by 3 array in this case)
    print(a)

    # If you want to have an array with random integers, you use 'randint' instead of 'rand'
    a = myNumPy.random.randint(0, 10, 3) # the first two parameters says that you want a variable from a range of 0 to 9 (the upperbound value is not included). The third parameter is to specify how many elements you want in your array
    print(a)

    # If you want to have a multiple dimensional array, you have to use a tuple for the third parameter
    a = myNumPy.random.randint(0, 10, (5, 6))
    print(a)

    # You can shuffle arrays using NumPy as well
    arr = myNumPy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(arr)
    myNumPy.random.shuffle(arr) # Because we're shuffling a multi-dimensional array, we're only shuffling the first dimension
    print(arr)


def func14():
    """
    Even with NumPy, you will get a pseudo random number because it is reproducible
    """
    import numpy as myNumPy

    myNumPy.random.seed(1)
    print(myNumPy.random.rand(3, 3))
    myNumPy.random.seed(1)
    print(myNumPy.random.rand(3, 3))



# type the name of the function that you want to run here
func14()