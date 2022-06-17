"""
https://youtu.be/CqvZ3vGoGs0

When you import something in Python, it runs all of the code inside of the module. 
This is how it gets all of the variables, functions, and classes inside of the module.
    If we have print statements or anything else like that, it will also run them as well. 
"""

def func1():
    # You can place the import module in the main body, inside of a function, inside of a class, etc.
    import my_example_module # This is how you import a module/python file in Python
    # You can see that all we did was import the file and we can see that it ran the print statement ("Imported my_example_module...")
    """
    How did Python know while module to import even though we didn't specify a file path of anything like that?
        The way that this works is that Python checks multiple locations and the locations that it checks is located 
        within a list called "sys.path"
        We can see this list if we import the sys module (func8)
    """


def func2():
    # If you wanted to use/run anything inside of the imported module, you have to use this formatting "<module>.<variable/function/class>"
    import my_example_module
    test_list = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]
    test_variable = my_example_module.find_index(test_list, "Chemistry")
    print(test_variable)


def func3():
    # In python, you can import the module and have it referred back to with a different name
    import my_example_module as test_mod
    test_list = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]  
    test_variable = test_mod.find_index(test_list, "Calculus")
    print(test_variable)


def func4():
    # If you only want to import a specific function/variable/class from a module, you can do that instead of importing the entire module
    from my_example_module import test # we don't need to write "my_example_module.test" but rather just say "test"
    print(test) # REMEMBER: this type of import statement will still run the entirety of "my_example_module" even though we're only using the variable "test"
    # ALSO REMEMBER: Once you import only a specific part of a module, you can't try to get anything else from the module now (EX: You can't call "my_example_module.Thing")


def func5():
    # You can import multiple variable/functions/class
    from my_example_module import test, find_index
    test_list = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]  
    print(test)
    print(find_index(test_list, "Computer Science"))
    

def func6():
    # You can still call the imported variable/function/class something else just like you can with the module
    from my_example_module import test as t, find_index as test_i
    test_list = ["Chemistry", "Economics", "Calculus", "Computer Science", "Literature", "Spanish"]  
    print(t)
    print(test_i(test_list, "Chemistry"))


def func7(): 
    # You can also just import everything using "*"
    """
    from my_example_module import *
    print(test) 
    # The reason why I commented this code out is because it threw the following error:
        SyntaxError: import * only allowed at module level

    In other words, we can't run "import *" inside of a function but rather only in the main body 
    """
    # The problem with this is that now we don't know if a certain variable/function/class came from a module or from this file or from a different module


def func8():
    # If we import the sys, module, we can see the list that contains where Python checks for modules
    import sys
    print(sys.path) # You can see that the first module was actually this file path ("../BasicPython/9-Import_Module_and_Standard_Library")
    """
    How do these directories get added to this list? 
        Directories get added in this order:
            1. The directory containing the code that we're running
            2. The directories in the Python path environment variable
            3. The standard library directories
            4. Site packages directory for third-party packages
    """

    """
    However, if we have a module that we want to import that is not within the file path of sys.path, we can manaully add it
    by treating sys.path like any other list (because that's what it is, a simple list)

    *** ASSUMING THAT "my_example_module" is the "Downloads" folder***
    import sys
    sys.path.append("../Downloads") # assume that ".." means the the other stuff that makes up the full directory (ex: "/Users/guest/")
    """
    """
    If you want to learn even further into this, just watch the video linked in the 1st docstring starting at 10:00 (for mac), 
    """


# type the name of the function that you want to run here
func8()
