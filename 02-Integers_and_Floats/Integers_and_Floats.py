"""
Integers are whole numbers 
Floats are decimals 
"""
import math # Imported the math library built into Python

def func1(): 
    # How to initialize and declare an int (int = integers) variable and print out the value of that integer
    num = 5
    print(num)


# REMEMBER: Primitive data types are made from classes, which is why "type()" returns CLASS
def func2(): 
    # Because in Python, we don't declare a variable with its data type, we sometimes might not know if a variable is an int or a float (or any other variable)
    # So, in order to check the data type, we can use the function "type()" in order to check the data type of the variable
    num = 5
    print(type(num)) # This prints out "<class 'int'>" because we made num equal 5, which is a whole number


def func3(): 
    num = 3.14159
    print(type(num)) # This time, this prints out "<class 'float'>" because we made num equal 3.14159, which is a decimal


def func4():
    # We can do math with numbers in Python (REMEMBER: Python follows the order of operation (a.k.a, PEMDAS))
    """
    Here's the arithmetic operators in Python

    Addition:       5 + 6
    Subtraction:    5 - 6
    Multiplication: 5 * 6
    Division:       5 / 4
    Floor Division: 5 // 4
    Exponent:       5 ** 6
    Modulus:        5 % 4
    """

    # Addition
    print(5 + 6)

    # Subtraction
    print(5 - 6)

    # Multiplication
    print(5 * 6)

    # Division
    print(5 / 4) # In Python2, division with ints will drop the decimals (so in this case, 5/6=0) but in Python3, it will just leave the decimals in the output

    # Floor Division
    print(5 // 4) # "math.floor()" is a function in Python that rounds down an number/float to the nearest integer (e.g., "3/2 = 1.5" but "math.floor(3/2) = 1")
    print(math.floor(5/4)) # This is basically the same thing as "5//4"

    # Exponent
    print(5 ** 6) # The "**" actually just tells Python to multiply 5 six times.

    # Modulus
    print(5 % 4) # Prints out the remainder when we divide two numbers


def func5(): 
    # We can increment number variables
    num = 1 
    num = num + 1
    print(num)


def func6():
    # Incrementing numbers are so common that there is a shorthand way to increment numbers in Python
    num = 1
    num += 1
    print(num)

    # Subtraction, Mulitplication, Division, and the other arithmetic operators in Python also have a shorthand 
    """
    +=  ——>  +
    -=  ——>  -    
    *=  ——>  *
    /=  ——>  /    
    //=  ——>  //
    **=  ——>  **
    %=  ——>  %
    """


def func7():
    # Taking the absolute value of a number/variable is a built in function in Python 
    print(abs(-5))


def func8(): 
    # Rounding is also a built in function in Python
    print(round(5.75)) 
    print(round(5.75, 1)) # We can tell the "round()" function by how many digits after the deicmal we want it to round to


def func9():
    # We also have comparison operators that we can use with numbers, which will print out "True" or "False" (a.k.a, boolean values) based on whether or not they true or false respectively
    """
    Here's the comparison operators in Python
    Equal:              5 == 6          # Remember: "=" assigns, "==" compares
    Not Equal:          5 != 6
    Greater Than:       5 > 6
    Less Than:          5 < 6
    Greater or Equal:   5 >= 6
    Less or Equal:      5 <= 6
    """

    # For Example: 
    num_1 = 5
    num_2 = 6
    print(num_1 == num_2) # "False" because 5 does not equal 6


def func10():
    # A situation might come up with you are dealing with data, like from a text file, where they seem like numbers but are actually strings
    num_1 = '100'
    num_2 = "2022"
    print(num_1 + num_2) # Because num_1 and num_2 are strings, adding them just conatenates them together
    

def func11():
    # However, to overcome the issue mentioned in func10, we can cast the data type of variables from a string to an int
    num_1 = '100'
    num_2 = "2022"
    print(int(num_1) + int(num_2))


def func12(): 
    # Casting isn't limited to converting strings to ints
    # For example, you can cast ints to floats
    num_1 = 100
    num_2 = 2022
    print(float(num_1) + float(num_2))


# type the name of the function that you want to run here
func12()