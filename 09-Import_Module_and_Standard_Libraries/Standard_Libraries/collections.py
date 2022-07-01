"""
Collections

The collections module implements special container data types and provides alternatives with some additional functionalities 
compared to the general built-in containers; such as dictionaries, lists, and tuples


Five common collection containers are...         
    Counter
    namedtuple
    OrderedDict
    defaultdict
    deque
"""

def func1():
    """
    Counter is a container that stores its elements as dictionary keys with how many times a certain thing 
    (for example, if you input a string, it will tell you how many times a certain character (including 
    punctuations, numbers, and spaces) appears).
    """
    from collections import Counter

    a = "abcdeabcde,,, Hello Hello"
    myCounter = Counter(a) # returns "Counter({'e': 4, 'l': 4, ',': 3, 'a': 2, 'b': 2, 'c': 2, 'd': 2, ' ': 2, 'H': 2, 'o': 2})""
    print(myCounter)

    # The .values() and .keys() in dictionaries work with Counter (because counter creates a dictionary)
    print(myCounter.values()) # returns "dict_values([2, 2, 2, 2, 4, 3, 2, 2, 4, 2])"
    print(myCounter.keys()) # returns "dict_keys(['a', 'b', 'c', 'd', 'e', ',', ' ', 'H', 'l', 'o'])"
    
    # You can find the most common character that appears in the counter/dictionary (the parameter is to show the "3" most common variable in a list with tuples in it)
    print(myCounter.most_common(3)) # returns "[('e', 4), ('l', 4), (',', 3)]"

    # Since .most_common() returns a list with tuples in it, you can access individual parts of the tuple inside the list as well
    print(myCounter.most_common(1)[0][0]) # .most_common(1) returns a list with one tuple. The first "[0]" lets you access the first tuple and the second "[0]" lets you access the first part of the selected tuple (will print the letter "e"
    print(myCounter.most_common(5)[3][1])

    # You can have the counter/dictionary print out only the keys using .elements() (BUT .elements() returns an iterable, meaning we need to put .elements() in list() to make it print nicely)
    print(myCounter.elements()) # Returns an iterable object ("<itertools.chain object at 0x109728fd0>")
    # The elements converted to a list will have all the same values clumped next to each other
    print(list(myCounter.elements())) # returns "['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'e', 'e', 'e', 'e', ',', ',', ',', ' ', ' ', 'H', 'H', 'l', 'l', 'l', 'l', 'o', 'o']"


def func2():
    """
    The namedtuple is an easy to create and light object type (similar to a struct)
    """
    from collections import namedtuple
    Point = namedtuple("Coordinate", "X,  Y") # The first parameter is a class name and the second parameter are going to be the fields (the comma means you're going to add more variables)
    # In other words, namedtuple created a class called "Coordinate" with the fields "X" and "Y"
    pt = Point(4, 5) # We are giving the values for x and y (x=4 and y=5)
    print(pt)
    print(pt.X, pt.Y) # Just like a normal class, we can access the different fields


def func3():
    """
    OrderedDict is just like a regular dictionary but they remember the order that the items 
    were inserted (They're practically USELESS now since regular dictionaries ALSO have the 
    ability to remember the order the elements were inserted).
    """
    from collections import OrderedDict
    ordered_dict = OrderedDict()
    ordered_dict['a'] = 1
    ordered_dict['b'] = 2
    ordered_dict['c'] = 3
    ordered_dict['d'] = 4
    print(ordered_dict)

    ordered_dict_2 = OrderedDict()
    ordered_dict_2['b'] = 2
    ordered_dict_2['d'] = 4
    ordered_dict_2['c'] = 3
    ordered_dict_2['a'] = 1
    print(ordered_dict) # it prints out the dictionary in the order they were inserted

    regular_dict = {}
    regular_dict['b'] = 2
    regular_dict['d'] = 4
    regular_dict['c'] = 3
    regular_dict['a'] = 1
    print(ordered_dict) # You can see that the order is still remembered even when a regular dictionary is used


def func4():
    """
    defaultdict is very similar to the regular/usual dictionary, with the only difference that defaultdict will 
    have a default value if the key has not been set yet.
    """
    from collections import defaultdict
    d = defaultdict(int) # The "int" in the parameters tell "defaultdict" to make integer the default type of the dictionary
    d['a'] = 1
    d['b'] = 2
    print(d['a'])
    print(d['b'])
    print(d['c']) # When we enter a key that does not exist, the dictionary will return the default value of the data type that we specified (for "int", it is 0)
    # float will return a default value of 0.0, list will return an empty list ("[]"), and a string (str) will return an empty string ("")


def func6():
    """
    Deque is a double ended queue and it can be used to add or remove elements from both ends and are implemented 
    in a way that will run very efficiently.
    """
    from collections import deque
    d = deque()
    d.append(1) # adds elements to be end/from the right.
    d.append(2)

    d.appendleft(3) # adds elements to the front/from the left.
    print(d)

    print(d.pop()) # return (remember the element that was removed) & remove the last element (the right-most element) from the list (the list is inside of a deque data type)
    print(d)
    print(d.popleft()) # return and remove the first element (the left-most element) from the list (the list is inside of a deque data type)
    print(d)
    d.clear() # removes every element from the list
    print(d)

    d = deque([1, 2, 3, 4, 5]) # How to call a deque with some elements already in it
    d.extend([4, 5, 6]) # How to add multiple elements to a deque from the right side/to the end
    print(d)
    d.extendleft([0, -1, -2]) # How to add multiple elements to a deque from the left side/at the front (the list of elements that you want to add will be added backwards (ex: [0, -1, -2] = [-2, -1, 0]
    print(d)

    d = deque([1, 2, 3, 4, 5])
    d.rotate(1) # shifts all the elements in the deque to the right by a factor of 1
    print(d)
    d.rotate(-2) # shifts all the elements in the deque to the left by a factor of 2




# type the name of the function that you want to run here
func6()