"""
https://youtu.be/6iF8Xb7Z3wQ

Loops and Iteration
- For loops
- While loops
- For each loops
"""

def func1():
    # for each loop
    nums = [1, 2, 3, 4, 5]

    for each_num in nums: 
        print(each_num) 


def func2():
    # The "break" keyword will completely break out of a loop
    nums = [1, 2, 3, 4, 5]

    for each_num in nums: 
        if each_num == 3: 
            print("3 Found!", end=" ")
            break # Will exit out of the loop
    print(each_num, end=" ")
    # prints out "1 2 3 Found!"


def func3():
    # The "continue" keyword will move onto to the next iteration of the loop
    nums = [1, 2, 3, 4, 5]

    for each_num in nums: 
        if each_num == 3:
            print("Skipped 3", end=" ")
            continue
        print(each_num, end=" ")
    # prints out "1 2 Skipped 3 4 5" 


def func4():
    # nested loops (a loop inside of a loop)
    nums = [1, 2, 3, 4, 5]

    for each_num in nums:
        for letter in "abc": 
            print(each_num, letter) 


def func5():
    # Just a regular for loop (using "range()")
    for i in range(15): # i starts at 0 and ends at 14
        print(i)


def func6():
    # In order to have i start at a different number, use "range(starting position (inclusive), ending position (exlcusive))"
    for i in  range(1, 16): # i starts at 1 and ends at 15
        print(i)


def func7(): 
    # While loops
    x = 0
    while x < 10:
        print(x)
        x += 1 


# type the name of the function that you want to run below
func7()