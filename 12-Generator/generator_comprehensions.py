"""
https://youtu.be/3dt4OGnU5sM

Generator Expression Comprehensions
"""

def func1_1():
    """
    Generator Expression Comprehension Example:
        What the Generator Expression comprehension is to achieve using a for loop
    """
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def gen_func(the_nums):
        for n in the_nums:
            yield n*n
    
    my_gen = gen_func(nums)

    for i in my_gen:
        print(i)


def func1_2():
    """
    func1_1 achieved using comprehensions
    """
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    my_gen = (n*n for n in nums) # generator comprehension

    for i in my_gen:
        print(i)



func1_2()