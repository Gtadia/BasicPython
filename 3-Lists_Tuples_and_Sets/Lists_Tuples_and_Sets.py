"""
Lists
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
    # list[start (inclusive): end (exclusive): jump]
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
    # Ways to sort lists
    courses = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]
    courses.reverse() # reverses the list
    print(courses)

    courses = ["1235", "2", "Hello", ".';jsdfj", "H.e.l.l.o.5.6"]
    courses.sort() # Sorted in Alpharebetta order or numerical order (More specically, it is sorted from least to greatest ASCII order)
    print(courses)






# Type the name of the function that you want to run
func12()