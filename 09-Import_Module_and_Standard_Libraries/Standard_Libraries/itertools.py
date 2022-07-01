"""
The itertools module is a collection of tools for handling iterators. Simply, iterators are data types tha can be used
in a for loop.
Itertools provides some advanced tools when using these loops.
Some of the common tools from Itertools are...
product, permutations, combinations, accumutate, groupby, and infinite iterators
"""
from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement # If you are importing from the same class, you can stack the functions in one line using commas
from itertools import accumulate
import operator # Used in the accumulate examples
from itertools import groupby
from itertools import count, cycle, repeat
import time # Used in the infinite iterators examples

"""
Product will compute the Cartesian product of the input iterables
Cartesian product: Combining all each element with every other element from the other list to create a tuple/point with two elements
Ex: [1, 5] product with [2, 3, 4] creates... [(1, 2), {1, 3), (1, 4), (5, 2), (5, 3), (5, 4)]
"""
a = [1, 2, 5]
b = [3, 4, 6]
prod = product(a, b)
print(prod) # product returns an iterable so you have to use list() in order to see it better
print(list(prod)) # Now you can actually make sense of the result

a = [1, 2]
b = [3]
prod = product(a, b, repeat=2) # repeat makes product create a tuple with 4 elements
# When you use repeat, it will create tuples with 1 and 1, 1 and 2, and so on until you reach the last one where it will repeat itself twice like the 1.
# For example: [1, 2] product with [3] creates... [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]
print(list(prod))

a = [1, 2, 5]
b = [3, 4, 6]
prod = product(a, b, repeat=2) # Just see the results of this and you're know what repeat does for products
print(list(prod))

"""
Permutations will return all possible orderings of an input/returns all the different ways the list can be reordered
"""
a = [1, 2, 3]
perm = permutations(a)
print(perm) # permutations returns an iterable so you have to use list() in order to see it better
print(list(perm))
perm = permutations(a, 2) # we can specify how long the orderings can get (so in this example, we will get a list of all the different ways to order the number 1, 2, and 3 in a list size/length of 2)
print(list(perm))

"""
The combination function will make all possible combinations with a specified length
"""
a = [1, 2, 3, 4]
comb = combinations(a, 2) # returns all the possible 2 number (because the second parameter is 2) combinations that can be made with the specified list (1, 2, 3, and 4)
print(list(comb))
comb_with_replacement = combinations_with_replacement(a, 2)
print(list(comb_with_replacement)) # Because regular combinations removes redundant terms, the combinations_with_replacement was created in case you wanted the redundancy
# redundant terms as in having the same number together in one tuple (ex. (1, 1))

"""
The accumulate function makes an iterator that returns accumulated sums, or any other binary function that you give as an input
"""
a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)
print(acc) # Accumulate returns an iterable so you have to use list() in order to see it better
print(list(acc)) # In this example, you will get [1, 3, 6, 10] as the return for [1, (1+2), (1+2+3), (1+2+3+4)] = [1, 3, 6, 10]

acc = accumulate(a, func=operator.mul) # "operator.mul" means to multiply
print(a)
print(list(acc)) # In this example, the program will return [1, 2, 6, 24] because [1, (1*2), (1*2*3), (1*2*3*4)] = [1, 2, 6, 24]

acc = accumulate(a, func=max) # Will compare the index the program is currently on and compare it with the next term and the larger element will be what the next index is going to be changed to
print(a)
print(list(acc)) # You don't see anything changing because all of the numbers are ordered from least to greatest
a = [4, 2, 5, 3, 4]
acc = accumulate(a, func=max)
print(a)
print(list(acc)) # Now that the list isn't ordered least to greatest, you can see that the greater number when compared between the element in the current index and the next element in the next index,the larger number changes the element in the next index

"""
The groupby function makes an iterator that returns keys and groups from an iterable
In other words, groupby will create a dictionary where the values are separated based on what key it got from something like a function (ex. smaller_than_3), 
therefore separating them into different key value pairs.
"""
def smaller_than_3(x): #
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
# print(group_obj) # groupby returns an iterable so you need list() in order to see it better
for key, value in group_obj:
    print(key, value) # groupby returns an iterable so you need list() in order to see it better
    print(key, list(value))

# Lambdas are small one line function that can have an input and will execute based on some expression and then returns an out.
# You can write better groupby functions using lambdas
a = [1, 2, 3, 4]
group_obj = groupby(a, key=lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))

# Different groupby example
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

group_obj = groupby(persons, key=lambda x: x['age']) # This program will sort and group "people" with the same age
for key, value in group_obj:
    print(key, list(value))

"""
There are three different types of infinite iterators and they are...
count, cycle and repeat

count - Takes in a start value for a parameter and start at that value and count on forever after that.
cycle - Takes in an iterable (such as a list or string) and cycle/loop through each element in each index continuously
repeat - Takes  whatever is passed into it (like strings, numbers, entire lists, entire dictionaries, etc.) and returns it continuously
# THE SECOND PARAMETER IN REPEAT() IS TO SPECIFY HOW MANY TIMES YOU WANT TO REPEAT
"""
# count
for i in count(10):
    print(i)
    if i == 15: # Created just to prevent the count() function from counting on forever
        break

# cycle
start = time.perf_counter()
a = [1, 2, 3]
for i in cycle(a):
    print(i, end=" ") # end=" " is added in order to make the results easier to read
    end = time.perf_counter()
    if end - start > 0.01:
        print()
        break

# repeat
a = [1, 2, 3]
for i in repeat(a, 5):
    print(i)
    if end - start > 2:
        break

