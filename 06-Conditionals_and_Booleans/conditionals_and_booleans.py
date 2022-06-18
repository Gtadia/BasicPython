"""
https://youtu.be/DZwmZ8Usvnk

Conditional and Booleans:
- If
- Else
- If Else (elif)
"""

def func1(): 
    # If statement
    if True:
        print("Conditional was True")

    if False:
        print("Conditional was True")


def func2():
    # Comparison conditions
    """
    Equal:              ==      # Remember: "=" assigns, "==" compares
    Not Equal:          !=
    Greater Than:       >
    Less Than:          <
    Greater or Equal:   >=
    Less or Equal:      <=
    Object Identity     is      # The difference between Object Identity and == is that Object Identity actually checks if values have the same ID/basically checking whether the two variables are teh same object in memory
    """
    # For Example:
    language = "Python"
    if language == "Python":
        print("The language is Python")
    

def func3():
    # If and else statements
    language = "Python 2.0"
    if language == "Python":
        print("The language is Python")
    else:
        print("Visible Confusion")


def func4():
    # If, if else (elif), and else statements
    language = "Python"
    if language == "Python":
        print("The language is Python")
    elif language == "Java": # If the language is not Python but is actually Java, then this elif statement will execute
        print("The language is Java")
    else: # If language is neither Python or Java, then the else statement will execute
        print("BTW I use arch")


def func5():
    # Not only can we use comparison conditionals, we can also use boolean operations 
    """
    and         x and y         Returns true if both x and y are true
    or          x or y          Returns true if either x or y is true
    not         not x           Returns true if x is false (and vise versa)
    """
    # For example
    air = "polluted"
    is_earth_flat = False
    
    # and
    if air == 'polluted' and is_earth_flat:
        print("yes")
    
    # or
    if air == 'polluted' or is_earth_flat:
        print("si")

    # not
    if not is_earth_flat:
        print("네")


def func6():
    # Example code on Object Identity from the Comparison Conditionals
    test_1 = [1, 2, 3]
    test_2 = [1, 2, 3]
    print(test_1 == test_2) # This prints out to true because the data/values stored inside of test_1 and test_2 are the same
    print(test_1 is test_2) # However, since test_1 and test_2 are stored in two different locations in memory, they are therefore two different objects and therefore NOT the same object (even though they store the same data)
    


def func7():
    # In order to show that test_1 and test_2 are not the same object, we can use the built-in "id()" function that shows the location are not the same
    test_1 = [1, 2, 3]
    test_2 = [1, 2, 3]
    print(id(test_1))
    print(id(test_2))


def func8():
    # However, if you make test_2 equal test_1 (or vise versa), then both test_1 and test_2 will have the same location (they both will have the location of test_1)
    test_1 = [1, 2, 3]
    test_2 = test_1
    print(id(test_1))
    print(id(test_2))
    print(test_1 is test_2)
    # In other words, the "is" operator basically does this...
    print(id(test_1) == id(test_2))


def func9():
    # Few of the things in Python conditionals that might be unexpected
    """
    Things that Python evaluates as False values:
        False
        None
        Zero of any numeric type. EX: 0, 0.0            # Therefore, any number that is not zero will return true
        Any empty sequence. EX: '', (), []              
        Any empty mapping. EX: {}, dict()               # A non-empty sequence or mapping will be true

    Anything else that are not false as stated by the list above, it is most likely going to evaluate to True 
    """
    # For example
    condition = ""

    if condition:
        print("Evaluated to True") # EX: condition = 1 or condition = ["Hi"] or condition = {1:"Why"}
    else:
        print("Evaluated to False") # EX: condition = None or condition="" or condition={} 


# type the name of the function that you want to run below
func9()