# Strings are ordered and immutable data collection type used for text representation

# These are single line comments
"""
These are docstrings 
    Python doesn't have multi-line comment but we can use multi-line strings instead 
    (multiline strings are reviewed later in this file)
"""

def func1(): 
    myString = "This is a string" # A string can be created from either single ('') or double ("") quotes
    print(myString)
    myString = 'This is a string' # A string created using single quotes
    print(myString)


def func2():
    """
    You have to be careful when using these quotes. For example, 
    myString = 'I'm a programmer' 

    This is going to throw an error because there's a single quote after the "I" and therefore ends the string prematurely. 
    In order to prevent this, you can either use an escaping backslash or use double quotes.
    """
    myString = 'I\'m a programmer'
    print(myString)
    myString = "I'm a programmer"
    print(myString)


def func3():
    # You can use triple quotes for multi-line strings
    myString = """Hello, 
    I 
    can
    Use
    multiple
    lines! 
    Isn't that cool?
    """
    print(myString)


def func4():
    # You can use an escaping backslash to say that the text on the next line should be moved to the line above it/connect the next line with the line above it into one string.
    myString = """Hello \
World, How are you today? 
I'm pretty good, how are you? 
    """
    print(myString)


def func5():
    # You can access certain parts/characters of string like lists
    myString = "Hello World!"
    char = myString[0]
    print(char)
    char = myString[-1]
    print(char) # You can use negative characters to access the list from the back (-1 is the very last character, -2 is the second last and so on)
    char = myString[1:10:2]
    print(char) # In other words, you can access characters from a string like accessing elements from a list

    """
    You cannot change certain characters from a string because they are IMMUTABLE. 
    For example: 
    myString = "Hello, World!" 
    myString[0] = "B"

    This will throw a TypeError because you cannot change certain elements from a list
    """


def func6():
    # You can access whole substrings (certain parts of a string) using slicing
    myString = "Hello World"
    substring = myString[1:5]
    print(substring)


def func7():
    # You can concatenate (combine) two or more strings together
    myString = "Hello, "
    name = "Rick"
    greeting = myString + name
    print(greeting)


def func8():
    # You can iterate through a list
    greeting = "Hello World!"
    for i in greeting:
        print(i)


def func9():
    # You can also check if a certain character is in the string
    greeting = "Hello World!"
    if 'e' in greeting:
        print(True)
    else:
        print(False)
    if "!" in greeting:
        print(True)
    else:
        print(False)
    if "ello" in greeting: # We can also check for substrings
        print(True)
    else:
        print(False)
    if "ElLo" in greeting: # The substring/character checker is CASE SENSITIVE though
        print(True)
    else:
        print(False)


def func10():
    # White space is printed out on Python
    myString = '       Hello World        '
    print(myString)


def func11():
    # We can get rid of white space using .strip()
    myString = '          Hello World        '
    myString = myString.strip() # You need myString to equal itself with .strip() in order to for it to save the changes to itself
    print(myString)


def func12():
    # We can convert every character to an uppercase and lower case
    myString = "Hello, World! 12345"
    print(myString.upper()) # Notice how it leaves the punctuations and other non-letter characters behind
    print(myString.lower())


def func13():
    # We can check if a string starts with a specific character
    myString = "Hello, World! 12345"
    print(myString.startswith('World'))
    print(myString.startswith('hello')) # Remember, .startswith is case sensitive
    print(myString.startswith('Hello'))
    print(myString.lower().startswith('hello')) # You could do this if you aren't sure of the case (upper or lower) the string you're checking is


def func14():
    # We can check if a string ends with a specific character
    myString = "Hello, World! 12345"
    print(myString.endswith("World"))
    print(myString.endswith("Hello"))
    print(myString.endswith("12345"))


def func15():
    # We can find the (first) index where we find a certain character
    myString = "Hello, World! 12345"
    print(myString.find('o')) # returns 4 because that's the index where it first appears
    print(myString.find('O')) # returns -1 because it can't find capital "O" because it's case sensitive


def func16():
    # We can count the number of times a certain character appears in the string
    myString = "Hello, World! 12345"
    print(myString.count("o"))
    print(myString.count("O")) # returns 0 because it can't find any capital "O" because .count() is case sensitive


def func17():
    # We can replace certain characters/substrings/strings using .replace() (.replace() will replace every instance of the certain substring)
    # .replace() WILL return a new string and DOES NOT change the original string
    myString = "Hello World"
    print(myString.replace("World", "Universe"))
    print(myString.replace("orl", "eir")) # You can replace substrings
    print(myString.replace("o", 'y')) # You can also replace single characters ######## You can see that it replaced EVERY SINGLE "o" with the letter "y"
    print(myString.replace("11", "100")) # If the substring that is the replaced cannot be found in the string, then nothing is going to be replaced


def func18():
    # You can convert a string into a list by having each individual word become individual elements of a list using .split()
    myString = "How are you doing?"
    myList = myString.split() # .split()'s default argument for deciding when to split the string into individual words are " "/spaces
    print(myList)
    myString = "   How   are  you  doing          Today?"
    myList = myString.split() # You can see that it removes all the white space for you
    print(myList)
    # If you want to split your sentences based on a different criteria, you have to specify it.
    myString = "How,Are,You,Doing,Today?"
    myList = myString.split(",")
    print(myList)


def func19():
    # You can convert a list of words (like the one created from .split()) back into a sentence using .join()
    myString = "How,are,you,doing,today?"
    myList = myString.split(",") # A list of words created using the .split() method
    my_New_String = ''.join(myList)
    print(my_New_String) # It didn't add a space before each word
    my_New_String = ' '.join(myList)
    print(my_New_String) # Adds a space before each word
    my_New_String = ','.join(myList)
    print(my_New_String) # I basically converted the list back into the string that it came from


def func20():
    from timeit import default_timer as timer
    # Example of using a string "multiplier" and converting it into a string
    myList = ['a'] * 1000000
    # Bad code
    startMyTimerISaid = timer()
    myString = ""
    for i in myList:
        myString += i # This is very expensive on the memory because it creates a new string (at "i") and then assign it back to myString (this is because strings are immutable)
    stopMyTimerISaid = timer()
    print(f"Time: {stopMyTimerISaid - startMyTimerISaid}")
    # Good code
    startTheTimer = timer()
    myString = ''.join(myList) # This isn't expensive on the memory and much cleaner
    stopTheTimer = timer()
    print(f"Time: {stopTheTimer - startTheTimer}")


def func21():
    # You can format strings
    # Old way to format strings ("%" or ".format()")
    var = "Tom"
    myString = "the variable is %s" % var # The percent sign shows that it is a place holder for a string (that's what the "s" is for) variable, which is specified outside the format with %var.
    print(myString)
    var = 5
    myString = "the variable is %d" % var # %d shows that it is a placeholder for a decimal value variable
    print(myString)
    var = 3.64159
    myString = "the variable is %d" % var # %d will only print out the whole number and not print out the decimal points
    print(myString)
    var = 3.14159
    myString = "the variable is %f" % var # %f shows that it is a placeholder for a float variable (by default, it will show 6 deciaml places)
    print(myString)
    var = 3.14159
    myString = "the variable is %0.2f" % var # %0.2f only shows the first two decimal point of the variable ("3.14")
    print(myString)
    var = 6
    myString = "the variable %f" % var # will convert the variable to a float
    print(myString)

    var = 3.14159
    myString = "the variable is {}".format(var) # This is the other, "old" way to format strings
    print(myString)
    var = "monkey"
    myString = "the variable is {}".format(var) # If you don't specify the format, then it will accept basically any format
    print(myString)
    var = 3.14159
    myString = "the variable is {:0.2f}".format(var) # you can choose to specify the format
    print(myString)
    var = 3.14159
    var2 = "monkeys"
    myString = "the variable is {} and {}".format(var, var2) # You can have more than one variables to add to the format (the ordering must be correct because the first parameter is going to be the first thing to entire the string and the second parameter is going to be on the second part of the format and so on)
    print(myString)
    var = 3.14159
    var2 = "space monkeys"
    myString = "the variable is {:0.2f} and {}".format(var, var2) # You can still choose to specify the variable types


"""
var = 3.14159
myString = "the variable is {} and {}".format(var) # the number of formats must equal to the number of variables in the parameter
print(myString)
"""


def func22():
    # New way to format strings ("f-Strings")
    # f-strings are actually faster than the other two "older" format methods
    var = 3.14159
    var2 = "MIT"
    myString = f"the variable is {var} and {var2}" # You can use the f-strings to add the variables into the formats directly
    print(myString)
    # You can manipulate the variables directly inside the formats for they run/evaluate the calculations at run time
    var = 3.14159
    var2 = "MIT"
    myString = f"the variable is {var * 2} and {var2}"
    print(myString)


def func23():
    print(help(str))  # Prints "... find(...)    Return the lowest index in..."
    print(help(str.lower))  # Prints "lower(self, /)      return a copy of the string converted to lowercase. "


def func24(): 
    # REMEMBER: If you want the print function to not create a new line after each time it prints, you can do the following
    print("Example text", end="") # This makes it that the print function doesn't do anything after it prints
    print("Hey Vsauce ", end="Michael \t here!") 


# type the name of the function that you want to run below
func24()