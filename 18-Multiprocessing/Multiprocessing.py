"""
https://youtu.be/fKl2JW_qrso

Multiprocessing:
We want to use multiprocessing whenever it's going to significantly speed up our program. This speed up comes from different tasks running in parallel on different
CPU threads (therefore, CPU Bound tasks are a good candidate for seeing benefits with mutliprocessing).

CPU Bound tasks:
Tasks that are crunching a lot of numbers and using the CPU a lot. These types of tasks are the ones that you would want to use multiprocessing with. However, these
processes are not going to be sped up, and sometimes even slowed down, by threading.

I/O Bound tasks:
Tasks that are waiting for input and ouput operations to complete and not really using the CPU al that much. (Some examples are file system operations and network
operations, such as downloading stuff online) These tasks are the ones that you would want to use threading with. You can also speed IO bound tasks up by using
multiprocessing as well.
"""

def func1():
    """
    The follow code below isn't using concurrency/threads nor is it using multi-processing to make the code run faster.

    In other words, the process is running synchronously
    """
    import time
    
    start = time.perf_counter()


    def do_something():
        print("Sleeping 1 second...")
        time.sleep(1)
        print("Done Sleeping...")
    
    
    do_something()
    do_something()
    
    finish = time.perf_counter()
    
    print(f"Finished in {round(finish - start, 2)} second(s)")



"""FOR FUNCTIONS 2 THROUGH 5"""
def do_something():
    """
    Strangely, the multiprocessing module is a little different from threading in that the "target=" can't seem to find the local inner local function. It has to
    be outside of the outer function in order to be able to see it. This is why for functions 2 - 5, we're going to use this do_something function outside
    of the outer functions.
    """
    import time
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done Sleeping")
"""FOR FUNCTIONS 2 THROUGH 5"""



def func2():
    """
    The older way of doing mutliprocessing

    In order to first set multiprocessing, you need to set up 'multiprocessing.Process(target=<function name>)' first for the number of processes that you want. 
    However, when you create the multiprocessor, you are not actually running the code. In order to run the code, you need to use the 'start' method for each 
    process.

    1. "if __name__ == '__main__'
    The reason why we need "if __name__ == '__main__':" is because we're importing the multiprocessing module and by using "if __name__ == '__main':" (which I'll 
    be calling "The Code" from now on), we are avoiding the unintended side effects, such as starting a new process. A module that doesn't have it, when imported, 
    runs as if it were being ran direclty. By including the "if" statement there, this will only allow the code within that "if" statement to run, if ran directly 
    (such as running it yourself), whereas if you were to import a module that has an "if" statement, it "loads" it in a sense, since it's no longer referred to 
    as "__main__". 

    If you ran it directly, it's "labelled" as "__main__". When imported, it's "labelled" as it's file name, more or less. 
        EX:
        If we run "Multiprocessing.py" directly, __name__ = "__main__".
        If we import Multiprocessing.py" into a different file (for example, "Exmple_File.py"), __name__ = "Multiprocessing.py"

    Knowing this, a translation may help:
    If it's name is main, run this code. (In this case, it could result in a stray process)
    Else (if it's name is anything else), do something else, usually nothing. 

    Stray process are like stray animals. One may (or may not) be harmless, but when they gather, it can cause mayhem. 
    """
    import multiprocessing
    import time
    
    start = time.perf_counter()
    
    """
    def do_something():  # Normally, this function would work but because this function is inside of another function ("func2"), the "target=" can't seem to find it
        print("Sleeping 1 second...")
        time.sleep(1)
        print("Done Sleeping")
    """
    
    if __name__ == '__main__': # We need this line of code in order to get the multiprocessing prepared to run (Details in the multi_line comment above)
        p1 = multiprocessing.Process(target=do_something) # the 'target' is the function that you want to run
        p2 = multiprocessing.Process(target=do_something)
    
        p1.start() # This is how you start the process.
        p2.start()
    
    # You need to make sure you run the finish and print statement within "if __name__ == '__main__' for processes that are called will run the entire code and print
    # out the print statement again (in other words, if you have anything in your code that you don't want to run in the threads, it has be to inside of the "if __name__ == '__main__':"
    
    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)} second(s)")

    """
    The output of the program is as follows: 
    Finished in 0.0 second(s)
    Sleeping 1 second..
    Sleeping 1 second...
    Done Sleeping
    Done Sleeping

    The reason why the finished running line of code ran first is because, just like threading, the program continued on after it assigned the processes. In other words, 
    after the program had assigned the different processes to run the function 'do_something', the program continued on with the rest of the code and ran the 'finish' 
    variable and printed out the time. 
    Since it takes a longer amount of time to spin up than threads, the program was able to assign the processes and run the 'finish' variable and print out the time 
    before the program had time to run the processes. This is why the finish time was printed out first before the 'sleeping 1 second' notification.
    """


def func3():
    """
    In order to have the program finish the processes before continuing on with the rest of the code, we need to use the 'join' method.
    """
    import multiprocessing
    import time

    start = time.perf_counter()

    """
    def do_something(): # Normally, this function would work but because this function is inside of another function ("func3"), the "target=" can't seem to find it
        print("Sleeping 1 second...")
        time.sleep(1)
        print("Done Sleeping")
    """

    if __name__ == '__main__':
        p1 = multiprocessing.Process(target=do_something)
        p2 = multiprocessing.Process(target=do_something)

        p1.start()
        p2.start()

        p1.join() # We're using 'join' in order to tell the code to wait until the processes are finished before moving on with the code.
        p2.join()

    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)} second(s)")


def func4():
    """
    Instead of creating large numbers of processes, you can create processes in a loop (or a list comprehension).

    1. print(f"Finished in {round(finish - start, 2)} second(s)")
    This code prints out 0.03 seconds because the just like in the earlier examples, the code assigned processes to the different threads and continued running code before
    the threads were finished. 
    """
    import multiprocessing
    import time

    start = time.perf_counter()

    """
    def do_something(): # Normally, this function would work but because this function is inside of another function ("func4"), the "target=" can't seem to find it
        print("Sleeping 1 second...")
        time.sleep(1)
        print("Done Sleeping")
    """

    if __name__ == '__main__':
        for _ in range(10): # the range of 10 means we are going to have 10 different processes
            p = multiprocessing.Process(target=do_something)
            p.start()

        finish = time.perf_counter()
        print(f"Finished in {round(finish - start, 2)} second(s)") # Footnote 1 (more detail in the multiline comment above


def func5():
    """
    In order to have the code wait for the code to run, we have to append each process to a list and then loop through that list in a different loop and join all the 
    elements/processes.

    The reason why we can't just simply run the 'join' method on the within the original loop because it would run 'join' on the processes before the loop is able to 
    loop through, create, and start the next process in the loop so it would basically be the same as running it synchronously. To combat this, we can append the 
    processes to a list and then joining the processes in a loop because that way, we can start the start all of the processes in one loop and the loop through those 
    processes again and run the join method on them so that they all finish before the end of our script. 

    1. print(f"Finished in {round(finish - start, 2)} second(s)")
    The reason why this program was still able to finish in around 1 second even though the computer doesn't have 20 different cores is because the computer has a way of 
    switching off between cores when one of them isn't too busy. 
    """
    import multiprocessing
    import time
    
    start = time.perf_counter()
    
    """
    def do_something(): # Normally, this function would work but because this function is inside of another function ("func5"), the "target=" can't seem to find it
        print("Sleeping 1 second...")
        time.sleep(1)
        print("Done Sleeping")
    """
    
    processes = [] # We have created an empty list to append all of our processes to

    if __name__ == "__main__":
        for _ in range(20): # the range of 20 means we are going to have 20 different processes
            p = multiprocessing.Process(target=do_something)
            p.start()
            processes.append(p) # We have appended all of our processes into a list

        for process in processes:
            process.join()  # We are joining all the elements/processes inside of the list (going to wait until the process finishes before countinuing on to the rest of the script)

        finish = time.perf_counter()
        print(f"Finished in {round(finish - start, 2)} second(s)") # Footnote 1



"""FOR FUNCTIONS 6"""
def do_something(seconds): # We are taking in a parameter of "seconds"
    import time
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds) # We are now going to sleep for "seconds" (the parameter value) number of seconds
    print("Done Sleeping")
"""FOR FUNCTIONS 6"""



def func6():
    """
    We can also pass in parameters to the functions that we are running with processes.

    In the example below, we are going to pass in a parameter to determine how many seconds we want our function to sleep for.


    1. p = multiprocessing.Process(target=do_something, args=[1.5])
    We can pass in arguments using 'args=' in this line of code but we have to make sure that we pass in the arguments as a list.
    Also, unlike with threads, in order to pass in arguments to a multi-processing process, the arguments must be able to be serialized using pickle. 

    ("Serializing with pickle" basically means that we're converting Python objects into a format that can be deconstructed and reconstructed in another Python script.)
    """
    import multiprocessing
    import time
    
    start = time.perf_counter()
    
    """
    def do_something(seconds): # Normally, this function would work but because this function is inside of another function ("func6"), the "target=" can't seem to find it
        print(f"Sleeping {seconds} second(s)...")
        time.sleep(seconds) 
        print("Done Sleeping")
    """
    
    if __name__ == '__main__':
        processes = [] # We can have the list inside or outside of "if __name__ == '__main__'
        for _ in range(10):
            p = multiprocessing.Process(target=do_something, args=[1.5]) # Footnote 1
            p.start()
            processes.append(p)
    
        for process in processes:
            process.join()
    
        finish = time.perf_counter()
        print(f"Finished in {round(finish - start, 2)} second(s)")


"""FOR FUNCTIONS 7 THROUGH 11"""
def do_something(seconds): # We are taking in a parameter of "seconds"
    import time
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds) # We are now going to sleep for "seconds" (the parameter value) number of seconds
    return("Done Sleeping") # Literally the only difference is between the last "do_something" function and this function is the last line of code is retruned, not printed
"""FOR FUNCTIONS 7 THROUGH 11"""



def func7():
    """
    The newer (and faster) way of multiprocessing

    ProcessPoolExecutor:
    ProcessPoolExecutor was added to Python 3.2 and in a lot of cases, it will be an easier and more efficient way to run multiple processes. It also allows us to easily 
    switch over to using multiple threads instead of processes as well, depending on the problem that we're trying to solve. 

    In order to use the ProcessP00lExecutor, we need to import it from the 'concurrent.futures' module instead of the 'multiprocessing' module


    1. f1 = executor.submit(do_something, 1)
    -  'submit' was one of the methods that we could have used within the "ProcessPoolExecutor". 
    -  The 'submit' method allows us to execute the function ('do_something') once at a time.
    -  The 'submit' method schedules a function to be executed and returns a future object.
    -  A future object basically encapsulates the execution of our function and allows us to check on it after it's been schedule (we can check if it is running, done, and 
    the results of the function (If we grab the results, it will give us the return value of the function))
    -  The parameters that the 'submit' method takes in are the function that we want to run (do_something) and arguments to that function (in this example, that would be 
    'seconds', which determines how many seconds the program should sleep for.
    """
    import concurrent.futures
    import time
    
    start = time.perf_counter()
    
    """
    def do_something(seconds): # Normally, this function would work but because this function is inside of another function ("func7"), the "target=" can't seem to find it
        print(f"Sleeping {seconds} second...")
        time.sleep(seconds)
        return "Done Sleeping" # We are going to return this string so that we can grab it when we call 'result' on the processes (ex. 'f1.result()')
    """

    if __name__ == '__main__':
        with concurrent.futures.ProcessPoolExecutor() as executor:
        #     We can use a couple of different methods that we can use within this statement
            f1 = executor.submit(do_something, 1) # footnote 1
            f2 = executor.submit(do_something, 1)
            # When you use 'result', the code will wait until the function completes.
            print(f1.result()) # We can grab the results using 'result' and it will give us the return value of the function (The result is "Done Sleeping").
            print(f2.result()) # If instead of print, we had return, the return statement will wait until the .result() functions returns something.
    
        finish = time.perf_counter()
        print(f"Finished in {round(finish - start, 2)} second(s)")


def func8():
    """
    In order to have a bunch of processes, we can use a loop (or a list comprehension).

    1. 
    In order to get the results, we can actually use another function from the 'concurrent.futures' module called "as_completed". "as_completed" will give us an iterator
    that we can loop over that will yield the results of our processes as they're completed. 

    2. print(f"Finished in {round(finish - start, 2)} second(s)")
    The reason why this took longer (2 seconds instead of 1 second) is because the ProcessPoolExecutor may have made a decision based on our hardware not to use as 
    many processes.

    3. print(f.result())
    This would print out in the order they were completed, not the order they were started.
    """
    import concurrent.futures
    import time
    
    start = time.perf_counter()
    
    """
    def do_something(seconds): # Normally, this function would work but because this function is inside of another function ("func8"), the "target=" can't seem to find it
        print(f"Sleeping {seconds} second...")
        time.sleep(seconds)
        return("Done Sleeping")
    """
    
    if __name__ == '__main__':
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = [executor.submit(do_something, 1) for _ in range(10)]
    
        for f in concurrent.futures.as_completed(results): # footnote 1
            print(f.result())   # footnote 3
    
        finish = time.perf_counter()
        print(f"Finished in {round(finish - start, 2)} second(s)") # footnote 2


def func9():
    """
    In order to show that that 'result' method prints out the return statement in the order they were completed, we are going to use the example down below (we are going 
    to have the function execute with different number of seconds each time they run and the return statement is going to say how many seconds the function was sleeping).


    1. print(f.result())
    While the quickest process might not end the first (it all depends on how many cores that your computer has and how the ProcessPoolExecutor thinks it should 
    assign the process) but you can still see that the shorter processes were returned and printed (by the result) first and the slower processes were returned and
    printed (by the result) last. 
    """
    import concurrent.futures
    import time
    
    start = time.perf_counter()
    
    """
    def do_something(seconds): # Normally, this function would work but because this function is inside of another function ("func9"), the "target=" can't seem to find it
        print(f"Sleeping {seconds} second...")
        time.sleep(seconds)
        return f"Done Sleeping {seconds}"
    """
    
    if __name__ == '__main__':
        with concurrent.futures.ProcessPoolExecutor() as executor:
            seconds = [5, 4, 3, 2, 1]
            results = [executor.submit(do_something, second) for second in seconds]
    
        for f in concurrent.futures.as_completed(results):
            print(f.result()) # footnote 1
    
        finish = time.perf_counter()
        print(f"Finished in {round(finish - start, 2)} second(s)")


def func10():
    """
    With the 'submit' method, it's submitting each function one at a time but in order to run 'submit' on an entire list, then we need to do a loop or a comprehension like we 
    did in the example above. But if you're familiar with the built-in mpa method, then there is actually something similar that we can do with processes where we can use the 
    map method to run our function over a list of values. In other words, it's very similar to the map method except that is uses processes instead it runs the function 
    everytime or with every item of the integral that we pass in. 

    When we used the 'submit' method, it returned future objects but when we use map, it just returns the results. 
    While 'map' is going to run the processes in parallel, but instead of returning the results as they're competed, like we saw with 'submit' and the old way of writing 
    multiprocesses, the results are going to be returned in the order that they were started.



    1. results = executor.map(do_something, seconds)
    This is how you run the map-like method for processes. 
    What this code is going to do is it basically will run 'do_something' with every item/element of the list 'seconds' (it doesn't have to be a list, it can be any iterable
    you pass in). This is, in short, what 'map' does.


    2. print(result)
    This is how you are to print out the results of the processes through map (you have to print them out through a loop). However, you can see that it waits for every 
    process to end before printing out the results. You can also see that the results printed out in the order that they were started, not in the order they finished. 
    This is because the method 'map' will return the results in the order they were started and therefore print out the results when the result for the first, second, third, 
    fourth, etc. are finished executing (You can see that in the list 'seconds', we have [2, 5, 4, 3, 2, 1]. The first '2' gets printed out before the rest of the code 
    because it got executed first and the second element was '5' seconds, meaning the rest of the code had to wait for the 5 second code to finish executing before they 
    were returned (even though they may have already finished executing).




    IF THE FUNCTION RAISES AN EXCEPTION, IT WON'T ACTUALLY RAISE THAT EXCEPTION WHILE RUNNING THE PROCESS. THE EXCEPTION WILL BE RAISED WHEN ITS VALUE IS RETRIEVED FROM THE 
    RESULTS ITERATOR SO IF YOU NEED TO HANDLE ANY EXCEPTIONS, YOU CAN DO SO IN THE RESULTS ITERATOR.
    """
    import concurrent.futures
    import time
    
    start = time.perf_counter()
    
    """
    def do_something(sec): # Normally, this function would work but because this function is inside of another function ("func10"), the "target=" can't seem to find it
        print(f"Sleeping {sec} second...")
        time.sleep(sec)
        return f"Done Sleeping {sec}"
    """
    
    if __name__ == '__main__':
        with concurrent.futures.ProcessPoolExecutor() as executor: # context manager
            seconds = [2, 5, 4, 3, 2, 1]
            results = executor.map(do_something, seconds) # footnote 1
    
            for result in results:
                print(result) # This is how you print out the results, through a loop                # footnote 2
    
        finish = time.perf_counter()
        print(f"Finished in {round(finish - start, 2)} second(s)")


def func11():
    """
    Now, even if we don't grab our results within the context manager (the 'with concurrent.futures.ProcessPoolExecutor() as executor'), it's still going to automatically
    join all of the processes and let them finish after the context manager ends. 



    1. print(f"Finished in {round(finish - start, 2)} second(s)")
    You can see that the processes didn't move on after assigning the processes and execute (and print) the 'finish' variable before the processes were finished. 
    The context manager still waited for the results to be returned from the processes even without grabbing the results and printing it out. In other words, the 
    context managers are still going to continue and automatically 'join' the processes.
    """
    import concurrent.futures
    import time
    
    start = time.perf_counter()
    
    """
    def do_something(secs): # Normally, this function would work but because this function is inside of another function ("func11"), the "target=" can't seem to find it
        print(f"Sleeping {secs} second...")
        time.sleep(secs)
        return f"Done Sleeping {secs}"
    """
    
    if __name__ == '__main__':
        with concurrent.futures.ProcessPoolExecutor() as executor:
            seconds = [5, 4, 3, 2, 1]
            results = executor.map(do_something, seconds)
    
    # We are going to remove the code that prints out the results
    #         for result in results:
    #             print(result)
    
        finish = time.perf_counter()
        print(f"Finished in {round(finish - start, 2)} second(s)") # footnote 1


def func12():
    """
    Real world examples of multiprocess code

    A photo editing code without using multiprocessing (each photo is downloaded one by one/synchronously)
    """
    import time
    from PIL import Image, ImageFilter  # PIL is the pillow library and it's an image library for Python that makes images processing easy (Make sure you download it using "pip instlal Pillow" (if you have pip) before trying to use it)
    import os

    os.chdir("photos")
    img_names = [ # The photos that were downloaded from the 'threading' Python code
        'photo-1516117172878-fd2c41f4a759.jpg',
        'photo-1532009324734-20a7a5813719.jpg',
        'photo-1524429656589-6633a470097c.jpg',
        'photo-1530224264768-7ff8c1789d79.jpg',
        'photo-1564135624576-c5c88640f235.jpg',
        'photo-1541698444083-023c97d3f4b6.jpg',
        'photo-1524758631624-e2822e304c36.jpg',
        'photo-1513938709626-033611b8cc03.jpg',
        'photo-1507143550189-fed454f93097.jpg',
        'photo-1493976040374-85c8e12f0c0e.jpg',
        'photo-1504198453319-5ce911bafcde.jpg',
        'photo-1530122037265-a5f1f91d3b99.jpg',
        'photo-1628338128143-1b9e187b1441.jpg',
        'photo-1550439062-609e1531270e.jpg',
        'photo-1593642634367-d91a135587b5.jpg'
    ]
    
    t1 = time.perf_counter()
    
    size = (1200, 1200)
    
    for img_name in img_names:
        img = Image.open(img_name)

        img = img.filter(ImageFilter.GaussianBlur(15)) # This might be more of an IO Bound thing rather than a CPU Bound task but the example still works as it is...
    
        img.thumbnail(size)
        img.save(f'processed_images/{img_name}') # we are saving the photo into folder named 'processed' but you need to create it first
        print(f'{img_name} was processed...')
    
    t2 = time.perf_counter()
    
    print(f'Finished in {t2-t1} seconds')


def func13():
    """
    Multiple processes example
    (This example is a good candidate for the 'ProcessPoolExecutor' 'map' method)

    In order to make the code above a multiprocess code, we would have to create a function that will process a single image (and then we can have our 'map' function).


    1. executor.map(process_image, img_names)
    We are going to take in the name of the function and every element in a list of things that we want to execute "executor.map(<function name>, <iterable_name>)"


    If we check the task manager/activity monitor, we are able to see that there are multiple Python processes running (a Python process for each core/process created). 
    When the Python program finishes, then we are able to see that the Python processes disappear as they are no longer in use (and therefore removed)
    """
    import concurrent.futures
    import time
    from PIL import Image, ImageFilter  # PIL is the pillow library and it's an image library for Python that makes images processing easy

    img_names = [ # The photos that were downloaded from the 'threading' Python code
        'photo-1516117172878-fd2c41f4a759.jpg',
        'photo-1532009324734-20a7a5813719.jpg',
        'photo-1524429656589-6633a470097c.jpg',
        'photo-1530224264768-7ff8c1789d79.jpg',
        'photo-1564135624576-c5c88640f235.jpg',
        'photo-1541698444083-023c97d3f4b6.jpg',
        'photo-1524758631624-e2822e304c36.jpg',
        'photo-1513938709626-033611b8cc03.jpg',
        'photo-1507143550189-fed454f93097.jpg',
        'photo-1493976040374-85c8e12f0c0e.jpg',
        'photo-1504198453319-5ce911bafcde.jpg',
        'photo-1530122037265-a5f1f91d3b99.jpg',
        'photo-1628338128143-1b9e187b1441.jpg',
        'photo-1550439062-609e1531270e.jpg',
        'photo-1593642634367-d91a135587b5.jpg'
    ]

    t1 = time.perf_counter()
    size = (1200, 1200)

    def process_image(img_name):  # This is going to take in the image name (represented by the variable 'img_name' as the argument)
        img = Image.open(img_name)

        img = img.filter(ImageFilter.GaussianBlur(15))  # This might be more of an IO Bound thing rather than a CPU Bound task but the example still works as it is...

        img.thumbnail(size)
        img.save(f'processed/{img_name}')  # we are saving the photo into folder named 'processed' but you need to create it first
        print(f'{img_name} was processed...')


    if __name__ == '__main__':
        with concurrent.futures.ProcessPoolExecutor() as executor:
            executor.map(process_image, img_names) # footnote 1

        t2 = time.perf_counter()
        print(f'Finished in {t2-t1} seconds')


    """
    The simple thing about threads and multiprocesses using the concurrent.futures library is that it is easily to switch between the two (all you have to do is to change 
    'ProcessPoolExecutor()' to 'ThreadPoolExecutor()' and vice versa.
    """


func12()