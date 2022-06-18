"""
https://youtu.be/Uh2ebFW8OYM

Read and Write to Files
"""


# When you open a file, it's recommended that you use a context manager 
def func1():
    # Simple way to open a file to run it
    open_test_file = open("test.txt") # If the file is in a different directory, then type the filepath to that file
    # When you open a file, you can have it be opened for 1) reading, 2) writing, 3) appending (basically like writing but you can only add new stuff in), and 4) reading and writing
    # If you don't specify anything, it defaults to reading.
    open_test_file.close() # While Python won't get mad too often if you don't close your file but it's still really good practice to close it anyways after you're done using it
    # If you forget to close a file, you may end up with leaks that may cause you to run over the maximum allowed file descriptors on your system and your applications could trhwo an error


def func2():
    # You can open a file to read, write, append or read and write
    open_test_file = open("test.txt", "r") # This opens the file on read mode
    open_test_file = open("test.txt", "w") # This opens the file on write mode
    open_test_file = open("test.txt", "a") # This opens the file on append mode
    open_test_file = open("test.txt", "r+") # This opens the file on read and write mode
    
    open_test_file.close()



def func3():
    #  ".name" will return the name of the file (no matter what mode the file was opened with)
    open_test_file = open("test.txt", "w")
    print(open_test_file.name) # Returns "test.txt"
    
    open_test_file.close()


def func4(): 
    # You can check which mode you opened the file as
    open_test_file = open("test.txt", "r")
    print(open_test_file.mode) # Returns which mode the file was opened with

    open_test_file.close()


def func5():
    # How to open a file using a context manager (anything that works with the regular way of opening files works with the content manager as well)
    """The reason why a context manager is a better way to open a file is because it allows us to work with files from 
    within the context manager block and after we exit it/the block of code, it'll automatically close the file for us 
    (it will also close the file if there are any exceptions that were thrown within the context manager)."""
    with open("test.txt", "r") as open_test_file: # You can open a file with a context manager using "with open() as <variable name>"
        print(open_test_file.name)
    
    # We can still access "open_test_file" from outside of the context manager but it'll just be closed, as demonstrated by the print statement below
    print(open_test_file.closed) # ".closed" is a funciton that tests whether or not a file is closed


def func6():
    # How to read the contents of the file
    with open("test.txt", 'r') as test_file:
        print(test_file.read()) # ".read()" returns the contents of the file


def func7():
    # If you don't want ot lead all of the contents of a file into memory or just want a couple of lines from the file, you can use the following
    with open("test.txt", "r") as test_file:
        print(test_file.readlines()) # ".readlines()" actually takes all the lines from a file and puts each line in a list
        print(test_file.readline()) # ".readline()" actually just prints the nextline from the file everytime it is run
 

func7()