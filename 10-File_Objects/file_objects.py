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
        print(test_file.readline(), end='') # ".readline()" actually just prints the nextline from the file everytime it is run (However, ",readline()" adds a new line on top of the new line from teh print statement, which is why we need "end=''")
 

def func8():
    # You can loop through all of the lines in a file using a for each loop (and like ".readline()", it won't read all of the lines at once and potentially run out of memory)
    with open("test.txt", "r") as t_file:
        for example_line_variable in t_file:
            print(example_line_variable, end='')


def func9():
    # If you want to have finer control on how much of the file is read, you can specify the amount using ".read(<number of characters>)"
    with open("test.txt", "r") as t_file: 
        print(t_file.read(100)) # Prints out the first 100 characters in our file
        print("If you run t_file.read(100) again, it will print the next 100 characters because Python knows where you last left off from")
        print(t_file.read(100)) # Since there wasn't another 100 characters left in the file, ".read()" will just return an empty string when it reaches the end


def func10():
    # EXAMPLE CODE: if your file is really large but you want to print the entire thing out without running out of memory? Just print the lines of code in chunks
    with open("test.txt", "r") as t_file:
        size_to_read = 10

        file_contents = t_file.read(size_to_read)

        while len(file_contents) > 0:
            print(file_contents, end='*') # end='*' allows us to see when a new chunk of file contents is being printed out 
            file_contents = t_file.read(size_to_read)


def func11():
    # The reason why Python is able to tell where you last left off in a file is because there is an imaginary cursor that advances everytime you tell it to read
    # You can check the position of the cursor by using ".tell()"
    with open("test.txt", "r") as t_file:
        t_file.read(10) # The cursor should have read 10 characters so therefore the cursor should be on the 10th position
        print(t_file.tell()) # Tells us that the location of the cursor is on the 10th position


def func12():
    # We can move the cursor around in the file using the ".seek()" method
    with open("test.txt", "r") as t_file:
        print(t_file.read(20)) # reads 20 characters and therefore moves the cursor by 20 characters
        t_file.seek(0) # moves the cursor back to the beginning/the 0th position
        print(t_file.read(20)) # reads the first 20 characters again and moves the cursor to the 20th position (again)

        print("Compared to...")

        print(t_file.read(20)) # reads 20 characters and therefore moves the cursor by 20 characters
        print(t_file.read(20)) # reads the next 20 characters and therefore moves the cursor by 20 more characters


def func13():
    # You can write to a file if the file is opened to be writeable
    # If you tried to write a file that isn't writable (opened as "read" or "append"), you will get a "io.UnsupportedOperation: not writable"
    with open("test2.txt", "w") as t_file: # If you try to open a file (in any mode) that does not exist in your directory, it will just create that file in that directory. 
        # If the file already exists and you open in "write" mode, it will just overwrite whatever is in that file so be careful (if you don't want it to overwrite, you can just append to the file using the "append" mode)
        pass # You don't have to write to the file to have Python create the file


def func14():
    # writing to a file using ".write()"
    with open("test2.txt", "w") as t_file:
        t_file.write("Test") 
        t_file.write("Test") # ".write()" also rembemers where the cursor is (while the file is opened, just like ".read()") 

    # Everytime time you open a closed file and write to it, it will put the cursor at the beginning and overwrite everything (delete everything in the file and start anew)


def func15():
    # You can also use ".seek()" in write mode
    with open("test2.txt", "w") as t_file:
        t_file.write("Longer Test Text")
        t_file.seek(0)
        t_file.write("Test") # Only overwrites the text that is in its way/doesn't clear the entire file because the file was still opened (only clears the entire file if open a closed file and write to it)
        # In other words, the second ".write()" modifies the file to say ("Tester Test Text")


def func16():
    # You can next content managers within each other 
    # EXAMPLE CODE: Making a copy of a file by reading a file and inputting that data into a new copy file
    with open("test.txt", "r") as read_t_file:
        with open("test_copy.txt", "w") as write_t_file:
            for line_of_text in read_t_file:
                write_t_file.write(line_of_text)


def func17():
    # If you want to work with image files, you have to open the file in binary mode (it defaults to text (utf-8))
    # For this example, we're going to take the original image and make a copy just like what we did with func16 (instead with just images)
    with open("noice_image.jpg", "rb") as read_b_file: # "rb" = read binary
        with open("noice_image_copy.jpg", "wb") as write_b_file: # "wb" = write binary
            for line_of_binary_data in read_b_file:
                write_b_file.write(line_of_binary_data)
    
    # "ab" = append binary, "r+b" = read and write binary


def func18():
    # Just like a normal text file, you can copy the file by chunks
    with open("noice_image.jpg", "rb") as read_b_file: # "rb" = read binary
        with open("noice_image_copy.jpg", "wb") as write_b_file: # "wb" = write binary
            chunk_size = 4096

            read_file_chunk = read_b_file.read(chunk_size)
            
            while len(read_file_chunk) > 0:
                write_b_file.write(read_file_chunk)
                read_file_chunk = read_b_file.read(chunk_size)


# type the name of the function that you want to run here
func17()