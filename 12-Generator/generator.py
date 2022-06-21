"""
https://youtu.be/bD05uGo_sVI

Generators:
The reason why we don't get a list of squared numbers but rather a generator object is because...
generators don't hold the entire result in memory. Rather, it yields one result at a time.
So really, the generator is waiting for us to ask for the next result.

This makes generators better for performance because it is not holding all the values in memory.
"""

def func1():
    """
    This is normally how you would create a class if you wanted to input a square of numbers and return a list with the numbers squared. 
    """
    def square_numbers(nums):
        result = []
        for i in nums:
            result.append(i*i)
        return result

    my_nums = square_numbers([1, 2, 3, 4, 5])

    print(my_nums)  # [1, 4, 9, 16, 25]


def func2():
    """
    In order to make the code above into a generator, we would need to do the follow:
    - remove the 'result' variable (for it won't be necessary anymore)
    - remove the return statement 
    - remove 'result.append' and replace it with 'yield' 

    The reason why we don't get a list of squared numbers but rather a generator object is because...
    generators don't hold the entire result in memory. Rather, it yields one result at a time.
    So really, the generator is waiting for us to ask for the next result.

    """
    def square_numbers(nums):
        for i in nums:
            yield (i*i) # This "yield" keyword is what makes this a generator

    my_nums = square_numbers([1, 2, 3, 4, 5])

    # With this statement on its own, the program hasn't really computed anything yet.
    print(my_nums) # If we just try to print this out now, you won't get a list of the squared numbers but instead get a generator object ('generator object square_numbers')
    # The reason for this is because generators don't hold  the entire result in memory. It yields one results at a time. In other words, the "yield" keyword is waiting for us to ask for the next result/hasn't actually computed anything yet.

    # By doing this, the computer has actually computed something.
    print(next(my_nums)) # By doing this, the program will print out result of the first index (which would result in '1')
    print(next(my_nums))
    print(next(my_nums))
    print(next(my_nums))
    print(next(my_nums)) # By printing out 'next(my_nums)' a couple of times, we can see that each time it prints, it prints out the result values of the number.
    # If we tried to print another time, it would return a "StopIteration" error, meaning that it's out of values to return
    try: # An error is going to thrown and so the try, except statement is here in order to SHOW that it fails
        print(next(my_nums)) # Running next(my_nums) threw a StopIteration error, meaning that the entire generator has been exhausted/out of values.
    except Exception as e:
        print("An error was thrown (StopIteration)")


def func3():
    """
    A good way to print out all the values in a generator is through a for loop
    """
    def square_numbers(nums):
        for i in nums:
            yield (i*i)

    my_nums = square_numbers([1, 2, 3, 4, 5])

    for num in my_nums:
        print(num)


def func4():
    """
    The following lines of code could have been much easier to write as a list comprehension: 
    _____
    def square_numbers(nums):
        for i in nums: 
            yield (i*i)
            
    my_nums = square_numbers([1, 2, 3, 4, 5])
    _____
    REMEMBER: List comprehension isn't a generator but rather acts like a regular list.
    """
    my_nums = [x*x for x in [1, 2, 3, 4, 5]] # square brackets, "[]", forms a regular list comprehension

    print(my_nums) # You can print out the entire list using list comprehension

    for num in my_nums:
        print(num)


def func5():
    """
    However, if we wanted our list comprehension to create a generator instead of a list, all you have to do is to replace the square brackets with parentheses.
    """
    my_nums = (x*x for x in [1, 2, 3, 4, 5]) # Using parentheses, "()", creates a generator list comprehension

    print(my_nums) # Since we are dealing with a generator, it hasn't processed anything yet and therefore returns a generator object.

    # When you cast a generator to a list (and therefore not the same data type), you do lose the advantages you gained in terms of performance.
    print(list(my_nums)) # However, if you really needed to print out the entire generator values without a loop, you can convert the generator object into a list

    for num in my_nums:
        print(num)


def func6():
    """
    In short, generators doesn't really store anything (except for the data its currently displaying). Also, it does take long to execute because once it reaches the 
    keyword 'yield', the program just stops and waits for the the program to call for the next data to process. 

    Lists, on the other hand, will compute and store everything in the list and therefore takes a longer to execute.
    """