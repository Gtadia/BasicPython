"""
https://youtu.be/vTX3IwquFkc

String Formatting
"""

def func1():
    # Simple string formatting in Python
    sentence = "My name is {} and I am {} years old.".format("Max", 12) # "{}" are "placeholders" in Python
    print(sentence)


def func2():
    # If you want to, you can specifically number your placeholders
    sentence = "{0} is a person and is {1} years old. {0} can do things.".format("Max", 12) # "Max" is placeholder 0 and 12 is placeholder 1
    print(sentence)


def func3():
    # You can also grab specific fields from dictionaries/lists/tuples from our placeholders

    # dictionary example
    example_dict = {"name": "Max", "age": 12}
    sentence = "{0[name]} is a person and is {1[age]} years old. {0[name]} can do things.".format(example_dict, example_dict)
    # However, insteead of have "example_dict" twice, you can have the placeholders use the same number
    sentence = "{0[name]} is a person and is {0[age]} years old. {0[name]} can do things.".format(example_dict)
    print(sentence)

    # list example
    example_list = ["Max", 12]
    sentence =  "{0[0]} is a person and is {0[1]} years old. {0[0]} can do things.".format(example_list)
    print(sentence)

    # tuples example
    example_tuple = ("Max", 12)
    sentence =  "{0[0]} is a person and is {0[1]} years old. {0[0]} can do things.".format(example_tuple)
    print(sentence)


def func4(): # Apparently you can have a class inside of a function...
    # you can also access attributes in a similar way to what we did in func3
    class Person(): 
        def __init__(self, name, age):
            self.name = name
            self.age = age

    person_1 = Person("Max", 12) # Creating a "Person" object with input parameters for its attributes
    sentence =  "{0.name} is a person and is {0.age} years old. {0.name} can do things.".format(person_1) # We're grabbing attributes/variables from within a class/object
    print(sentence)


def func5():
    # We can create a string format using keyword values
    sentence =  "{name} is a person and is {age} years old. {name} can do things.".format(name="Max", age=12) # Anywhere the placeholder matches the keyword will pass in the value stored under the keyword into the placeholder
    print(sentence)


def func6():
    # Keeping in mind what we did in func5, we can just unpack a dictionary to have the same affect (see func6 in 8-Functions/functions.py)
    example_dict = {"name": "Max", "age": 12}
    sentence = "{name} is a person and is {age} years old. {name} can do things.".format(**example_dict)
    print(sentence)


def func7():
    # With placeholders, we can do things like add padding to numbers so that numbers with less than 3 digits will have a however many zeros they need in order to have "3" digits
    for i in range(0, 101, 10):
        sentence = "The current value is {:-3}".format(i) # including ":03" inside of the placeholder adds a 3 digit padding using 0 (":-3" padds everything to far right and ": 3" centers the padding)
        print(sentence)


def func8():
    # In order to pad/round a float up to a certain number of decimal places, we can including ":.#f" within the placeholder
    pi = 3.14159265
    sentence = "Pi is equal to {:.3f}".format(pi) # prints out "3.142" (rounds to the nearest thousandths place)
    print(sentence) 


def func9():
    # In order to separate large number (numbers over 1000) with commas (ex: 1,000,000), insert ":," inside of the placeholder
    sentence = "1 MB is equal to {:,} bytes".format(10**6) # works for both ints and floats
    print(sentence)


def func10():
    # You can chain these formatting together
    example_dict = {"number_1": 2, "number_2": 12.023}
    sentence = "integer: {number_1:05,} float: {number_2:,.2f}".format(**example_dict)
    print(sentence)


# type the name of the function that you want to run here
func10()