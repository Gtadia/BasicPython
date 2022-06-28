"""
https://youtu.be/3dt4OGnU5sM

Dictionary comprehensions
"""

def func1_1():
    """
    Example Code:
        Combining the first, second, third, (and so on) elements of both list 1 and 2 into a tuple and then appending that tuple
        into a list

    EX:
        list_1 = [1, 2, 3, 4, 5]
        list_2 = [6, 7, 8, 9, 10]

        RESULT:
        [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
    """
    things = ["Apple", "Herseys", "Spoon", "Piano", "T-shirt"]
    classifications = ["Fruit", "Chocolate", "Silverware", "Instrument", "Clothing"]

    print(list(zip(things, classifications))) # use zip to combine the first, second, third, etc. elements in multiple lists in a tuple and then store those tuples in a list


def func1_2():
    """
    Instead of storing the things and its classifications into tuples, we can make the "thing" as the key and the "classification" as the value
    using for loops
    """
    things = ["Apple", "Herseys", "Spoon", "Piano", "T-shirt"]
    classifications = ["Fruit", "Chocolate", "Silverware", "Instrument", "Clothing"] 
    my_dict = {}

    for a_thing, the_classification in zip(things, classifications): # We can use zip to get the elements in tuples to be easily converted to a dictionary (but it's not technically necessary)
        my_dict[a_thing] = the_classification

    print(my_dict) 


def func1_3():
    """
    Achieveing what we did for func1_2 using dictionary comprehensions
    """
    things = ["Apple", "Herseys", "Spoon", "Piano", "T-shirt"]
    classifications = ["Fruit", "Chocolate", "Silverware", "Instrument", "Clothing"] 

    my_dict = {a_thing: the_classification for a_thing, the_classification in zip(things, classifications)}
    
    print(my_dict)

def func1_4():
    """
    We can have if statements at the end like LIST comprehensions
        (if the if statement is TRUE, it will be appended)
        (if FALSE, it will be omitted)

    EX:
    Not appending "Spoon" to our dictionary
    """
    things = ["Apple", "Herseys", "Spoon", "Piano", "T-shirt"]
    classifications = ["Fruit", "Chocolate", "Silverware", "Instrument", "Clothing"] 

    my_dict = {a_thing: the_classification for a_thing, the_classification in zip(things, classifications) if a_thing != "Spoon"}
    
    print(my_dict)



# type the name of the function that you want to run here
func1_4()