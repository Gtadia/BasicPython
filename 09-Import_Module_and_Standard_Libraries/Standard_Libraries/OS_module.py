"""
https://youtu.be/tJxcKyFMTGo

OS Module
"""
import os

def func1():
    print(os.getcwd()) # "os.getcwd" (cwd = "current working directory") returns the current directory that this code is running in


def func2():
    os.chdir('../BasicPython/9-Import_Module_and_Standard_Libraries') # Changes the current directory to any directory you specify  (In macos/linux, "../" means to go back by one directory from the current one you're on)
    print(os.getcwd())


def func3():
    print(os.listdir()) # returns a list of the files and folders in the current directory (or you can specify which direcotry you would like it to use)


def func4():
    os.mkdir("OS-Demo") # Makes a single directory in the current directory that you're in
    os.makedirs("OS-Demo/Sub-OS-Demo") # Can make a directory with a sub directory inside of the directory (top level directory)
    # If the specific directory already exists, a "FileExistsError" will be thrown

    os.removedirs("OS-Demo/Sub-OS-Demo") # Removes even the intermediary directories (if this sub-directory has sub-directories of its own or files, then it cannot remove it. The directory has to be completely empty)
    os.rmdir("OS-Demo") # Removes a single directory (if this directory has sub-directories or files, then it cannot remove it. The directory has to be completely empty)


def func5():
    os.rename("rename_me.txt", "renamed.txt") # Renames a file that it can find within the directory 
    os.rename("renamed.txt", "rename_me.txt") # This is just here to make sure that the name returns back to "rename_me.txt"


def func6():
    print(os.stat('renamed.txt')) # Prints out a list with a bunch of stats about this text file
    print(os.stat("renamed.txt").st_size) # You can just pull certain data from stats instead of an entire list of stats "st_size" returns the size of the file in bytes


def func7():
    # Example of using the standard libraries
    from datetime import datetime

    os.chdir('../BasicPython/9-Import_Module_and_Standard_Libraries') # chdir = change directory
    date_file_was_modified = os.stat("rename_me.txt").st_mtime
    print(datetime.fromtimestamp(date_file_was_modified))    


def func8():
    # Let's say that we want to see the entire direcotry tree and files within the desktop 
    # If you want to traverse the directory tree and print all of the directories and the files then you can us "os.walk()"
    # os.walk() is a generator that yields a tuple of three values as its walking the directory tree (so for each directory that it sees, it yields the directory path, the directories within that path, and the files within that path)
    # By default, os.walk traverses from the top down 
    for dirpath, dirnames, filenames in os.walk('../../'): # For me, this brings me back to my Document folder
        print("Current Path:", dirpath) # Returns the current directory
        print("Directories:", dirnames) # Returns the directories within the current directory 
        print("Files:", filenames) # Returns the files within the current directory
        print() # Whitespace

        # First it searches thought the direcotries in the Documents folder, then it enters the first directory in Documents and the prints out all of the directories within that and then enter the first one in that list and so on until it has entered and searched through each and every directories


def func9():
    # "os.environ.get('HOME')" returns the home directory
    print(os.environ.get('HOME'))

 
def func10():
    # If you wanted to get the file path of a file that is in a directory, EX: a "test.txt" file in the HOME direcotry.
    # You could do something like this (os.environ.get("HOME") + '/test.txt')
    # OR you could use "os.path.join()"
    print(os.path.join(os.environ.get("HOME"), 'test.txt'))


def func11(): 
    # If you have a filepath and you only wanted the BASE NAME, or only the DIRECTORY NAME, or both, use "os.path" (it doesn't have to be a real directory, but it does have to be in the format of a file path)
    print(os.path.basename("/example_directory/test.txt")) # Returns the base name ("test.txt")
    print(os.path.dirname("/example_directory/test.txt")) # Returns the directory name ("example_directory")
    print(os.path.split("/example_directory/test.txt")) # Returns 1) the directory name ("example_directory") and 2) the base name ("test.txt") in a tuple

    print(os.path.exists("/example_directory/test.txt")) # You can check to see if a file path actually exists (Returns True or False)
    print(os.path.isdir("../"))  # Returns True when the filepath is a directory
    print(os.path.isfile("9-Import_Module_and_Standard_Libraries/OS_module_from_standard_library.py")) # Returns True when the filepath is a file
    print(os.path.splitext("/example_directory/test.txt")) # Returns the file root and the extension into a tuple ("example_directory/test", ".txt")


def func12():
    # If you want to see all of the different functions that exist in the OS module, you can check the directory within the module
    print(dir(os))
    print(dir(os.path)) # And you can see additional functionality what each individual os functions have 


# type the name of the function that you want to run here
func1()