# The collections module implements special container data types and provides alternatives with some additional functionalities compared to the general built-in containers; such as dictionaries, lists, and tuples
# Five common collection containers are...         Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

# Counter is a container that stores its elements as dictionary keys with how many times a certain thing (for example, if you input a string, it will tell you how many times a certain character (including punctuations and numbers and spaces) appears)
a = "abcdeabcde,,, Hello Hello"
myCounter = Counter(a)
print(myCounter)
print(myCounter.values())
print(myCounter.keys()) # The .values() and .keys()  in dictionaries work with Counter (because counter creates a dictionary)
print(myCounter.most_common(3)) # You can find the most common character that appears in the counter/dictionary (the parameter is to show the "3" most common variable in a list with tuples in it)
# Since .most_common() returns a list with tuples in it, you can access individual parts of the tuple inside the list as well
print(myCounter.most_common(1)[0][0]) # .most_common(1) returns a list with one tuple. The first "[0]" lets you access the first tuple and the second "[0]" lets you access the first part of the selected tuple (will print the letter "e"
print(myCounter.most_common(5)[3][1])
# You can have the counter/dictionary print out only the keys using .elements() (BUT .elements() returns an iterable, meaning we need to put .elements() in list() to make it print nicely)
print(myCounter.elements()) # Returns an iterable
print(list(myCounter.elements()))

# The namedtuple is an easy to create and light object type (similar to a struct)
Point = namedtuple("Coordinate", "X,  Y") # The first parameter is a class name and the second parameter are going to be the fields (the comma means you're going to add more variables)
# In other words, namedtuple created a class called "Coordinate" with the fields "X" and "Y"
pt = Point(4, 5) # We are giving the values for x and y (x=4 and y=5)
print(pt)
print(pt.X, pt.Y) # Just like a normal class, we can access the different fields

# OrderedDict is just like a regular dictionary but they remember the order that the items were inserted (They're practically USELESS now since regular dictionaries ALSO have the ability to remember the order the elements were inserted)
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)
ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['d'] = 4
ordered_dict['c'] = 3
ordered_dict['a'] = 1
print(ordered_dict) # it prints out the dictionary in the order they were inserted
ordered_dict = {}
ordered_dict['b'] = 2
ordered_dict['d'] = 4
ordered_dict['c'] = 3
ordered_dict['a'] = 1
print(ordered_dict) # You can see that the order is still remembered even when a regular dictionary is used

# defaultdict is very similar to the regular/usual dictionary, with the only difference that defaultdict will have a default value if the key has not been set yet.
d = defaultdict(int) # The "int" in the parameters tell "defaultdict" to make integer the default type of the dictionary
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['b'])
print(d['c']) # When we enter a key that does not exist, the dictionary will return the default value of the data type that we specified (for "int", it is 0)
# float will return a default value of 0.0, list will return an empty list ("[]"), and a string (str) will return an empty string ("")

# Deque is a double ended queue and it can be used to add or remove elements from both ends and are implemented in a way that will run very efficiently.
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
