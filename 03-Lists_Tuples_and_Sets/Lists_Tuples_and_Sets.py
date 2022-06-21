"""
Lists = Are a mutable data collections that also stores the elements in a specific index to be referenced
Tuples = Are basically immutable versions of lists
Sets = Are basically unordered lists that doesn't store duplicate values (if there are any duplicates, it will remove it)
"""

def func1():
    # How to initialize and declare a list variable
    courses = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]
    print(courses)


def func2():
    # Finding the length of the list using "len()"
    courses = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]
    print(len(courses))


def func3():
    # Getting the value at a certain index (REMEMBER: The index starts at 0, not 1)
    courses = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]
    print(courses[0]) # Prints out chemistry
    print(courses[5]) # Prints out Spanish


def func4(): 
    # In Python, you can use negative indices (-1 is the very first index and so on)
    courses = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]
    print(courses[-1]) # Prints out Spanish
    print(courses[-6]) # Prints out Chemistry


def func5():
    # You can get the values from multiple indices
    # list[start (inclusive): end (exclusive): step]
    courses = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]
    print(courses[0:2]) # Prints out Chemistry, & Economics
    print(courses[1:6:2]) # Prints out Economics, Computer Science, and Spanish
    print(courses[5:2:-1]) # Prints out Spanish, Literature, and Computer Science in that order 


def func6(): 
    # You can add more items to a list using ".append()"
    courses = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]
    courses.append("Physics")
    print(courses) # Physics has been added as the very last element in the list


def func7():
    # Unlike ".append()", ".insert()" allows us to add an element anywhere on the list
    # genericList.insert(index, element)
    courses = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]
    courses.insert(0, "Physics") # Inserts "Physics" at index 0 (the very beginning) and pushes the other elements by one element (e.g., so Chemistry would now have the index of 1)
    print(courses)



def func8(): 
    # You can use insert or append to insert/append a list to a list 
    courses = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]
    courses_2 = ["Engineering", "Geometry"]
    courses.insert(0, courses_2)
    print(courses) # The problem is that when the is appended/inserted, the list becomes a 2D list (a list inside of a list) at that specific index
    print(courses[0]) # As you can see, at index 0, we get the entirity of "courses_2"
    # You can do the same thing with ".append()" except that it appends the list at the end


def func9():
    # Use ".extend()" if you want to combine two lists, not insert/append a list to a list
    courses = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]
    courses_2 = ["Engineering", "Geometry"]
    courses.extend(courses_2)
    print(courses) # Each individual elements inside of courses_2 was just extended onto the end of courses


def func10():
    # We can remove values using ".remove()"
    courses = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish", "Economics"]
    courses.remove("Economics")
    print(courses) # removes only the FIRST/earliest instance of "Economics"


def func11(): 
    # We can also remove values using ".pop()" but it only removes the very last value
    courses = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]
    courses.pop()
    print(courses)
    # ".pop()" also returns the element that is removes
    courses = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]
    element_popped = courses.pop() # Equals "Spanish"
    print(element_popped)
    print(courses)


def func12():
    # You can sort lists in assending order
    courses = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]
    courses.reverse() # reverses the list
    print(courses)

    courses = ["1235", "2", "Hello", ".';jsdfj", "H.e.l.l.o.5.6"]
    courses.sort() # Sorted in Alpharebetta order or numerical order (More specically, it is sorted from least to greatest ASCII order)
    print(courses)


def func13(): 
    # We can also sort lists in desending order 
    courses = ["1235", "2", "Hello", ".';jsdfj", "H.e.l.l.o.5.6"]
    courses.sort(reverse = True)
    print(courses)


def func14(): 
    # There is a way to sort a function in assending and desending order without altering the original list
    courses = ["1235", "2", "Hello", ".';jsdfj", "H.e.l.l.o.5.6"]
    sorted_list = sorted(courses) # sorts the list in assending order without altering the original list
    print(courses)
    print(sorted_list) # Now you can see the sorted version of the list

    reverse_sorted_list = sorted(courses, reverse=True) # sorts the list in desending order
    print(reverse_sorted_list)


def func15():
    # REMEMBER: In Python, a list CAN contain elements from different data types 
    list = [1, 2, 4, "Things", True, "Hahaha"] # This list contains ints, Strings, and boolean values
    # However, you can not sort the elements in this list. It either has to be all strings or ints/floats (you CAN sort a list with both ints and floats), booleans (False goes first then True), etc.
    lists = sorted(list)
    print(lists)
    list.sort() # Both ".sort()" and "sorted()" doesn't work
    print(list) 


def func16(): 
    # We can find the minimum and maximum value in a list (based on ordering of the ACSII characters)
    courses = ["1235", "2", "Hello", ".';jsdfj", "H.e.l.l.o.5.6"]
    print("Max value: " + max(courses))
    print("Min value: " + min(courses))


def func17(): 
    # If we have a list of integers/floats, we can find the sum of every value of each element
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(sum(nums))

    nums_floats = [1.0, 4.5, 6.2]
    print(sum(nums_floats))


def func18(): 
    # If can find the first/earliest index of a certain element using ".index()"
    courses = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]
    print(courses.index("Computer Science"))
    # If a value does not exist in a list, such as "Art", a ValueError is thrown


def func19(): 
    # Instead of value of the index that an element is in, we can just get a boolean value ("True" if it exists, "False" if it doesn't)
    courses = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]
    print("Calculus" in courses) # Prints "True"
    print("Art" in courses) # Prints "False"
     

def func20(): 
    # We can iterate through every item in a list with a for-each loop
    courses = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]
    for course_element in courses:
        print(course_element)


def func21(): 
    # We can access the index and the value using the "enumerate()" function in Python
    courses = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]
    for index, different_course_element in enumerate(courses):
        print(index, different_course_element) 

    # If you wanted the index to start at 1 instead of 0, you can do the following
    for index, different_course_element in enumerate(courses, start=1):
        print(index, different_course_element) # The first index is 1, isntead of 0 and so on


def func22():
    # If we want to turn a list into a string separated by commas, we use the string method ".join()"
    courses = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]
    courses_str = ", ".join(courses) # You can put anything inside of the parentheses to separate each element inside of the list
    print(courses_str)


def func23(): 
    # We can separate a string into a list after a certain character, like a comma
    faang = "Facebook, Amazon, Apple, Netflix, Google"
    new_list = faang.split(", ") # 
    print(faang) # prints as a string
    print(new_list) # prints as list


def func24(): 
    # Lists are mutable, meaning that you can change its elements 
    # For xample: 
    example_list = ["Food", "Is", "Edible", "In", "Most", "Cases"]
    example_list[1] = "Isn't"
    print(example_list) # We can see that this didn't throw an error


def func25():
    # You can make a TRUE copy of a list that is independent from the original list
    list_original = ["banana", "cherry", "apple"]
    list_copy = list_original.copy() # Makes a copy of "list_original"
    list_copy.append("lemon")
    print(list_copy)
    print(list_original)


def func26():
    # ANOTHER way to make a TRUE copy of a list that is independent from the original list
    list_original = ["banana", "cherry", "apple"]
    list_copy = list_original[:]
    list_copy.append("lemon")
    print(list_copy)
    print(list_original)


def func27():
    # QUICKLY modifying the contents of a list
    a = [1, 2, 3, 4, 5, 6]
    b = [i*i for i in a]
    c = [(x+x)*x for x in b]
    # list_name = [<expression> for <new_variable_that_you_can_create_in_this_spot> in <original_list_name>]
    print(a)
    print(b)
    print(c)


def func28():
    # However, unlike lists, TUPLES are IMMUTABLE, meaning that you cannot change its elements
    # For example: 
    example_tuples = ("Airplanes", "Stay", "In", "The", "Air", "Most", "Of", "The", "Time") # Notice how you can create a tuples using parentheses instead of square brackets like lists
    example_tuples[0] = "Particles in the air"
    print(example_tuples) # This throws a TypeError because "'tuple' object does not support item assignment"
    
    # Because tuples are immutable, it can't append/insert, remove/pop elements, or sort (sorted works though because it doesn't change the original tuple). Other than that, tuples and lists nearly behave the same


def func29():
    # Sets are unordered and doesn't store any duplicate values
    example_sets = {"The", "The", "Dopest", "Thing", "About", "Horses", "Horses", "Is", "That", "They're", "Basically", "Grass", "Engines"}
    print(example_sets)


def func30():
    # We can see if two sets have any variables in common (Using ".intersection()")
    sets_1 = {"seven", "ate", "nine"}
    sets_2 = {"seven", "didn't", "eat", "nine"}
    print(sets_1.intersection(sets_2)) # Returns {"seven", "nine"} because that's what they have in common


def func31(): 
    # If you wanted to know what elements were in sets_1 but not in sets_2, then we can use the ".difference()" method
    sets_1 = {"seven", "ate", "nine"}
    sets_2 = {"seven", "didn't", "eat", "nine"}
    print(sets_1.difference(sets_2)) # Returns {"ate"}


def func32(): 
    # if you wanted to combine two sets, you can use the ".union()" method
    sets_1 = {"seven", "ate", "nine"}
    sets_2 = {"seven", "didn't", "eat", "nine"}
    print(sets_1.union(sets_2))


def func33(): 
    # How to create empty lists, tuples, and sets

    # Empty Lists
    empty_list = []
    empty_list = list()

    # Empty Tuples
    empty_tuple = ()
    empty_tuple = tuple()

    # Empty Sets
    empty_set = {} # CAUTION!!!! This doesn't create an empty set, this creates an empyt dictionary
    empty_set = set()


# Type the name of the function that you want to run
func29()