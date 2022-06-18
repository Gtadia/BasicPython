"""
https://youtu.be/CqvZ3vGoGs0        # Starting from 14:50
https://youtu.be/tJxcKyFMTGo

Some Commmon Standard Libraries
"""

def func1():
    # Random module
    # https://docs.python.org/3/library/random.html
    import random 
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(random.choice(test_list)) # Returns a a random element from a list ("random.choice()")
    print(random.randint(8, 10)) # Returns a random integer from [a, b] ("random.randint(a, b)" where a and b are both inclusive)
    print(random.random()) # Returns a random floating point number in the range [0.0, 1.0) (in other words, inclusive of 0.0 but exclusive of 1.0)
    print(random.uniform(4, 10)) # Returns a random floating point number from [a, b] ("random.uniform(a, b)" where a and b are both inclusive)


def func2():
    # Math module
    import math

    print(math.radians(90)) # Converts degrees into radians and returns it
    print(math.sin(math.pi)) # Can do trigonmetric calculations (sin, cos, tan) using radians (also math.pi is how you get pi in Python)


def func3():
    # datetime and calendar module
    import datetime
    import calendar

    print(datetime.date.today()) # Returns today's date
    print(calendar.isleap(2020)) # Returns whether a certain year is a leap year


def func4():
    # OS module
    # Gives access to the underlying operating system
    import os
    print(os.getcwd()) # "os.getcwd" (cwd = "current working directory") returns the current directory that this code is running in
    
    os.chdir('../BasicPython/9-Import_Module_and_Standard_Libraries') # Changes the current directory to any directory you specify  (In macos/linux, "../" means to go back by one directory from the current one you're on)
    print(os.getcwd())

    print(os.listdir()) # returns a list of the files and folders in the current directory (or you can specify which direcotry you would like it to use)

    os.mkdir("OS-Demo") # Makes a single directory in the current directory that you're in
    os.makedirs("OS-Demo/Sub-OS-Demo") # Can make a directory with a sub directory inside of the directory (top level directory)
    # If the specific directory already exists, a "FileExistsError" will be thrown

    os.removedirs("OS-Demo/Sub-OS-Demo") # Removes even the intermediary directories (if this sub-directory has sub-directories of its own or files, then it cannot remove it. The directory has to be completely empty)
    """os.rmdir("OS-Demo") # Removes a single directory (if this directory has sub-directories or files, then it cannot remove it. The directory has to be completely empty)"""

    os.rename("rename_me.txt", "renamed.txt") # Renames a file that it can find within the directory 

    print(os.stat('renamed.txt')) # Prints out a list with a bunch of stats about this text file
    print(os.stat("renamed.txt").st_size) # You can just pull certain data from stats instead of an entire list of stats "st_size" returns the size of the file in bytes

    os.rename("renamed.txt", "rename_me.txt") # This is just here to make sure that the name returns back to "rename_me.txt"


def func5():
    # Since the standard library is just a python file as well, we can modify and access them like regular python files 
    import os
    print(os.__file__) # This is how you can access the location of a module, whether or not it's built-in/from the standard library or one that you've/someone else wrote
    # EXTRA INFO: "__" or double underscore is sometimes referred to as "dunder"


def func6():
    # Example of using the standard libraries
    import os
    from datetime import datetime

    os.chdir('../BasicPython/9-Import_Module_and_Standard_Libraries')
    date_file_was_modified = os.stat("rename_me.txt").st_mtime
    print(datetime.fromtimestamp(date_file_was_modified))    


def func():
    # A python easter egg
    import antigravity


# type the name of the function that you want to run here
func6()