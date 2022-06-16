"""
https://youtu.be/9Os0o3wzS_I

Functions: Basically specific instructions packed together to perform a specific task

*Heads Up*
    We've been using functions this entire time to separate certain code throughout the lessons


With functuons, you can keep your code "dry", meaning that instead of copy and pasing the same line 
of code everytime you need it, you can just call a function with that code in it/DON'T REPEAT CODE



Keyword Arguments: Arguments that you pass into a function WITH "<keyword>=<value>"
Positional Arguments: Arguments that you pass into a function WITHOUT "<keyword>=<value>" but rather just passes in the <value>

<Check the last print statement for func5
In other words, the position of where you input the value matters but doesn't really matter too much with keyword arguments because Python knows where the value belongs because of the keyword.
"""

def function_name():
    """
    This is how you create a function
    """
    # Code goes here


def func1():
    # Functions don't have to have anything inside of it but you can't leave it entirely empty. If you want to leave it empty, you can use the keyword "pass"
    pass # when we run this function, it will return "None"


def func2():
    # When you run code inside of a function, most of the time, whatever happens in the function stays in the function
    nothing_else_outside_of_this_function_can_see_this_variable = "Something" # only func2 can see this variable
    return nothing_else_outside_of_this_function_can_see_this_variable # However, we can return the value stored inside of the variable


def func3(parameter_variable):
    # Functions can have parameters that are passed in when it is called/runs.
    return parameter_variable + " Function" # parameter_variable is local to func3 and therefore cannot be accessed outside of this function


def func4(age, name): 
    # You can have more than one parameter
    return "age: {}, name: {}".format(age, name)


def func5(age, name="Mike"): # You can declare a default variable so when nothing is passed in for name, the function will just use the default value of "Mike"
    return "age: {}, name: {}".format(age, name)


def func6(*args, **kwargs): # the variables doesn't need to be "args" and "kwargs"
    # These specific parameters are allowing us to accept any number of parameters (0 to essentially infinity (not really but it an accept a very large number of parameters))
    print(args)
    print(kwargs)



"""
func1
"""
print("-----FUNCTION 1-----")
func1() # If you want to run a function, you could call the fnction by its name
# The parentheses tells Python that it's a function and that it should execute the code inside of the function
print(func1) # However, if you leave out the parentheses, then Python will just return that "func1" is a function in a certian location in memory
print("-----FUNCTION 1-----", end="\n\n\n")


"""
func2
"""
print("-----FUNCTION 2-----")
the_result_of_func2 = func2()
print(the_result_of_func2)
print(len(the_result_of_func2))
print(the_result_of_func2.upper())
print(func2()) # or we can just straight up use the return value without storing it in another variable
print(len(func2()))
print(func2().upper()) # We can just treat the return value from a function as a string/int/float/blooean/etc. \
print("-----FUNCTION 2-----", end="\n\n\n")


"""
func3
"""
print("-----FUNCTION 3-----")
print(func3("Hi")) # This is passing the variable "Hi" to parameter_variable for func3 to use
print("-----FUNCTION 3-----", end="\n\n\n")


"""
func4
"""
print("-----FUNCTION 4-----")
print(func4(15, "Amy")) # REMEMBER: Since in the parameters we have "(age, name)", this means that you need to input the value for age first then the value for the name
# print(func4()) # If you don't pass in the correct number of parameters that a function has, Python will throw a TypeError unless the function has default parameters (see func5)
print("-----FUNCTION 4-----", end="\n\n\n")


"""
func5
"""
print("-----FUNCTION 5-----")
print(func5(21, "Peter")) # When we pass in something for name, it uses the value that we pass in
print(func5(52)) # When we don't pass in anyhting for name, it uses the default value "Mike"
# A cool thing that you can do in Python...
print(func5(age = 5, name = "donkey")) # You can use the name of parameters equal to the value that you want when pass in the parameters to a function
# MAKE SURE THAT THE PARAMETERS ARE IN ORDER  

print(func5(name="Hello", age=5)) # the position of where you input the value matters but doesn't really matter too much with keyword arguments because Python knows where the value belongs because of the keyword
print("-----FUNCTION 5-----", end="\n\n\n")


"""
func6
"""
print("-----FUNCTION 6-----")
func6("Math", "Science", name="Johnny", age=34567) 
# All of the positional arguments (*args) are stored in a tuple  
# Meanwhile, all of the keyword arguments (**kwargs) are stored in a dictionary with the keyword values as the keys 

# What if we had a list and a dictionary and we wanted to pass the list as a positional argument and the dictionary as a keyword argument
courses = ['Math', 'Science']
info = {'name': 'Johnny', 'age': 34567}
func6(courses, info) # We might assume that this is how we do it but instead, this just passes in the list and dictionary as it is instead of passing in the contents of the list and dictionary
func6(*courses, **info) # However, if you type *, it UNPACKS the list into its individual elements and ** UNPACKS a dictionary into "<keyword>=<value>"
print("For example, you can visuallize what '*' does:", *courses)
# However, when the "*" and "**" is used in the parameters, it packs up the positional arguments into a list ("*") and the keyword arguments into a dictionary ("**")
print("-----FUNCTION 6-----", end="\n\n\n")