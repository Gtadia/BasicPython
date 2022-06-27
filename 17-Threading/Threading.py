"""
https://youtu.be/IEEhzQoKtQU

Threading

Basically, we want to use threading whenever it's going to significantly speed up our program. This speed up comes from running different tasks concurrently.

How threading works:
When we run something concurrently using threads, it's not going to run the code at the same time, it just gives the illusion of running code at the same time because
when it comes to a point where it's just waiting around, it's just going to go ahead and move forward with the script and run other code while the I/O operations finish.

For example, when we run the 'do_something' function twice, the program is going to have to wait for the function to finish waiting one by one. So, instead of waiting
for the program to finish loading/waiting, the program will run another function after the first function is finished processing while we wait for the 1 second sleep
to be finished.


CPU Bound tasks:
Processes that are crunching a lot of numbers and using the CPU

I/O Bound tasks:
Processes that are just waiting for input and output operations to be completed and not really using the CPU all that much.
Another example of I/O Bound tasks are reading and writing from the file system and other filesystem operations, network operations, downloading stuff online, etc.

When we are threading, we are going to see benefits when our tasks are I/O bound.

We would want to use mutliprocessing to run CPU Bound tasks so that these computationally hard tasks run in parallel of each other in order to get computing time benefits.
(We wouldn't get much of a benefit running CPU Bound tasks with threading because those tasks are still bound to a single thread)
(If we try to use threads on CPU Bound tasks, we might actually slow the program down because creating and destroying the threads have some overhead (take up
computational power).)
"""

def func1():
    """
    An example of why we would want to use threading

    Without threading, the program starts the first do_something function, waits one second/does nothing/wastes time until it's finished and then run the next do_something function.
    (Check out the "Without_Threading.png" picture in this file to get a visual of how this function is running without threading)
    
    Running everything in order like this is called running a program "synchronously."  
    """
    import time # We are just using the "time" library in order to 1) sleep/make the functions wait for 1 second, and 2) get the start and end time in order to determine how long the program ran for.

    start = time.perf_counter() # This gets the time of when the function was run

    def do_something():
        print('Sleeping 1 second...')
        time.sleep(1)
        print('Done Sleeping...')

    do_something()
    do_something() # 

    finish = time.perf_counter() # this gets the time when the function finishes running

    print(f'Finished in {round(finish-start, 2)} second(s)') # We subtracted the end when the program ended with the time when the program began, resulting in the total run-time


def func2():
    """
    Threading is when the program just goes ahead and starts running other code when the function/computation that it was just running is waiting around (such as waiting
    for an input). This way, it gives other functions an opportunity to run while the current/previous functions finish their I/O operations.
    (Check out the "With_Threading.png" picture in this file to get a visual of how this function is running without threading)


    This is the old way of threading
    """
    import threading # You need to import the threading module to have python run functions/programs with threads
    import time

    start = time.perf_counter()

    def do_something():
        print('Sleeping 1 second...')
        time.sleep(1)
        print('Done Sleeping...')

    t1 = threading.Thread(target=do_something) # the 'target' is the function that we want to run (we only want to pass in the funciton, not execute it)
    t2 = threading.Thread(target=do_something)

    # Just setting up threads like this won't run it. So you need to use the 'start' method on each thread in order to get it to run.
    t1.start()
    t2.start() # There is a problem with this. You can see that the program says it finished in 0 seconds when it actually took around 1 second.
    # The reason for this is because when the threads were finished running, the program continued on concurrently and executing the rest of the program (and therefore ran the 'finish' variable and the print statement that prints out the time). ALl of this was done while the threads were still sleeping.

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)') # Says that the function finished running in 0 seconds, which isn't true




def func3():
    """
    In order to have our threads finish BEFORE we execute the 'finish' variable and print the result, we just need to run the 'join()' method on each thread after the 
    'start()' method. The 'join()' method on each of the threads states that the thread need to complete before moving on to calculate anything else that are not threads 
    (which in this case are the finish times).
    """
    import threading
    import time

    start = time.perf_counter()

    def do_something():
        print('Sleeping 1 second...')
        time.sleep(1)
        print('Done Sleeping...')

    t1 = threading.Thread(target=do_something)
    t2 = threading.Thread(target=do_something)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} second(s)") # Correctly prints out that the program terminates after 1 second.


def func4():
    """
    If you want to run multiple threads easily (instead of creating them manually), you can run use a loop.
    """
    import threading
    import time

    start = time.perf_counter()

    def do_something():
        print('Sleeping 1 second...')
        time.sleep(1)
        print('Done Sleeping...')

    threads = []

    for _ in range(10): # An underscore ('_') means that it is a throwaway variable (not using it, because we just want to loop a certain number of times and not store things)
        # print(_) # You can, however, still call on the underscore ('_') to print it out. It's just a common practice that people use, not an actual built-in thing.
        t = threading.Thread(target=do_something)
        t.start()
        threads.append(t)
    #   We can't really do a 't.join()' in a loop because it would join on the thread before looping through, creating, and starting the next thread (so it would basically be the same as running the code synchronously). So, we would need a way that we can start all of the threads in one loop. Then, we need to loop through the thread again and run the join method on them so that they all finish before the end of the script.
    #   In order to do this, we can append each thread that we created to a list of threads. In other words, we can create an empty list of threads above the loop (ex: 'threads = []') and then append threads into it (ex: 'threads.append(t)').

    #   Finally, we create a new loop that loops through the 'threads' list and run 'join()' on all of the elements of that list
    for thread in threads:
        thread.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')


def func5():
    """
    How to pass arguments into threads

    In the example below, we are going to pass in a parameter to determine how long the threads should sleep into the function that is going to be threaded.
    """
    import threading
    import time

    start = time.perf_counter()

    def do_something(seconds): # are adding the parameter here
        print(f'Sleeping {seconds} second(s)...')
        time.sleep(seconds)
        print('Done Sleeping...')

    threads = []
    for _ in range(10):
        t = threading.Thread(target=do_something, args=[1.5]) # You can see that we pass in the values to the parameter through 'args=' and we pass the values in a list
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()


    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')


def func6():
    """
    THE NEW WAY OF EXECUTING THREADS
    The "thread pool" executor is this new way of executing threads (they were introduced in Python 3.2)
        - An easier and more efficient way of running threads
        - Allows us to easily switch over to using multiple processes instead of threads as well (depending on the problem that we're trying to solve/execute)

    What we need to do is to import 'concurrrent.futures' (and we don't even need the import threading statement anymore)

    When we use the thread pool executors, it's usually best to use this with a context manager
    """
    import concurrent.futures
    import time

    start = time.perf_counter()


    def do_something(seconds):
        print(f"Sleeping {seconds} second(s)...")
        time.sleep(seconds)
        return "Done Sleeping..." # making this a return value and not a print so that we can grab it


    """
    The submit method schedules a function to be executed and returns a future object
    A future object basically encapsulates the execution of our function and allows us to check in on it after it's been scheduled so we can 
    check that it's running or if it's done, or the result. So, if we grabbed a result, then it'll give us the return value of the function.
    """
    with concurrent.futures.ThreadPoolExecutor() as executor: # context manager
        f1 = executor.submit(do_something, 1) # Takes in a function and an argument for the parameters (in that order)
        print(f1.result()) # We are telling 'f1', which is executing 'do_something', to grab the return statement (which is returning 'Done Sleeping...").
        # The 'result()' method will actually wait around until the function completes.

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)...")


def func7():
    """
    You can see that the new way of executing threads are a lot shorter than running threads the old way. 

    If you, however, wanted to run multiple threads on the new method, all you have to do is to run the 'sumbit' method mutliple times
    """
    import concurrent.futures
    import time

    start = time.perf_counter()


    def do_something(seconds):
        print(f"Sleeping {seconds} second(s)...")
        time.sleep(seconds)
        return "Done Sleeping..."

    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(do_something, 1) # The '1' is the arguments that the 'do_something' function takes in (so in other words, the program will run for 1 second)
        f2 = executor.submit(do_something, 1)

        print(f1.result())
        print(f2.result()) # You can see that this is how to run multiple threads

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)...")


def func8():
    """
    Instead of calling the different threads manually, you could use a loop (like the old method) but you could also use a list comprehension.
    """
    import concurrent.futures
    import time

    start = time.perf_counter()


    def do_something(seconds):
        print(f"Sleeping {seconds} second(s)...")
        time.sleep(seconds)
        return "Done Sleeping..."

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(do_something, 1) for _ in range(10)]
        for f in concurrent.futures.as_completed(results): # "as_completed" is notified when a thread is completed and will immediately yeidl to teh finished future/thread and run the code within in local environment, which in this case is the print statement
            print(f.result())
            
    """
    'as_completed' is a function from the 'concurrent.futures' and it will give us an iterator that we can loop over that will yield the 
    results of our threads as they are completed.

    In short, you use this function to get the results of the threads.
    """

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")


def func9():
    """
    To show that the 'as_completed' function is yielding the results are they are completed, we have created an example to demonstrate it (We'll create a list of seconds to 
    sleep 
    """
    """
    The 'submit' method submits each function once at a time. So, in order run 'submit' on an entire list, then we would need to do a loop or a comprehension like we did 
    in the example above. 
    However, if you are familiar with the built-in 'map' method, you can that we can use a map method to run our function over a list of values. We can use this with our 
    threads as well. 
    """

    import concurrent.futures
    import time

    start = time.perf_counter()


    def do_something(seconds):
        print(f"Sleeping {seconds} second(s)...")
        time.sleep(seconds)
        return f"Done Sleeping...{seconds}"

    with concurrent.futures.ThreadPoolExecutor() as executor:
        seconds = [5, 4, 3, 2, 1]
        # Below, we are looping through the elements in the list 'seconds' and we are passing the different elements ('sec') as parameters for the 'do_something' function.
        results = [executor.submit(do_something, sec) for sec in seconds]
        for f in concurrent.futures.as_completed(results):
            print(f.result())

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")


def func10():
    import concurrent.futures
    import time

    start = time.perf_counter()


    def do_something(seconds):
        print(f"Sleeping {seconds} second(s)...")
        time.sleep(seconds)
        return f"Done Sleeping...{seconds}" # making this a return value and not a print so that we can grab it

    with concurrent.futures.ThreadPoolExecutor() as executor:
        seconds = [5, 4, 3, 2, 1]
        results = executor.map(do_something, seconds) # When we used the 'sumbit' method, it returned a future object. When we use 'map', it instead returns the results.
    # While it returns the results, it is going to run the threads concurrently but instead of running the results as they complete (like we saw before), map is going to return the results and the order that they started.
    # Also, "map" automatically joins everything so it will sitll wait until everything in the program finishes before continuing
        for result in results:
            print(result)

    """
    Instead of getting the results back in the order that they finish (the 1 second operation finishing first and the 5 second operation last), map will wait until every 
    thread is finished executing and then return them in the order they were started (so in this example, the 5 second operation is displayed first and the 1 second operation
    is displayed next).
    """
    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")

    """
    If one of our functions raises an exception, it won't actually raise the exception while running the thread. The exception will be raised when its value is retrieved from 
    the results iterator so if you need to handle exception, then you can do that within the iterator. 
    """


def func12():
    """
    The multi-thread concurrent executor will still run and still wait for the results to finish executing before continuing even though you don't print out the results
    """
    import concurrent.futures
    import time

    start = time.perf_counter()


    def do_something(seconds):
        print(f"Sleeping {seconds} second(s)...")
        time.sleep(seconds)
        return "Done Sleeping..." # making this a return value and not a print so that we can grab it

    with concurrent.futures.ThreadPoolExecutor() as executor:
        seconds = [5, 4, 3, 2, 1]
        results = executor.map(do_something, seconds)

        # We're not going to print out the results
        # for result in results:
        #   print(result)

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")


def func13part1():
    """
    A real-world practical example

        Downloading images one by one as it waits for the entire image to download before it moves on to the next image.
    """

    """
    This is how people would do it without threading
    """
    import requests # Allows us to get data form online sources 
    import time
    import os

    img_urls = [ 
        'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
        'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
        'https://images.unsplash.com/photo-1524429656589-6633a470097c',
        'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
        'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
        'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
        'https://images.unsplash.com/photo-1524758631624-e2822e304c36',
        'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
        'https://images.unsplash.com/photo-1507143550189-fed454f93097',
        'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
        'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
        'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
        'https://images.unsplash.com/photo-1628338128143-1b9e187b1441',
        'https://images.unsplash.com/photo-1550439062-609e1531270e',
        'https://images.unsplash.com/photo-1593642634367-d91a135587b5'
    ]

    os.chdir("photos") # Changing the directory so that the photos download in a different folder


    t1 = time.perf_counter()

    for img_url in img_urls:
        img_bytes = requests.get(img_url).content
        img_name = img_url.split('/')[3] # Takes "photo-1......." because that's the fourth thing after the split
        img_name = f"{img_name}.jpg"
        with open(img_name, 'wb') as img_file:
            img_file.write(img_bytes)
            print(f"{img_name} was downloaded...")

    t2 = time.perf_counter()
    print(f"Finished in {round(t2-t1, 2)} second(s)")


def func13part2():
    """
    This is how people would do it after threading

        It will start downloading the image and move onto the next image while the first image is pulling the data to download the image.
    """
    import concurrent.futures
    import requests
    import time
    import os

    img_urls = [
        'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
        'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
        'https://images.unsplash.com/photo-1524429656589-6633a470097c',
        'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
        'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
        'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
        'https://images.unsplash.com/photo-1524758631624-e2822e304c36',
        'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
        'https://images.unsplash.com/photo-1507143550189-fed454f93097',
        'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
        'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
        'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
        'https://images.unsplash.com/photo-1628338128143-1b9e187b1441',
        'https://images.unsplash.com/photo-1550439062-609e1531270e',
        'https://images.unsplash.com/photo-1593642634367-d91a135587b5'
    ]

    t1 = time.perf_counter()

    os.chdir("photos") # Changing the directory so that the photos download in a different folder

    def download_image(img_url): # We changed the for loop into a function.
        img_bytes = requests.get(img_url).content
        img_name = img_url.split('/')[3]
        img_name = f"{img_name}.jpg"
        with open(img_name, 'wb') as img_file:
            img_file.write(img_bytes)
            print(f"{img_name} was downloaded...")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls) # This will run the "download_image" function and for every element in the 'img_urls' list and then create new threads to run these elements through the 'download_image' function.

    t2 = time.perf_counter()
    print(f"Finished in {round(t2 - t1, 2)} second(s)")



# Type the name of the function that you want to run
func13part1()