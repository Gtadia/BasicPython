"""
https://youtu.be/GfxJYp9_nJA

Namedtuples
    You can think of namedtuples as a lightweight object that works just like a regular tuple but more readable

In order to use a namedtuple, you have to import it from collections:
    'from collections import namedtuple'


* Extra Info (From Comment Section)
namedtuple returns a class (that's a child of the built-in class tuple). 
    The first argument you pass to namedtuple becomes the name of the class, 
    while the list of strings becomes the attributes (data fields). You can 
    then call the constructor (the line of code before the print() method in 
    the video) to make objects.

    This quote from the docs should explain a couple of points here:
    > Named tuple instances do not have per-instance dictionaries, so 
    they are lightweight and require no more memory than regular tuples.
    > To support pickling, the named tuple class should be assigned to a 
    variable that matches typename.
    Pickling is Python's name for its built-in method of serializing an object
"""

def func1():
    """
    For example, say that we want to represent RGB color values using regular tuples
    """
    color = (55, 155, 255)
    print(color[0]) 
    """
    But what if someone else reads your code and doesn't know what the values in the tuple means 
    (Like instead of interpretting the RGB values as values for hue, saturation, and light)
    """


    """
    You could try to resolve this issue through a dictionary like so...
    """
    color = {"red": 55, "green": 155, "blue": 255}
    print(color["red"])
    """
    So why would using a dictionary be a problem?
        - You might have chosen a tuple for a reason (like you are iterating through the different color values)
        - You might have chosen a tuple so that the values cannot be changed (because they're immutable)
        - A dictionary takes longer to write due to the sheer amount of typing that's required
    """


def func2():
    """
    So a named tuple gives you a good balance between readability and the functionality of a tuple

    The syntax of namedtuple is...
        namedtuple(<typename>, [a, b, c, ...])
        or
        namedtuple(<typename>, "a, b, c, ...")                      # automatically breaks up the string into a, b, c, and so on 
        or 
        namedtuple(<typename>, {'a': 0, 'b': 0, 'c':0, ...})        # takes the keywords and ignores their values



        Basically what this does is create a namedtuple object and the name of the tuple is <typename> with fields a, b, c and so on. 
        However, we are going to treat this object like a class and create new objects with this new namedtuple object
    """
    from collections import namedtuple
    Color_Tuple = namedtuple("Color_Tuple", ['red', 'green', 'blue']) 
    color = Color_Tuple(55, 155, 255) # After we named our tuple, we give the nametuple data to store 
    """ color = Color_Tuple(red=55, green=155, blue=255) """ # If you wanted, you can be really specific with your values
    color_2 = Color_Tuple(red=86, green=203, blue=100) # Unlike dictionaries, you can create new colors really quickly 
    color_3 = Color_Tuple._make([23, 100, 93]) # Another way to make a namedtuple "object"

    print(color[0]) # We can get the values returned back like a normal tuple
    print(color.red) # Or we can get the values returned using the name we gave our values

    new_color_2 = color_2._replace(red=100, green=255) # "._replace()" returns a new namedtuple "object" with the new values
    print(new_color_2)


# type the name of the function that you want to run here
func2()