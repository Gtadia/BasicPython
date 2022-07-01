"""
Set
"""

def func1():
    # Sets are unordered, mutable, and cannot contain duplicates
    mysets = {1, 2, 3} # Kind of like dictionaries without the key value pair (you don't add the colons (":"))
    print(mysets)


def func2():
    # You can't have duplicates in sets
    mysets = {3, 2, 1, 2, 1, 3} # The list will remove the duplicates
    print(mysets)


def func3():
    # You can create a set using set()
    mysets = set([5, 3, 5, 1]) # set() only takes iterable (like lists and strings) as a input
    print(mysets)
    mysets = set("Hello")
    print(mysets)


def func4():
    # If you want to create an empty set, you have to use set() and not {} because {} will create an empty dictionary
    mysets = set()
    print(type(mysets))


def func5():
    # You an add and remove things from your set
    mysets = set([1,2,3])

    mysets.add(1) # If the variable already exists, then it's going to be added but nothing will change in the set
    mysets.add(4)
    mysets.remove(4) # You can remove items by specifying which one to remove
    try:
        mysets.remove(5)
    except Exception as err:
        print(err) # When you remove something that doesn't exist in the set, it will throw a KeyError


def func6():
    # The better way to remove elements from a set is to use .discard()
    mysets = set([1, 2, 3])
    removed = mysets.discard(3) # It removes elements normally
    print(removed) # .discard() doesn't return anything/the value that it removed.
    print(mysets)
    mysets.discard(4) # If the element does not exist, then it does nothing and not throw an error
    print(mysets)


def func7():
    # You can also remove everything from the list
    mysets = {1, 2, 3}
    print(mysets)
    mysets.clear()
    print(mysets)


def func8():
# We can save the element that we popped off of the set (and remove the element as well) using .pop()
    mysets = {5, 2, 3}
    removed = mysets.pop() # .pop() will retrun what was removed
    print(removed) # It will remove the element with the lowest value (so in this case, it will remove 2, and if we use pop again, it will remove 3
    print(mysets)
    print(mysets.pop())
    print(mysets)


def func9():
    # We can loop through the set
    mysets = {1, 2, 3, 4}
    for i in mysets:
        print(i)


def func10():
    # We can check if an element is in the set
    mysets = {1, 2, 3, 4}
    if 1 in mysets:
        print(True)
    else:
        print(False)
    if 5 in mysets:
        print(True)
    else:
        print(False)


def func11():
    # We can check the union of two sets (union combines both lists/sets and removes any duplicates)
    odd = {1, 3, 5, 7, 9}
    even = {0, 2, 4, 6, 8}
    prime = {2, 3, 5, 7}
    union = odd.union(even)
    print(union)
    union = odd.union(prime)
    print(union)
    

def func12():
    # You can check the intersection of two sets (the intersection of two lists/sets returns a list/set with only the elements that they share in common)
    odd = {1, 3, 5, 7, 9}
    even = {0, 2, 4, 6, 8}
    prime = {2, 3, 5, 7}
    intersection = odd.intersection(even)
    print(intersection)
    intersection = odd.intersection(prime)
    print(intersection)


def func13():
    # You can check the difference of two sets (the difference of two lists/sets returns a list/set with only the elements that the lists/sets did not share in common with the first list)
    setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    setB = {1, 2, 3, 10, 11, 12}
    difference = setA.difference(setB) # returns 4, 5, 6, 7, 8, 9
    print(difference)
    difference = setB.difference(setA) # returns 10, 11, 12
    print(difference)


def func14():
    # In math, difference actually returns what both lists/sets don't have in common (and you can do the same with .symmetric_difference())
    setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    setB = {1, 2, 3, 10, 11, 12}
    difference = setA.symmetric_difference(setB)
    print(difference)


def func15():
    # You can update sets with another set (basically .union())
    setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    setB = {1, 2, 3, 10, 11, 12}
    setA.update(setB) # It updates setA with the union of setA and setB
    print(setA)


def func16():
    # There's also a intersection update method (updates the set so that its value is the result of the intersection)
    setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    setB = {1, 2, 3, 10, 11, 12}
    setA.intersection_update(setB) # returns 1, 2, 3
    print(setA)


def func17():
    # There's also a difference update method (updates the set so that its value is the result of the difference (not symmetric_difference))
    setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    setB = {1, 2, 3, 10, 11, 12}
    setA.difference_update(setB)
    print(setA)
    # REMMEBER: The difference is different for which set is first
    setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    setB = {1, 2, 3, 10, 11, 12}
    setB.difference_update(setA)
    print(setB)


def func18():
    # There's also a .symmetric_difference update method
    setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    setB = {1, 2, 3, 10, 11, 12}
    setA.symmetric_difference_update(setB)
    print(setA)


def func19(): 
    """
    We can check if a set is a subset.
        A subset is a set that has all of the same elements as another set (aka: the superset)

        EX: 
        subset = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        superset = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    """
    setA = {1, 2, 3, 4, 5, 6}
    setB = {1, 2, 3}
    print(setA.issubset(setB)) # This returns false because because all the elements of setA is not in setB
    print(setB.issubset(setA)) # This returns true because setB is a subset of setA


def func20():
    # We can check if a set is a superset (a superset is a set that has all the elements of a subset and more)
    setA = {1, 2, 3, 4, 5, 6}
    setB = {1, 2, 3}
    print(setA.issuperset(setB))
    print(setB.issuperset(setA))


def func21():
    # We can check if two sets are disjoint, meaning that they don't share anything is in common
    setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    setB = {10, 11, 12}
    print(setA.isdisjoint(setB))


def func22():
    # We can copy sets but we have to do it a certain way or else the "copy" set will have the same changes on the original set
    setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    setB = setA
    setB.add(10)
    print(setB)
    print(setA) # You can see that both sets have the update made to it

    # In order to make a TRUE copy of a set, you have to use .copy()
    setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    setB = setA.copy()
    setB.add(10)
    print(setB)
    print(setA) # You can see that the original set doesn't have any modifications made to it, unlike the copy/setB


def func23():
    # You can also use the set() method to make a TRUE copy/Another way to make a TRUE copy 
    setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    setB = set(setA)
    setB.discard(9)
    print(setB)
    print(setA)


def func24():
    # You can create an immutable version of a normal set
    immutable_set = frozenset([1, 2, 3, 4]) # Everything with a normal set applies to the frozenset, except for the fact that it is immutable
    """
    # You CANNOT do ANY of this because this set is immutable
    immutable_set.add(5)
    immutable_set.remove(4)
    immutable_set.update({5, 6, 7})
    """
    print(immutable_set)



# type the name of the function that you want to run here
func24()