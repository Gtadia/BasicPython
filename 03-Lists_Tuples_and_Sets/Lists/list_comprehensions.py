"""
https://youtu.be/3dt4OGnU5sM

List Comprehensions
    A more easier and readable way to create a list.

"example_list = [x1 for x2 in list/range]"
    - x1 is what we wnat to store in "example_list"/it's the function that we want to use to manipulate using x2.
    - x2 is the x1 is going to use to manipulate
    - list/range is the list or the range that we're going to use
    * starting from "for" is where the for loop section begins. 
    So in other words...
    [function <then> for loop]


"exmaple_list = [x1 for x2 in list/range if <boolean_condition>]
    - There's an if statement at the end where x1 is only stored in "example_list" if the boolean condition in the if statement is true
        (if the if statement is TRUE, it will be appended)
        (if FALSE, it will be omitted)

    * YOU CAN ALSO HAVE ELSE STATEMENTS IN LIST COMPREHENSIONS BUT
    NO ELIF STATEMENTS (Not for lists, sets, dictionaries, etc.)
"""

def func1_1():
    """
    A regular for loop
        loops through "nums" and append everything to "my_list" and then we print it out.
    """
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_list = list()
    for n in nums:
        my_list.append(n)
    
    print(my_list)


def func1_2():
    """
    What func1_1 achieves using list comprehensions
    """
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    my_list = [n for n in nums] # list comprehension
    print(my_list)


def func2_1():
    """
    Storing the square of each number in "nums" and then storing in "my_list" using for loops
    """
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_list = []

    for n in nums:
        my_list.append(n**2)

    print(my_list)


def func2_2():
    """
    func2_1 but using list comprehensions
    """
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    my_list = [n*n for n in nums]
    print(my_list)


def func2_3():
    """
    You can also use the "map" and "lambda" functions to achieve the same thing as list comprehensions
    """
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    my_list = map(lambda n: n**2, nums)
    print(list(my_list))


def func3_1():
    """
    If the number is even in "nums", then we're going to store it in "my_list" using for loops
    """
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_list = []

    for n in nums:
        if n%2 == 0:
            my_list.append(n)

    print(my_list)


def func3_2():
    """
    func3_1 achieved through list comprehensions
        This uses the other type of list comprehension that has an if statement at the end
    """
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    my_list = [n for n in nums if n%2 == 0]
    print(my_list)


def func3_3():
    """
    func3_1 achieved using "filter" and "lambda"
    """
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    my_list = filter(lambda n: n%2==0, nums)
    print(my_list)


def func4_1():
    """
    Nested for loops example
    """
    my_list = []

    for letter in "abcd":
        for num in range(4):
            my_list.append((letter, num))
    
    print(my_list)


def func4_2():
    """
    Nested for loops using list comprehensions
        The first for loop is the outer for loop and the second for loop is the inner for loop (and so on)
    """
    my_list = [(letter, num) for letter in "abcd" for num in range(4)]

    print(my_list)



# type the name of the function that you want to run here
func4_1()