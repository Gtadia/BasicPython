"""
https://youtu.be/3dt4OGnU5sM

Set Comprehensions
    Just like list comprehensions, you can add:
        - nested loops
        - conditionals/if else statements
"""

def func1_1():
    """
    Example set comprehension:
        What the set comprehension is to achieve using a for loop
    """
    nums = [1, 1, 2, 1, 3, 4, 6, 4, 5, 7, 4, 3, 4, 6, 7, 9, 0, 9 ,8, 6, 5, 7, 8, 5, 4] # A jumbled set of numbers
    my_set = set()

    for n in nums:
        my_set.add(n)
    
    print(my_set)


def func1_2():
    """
    func1_1 using set comprehensions
    """
    nums = [1, 1, 2, 1, 3, 4, 6, 4, 5, 7, 4, 3, 4, 6, 7, 9, 0, 9 ,8, 6, 5, 7, 8, 5, 4]

    my_set = {n for n in nums}
    
    print(my_set)



func1_2()