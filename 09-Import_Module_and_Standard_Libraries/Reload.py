"""
reload() is a method that RELOADS imported/loaded modules. 

This means that libraries that were imported from the standard library or custom libraries will have their cache wiped and 
basically started  anew. 

This can be handy for modules like "logging" where you have to reset the .basicconfig
OR
Maybe you don't need the data that you've stored in a custom module that you've imported and it's just hogging up memory so you 
can just reload it and not give it any more data.


REMEMBER:
For Python2.x
    reload(module)

For above 2.x and <=Python3.3
    import imp
    imp.reload(module)

For >=Python3.4
    import importlib
    importlib.reload(module)
"""

def func1():
    """
    Example Code:
        Reloading the logging module
    """
    import logging
    import importlib

    logging.basicConfig(level=logging.DEBUG)
    print(logging.getLogger(__name__))

    importlib.reload(logging) # reloading the logging module
    print(logging.getLogger(__name__)) # You can see that the level has retruned back to the default value (WARNING)



func1()