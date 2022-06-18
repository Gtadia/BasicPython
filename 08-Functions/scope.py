"""
https://youtu.be/QVdf0LgmICw

Scopes
"""
"""
REMEMBER THIS WITH SCOPES
    LEGB
    Local, Enclosing, Global, Built-in          # This is the order that determines what a variables is assigned to (Python first checks variables/functions in the local scope, then the enclosing scope, then global, then built-in)

Local -     Variables defined within a function
Enclosing - Variables in the local scope of enclosing functions         # enclosing fuctions are functions inside of a function
Global -    Variables defined at the top level of a module or explicity declared global using the global keyword
Built-in -  Variables/names that are pre-assigned in Python
"""

# Examples:
"""Global Scope"""
global_variable = "This is a global variable" # This is a global variable because this is in main body of our file
"""Gloabl Scope"""


"""Local Scope"""
def example(parameters_are_also_local_variables): # The only difference with parameters is that it can get its value from outside of the local scope by having it passed in (or it can be from the default parameter value)
    global also_a_global_variable # You can't declare and initialize a variable with the "global" keyword on the same line
    also_a_global_variable = "This is also a global variable" # This is a global variable because we declared it as a global variable
    local_variable = "This is a local variable" # This is a local variable because this inside of the function "example"
"""Local Scope"""


"""Built-in Scope"""
import builtins
from threading import local # All of the built-in functions/variables in Python

# example:
print(min([5, 1, 2, 3, 4])) # 'min' and 'print' is a built-in function
# print(dir(builtins)) # This will print out all of the built-in functions (not variables) that is available to Python
"""Built-in Scope"""


"""Enclosing Scope"""
def outer_func_1():
    local_variable = "outer local variable"
    
    def inner_func():
        local_variable = "inner local variable"
        print(local_variable)

    inner_func() # Prints out "inner local variable"
    print(local_variable) # Prints out "outer local variable"


# outer_func_1() # Runs the outer function




# 'nonlocal' example:
def outer_func_2():
    local_variable = "outer local variable"
    
    def inner_func():
        nonlocal local_variable # This makes 'local_variable' inside of the inner_func modify 'local_variable' in 'outer_func_2'    (BUT REMEMBER, 'local_variable' must be already declared (and initialized with at least "None" in the outer function)
        local_variable = "inner local variable"
        print(local_variable)

    inner_func() # Prints out "inner local variable"
    print(local_variable)

# outer_func_2() # Rusn the 2nd outer function
"""Enclosing Scope"""