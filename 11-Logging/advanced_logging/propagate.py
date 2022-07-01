"""
https://stackoverflow.com/questions/18058817/python-logging-propagate-messages-of-level-below-current-logger-level
    answered by Udesh Ranjan
"""

"""
If this attribute evaluates to true, events logged to this logger will be passed to the handlers of higher level (ancestor) 
loggers, in addition to any handlers attached to this logger. Messages are passed directly to the ancestor 
loggers/' handlers - neither the level nor filters of the ancestor loggers in question are considered.

If this evaluates to false, logging messages are not passed to the handlers of ancestor loggers.
"""

def func1():
    """Disabling the propagate message"""
    import logging

    handler = logging.StreamHandler()

    parent = logging.getLogger("parent")
    parent.addHandler(handler)
    child = logging.getLogger("parent.child")
    child.propagate = False

    child.setLevel(logging.DEBUG)
    child.addHandler(handler)

    child.info("HELLO")


    """
    OUTPUT:
    HELLO
    """


def func2():
    """Code without disabliing the propagate message"""
    import logging

    handler = logging.StreamHandler()

    parent = logging.getLogger("parent")
    parent.addHandler(handler)
    child = logging.getLogger("parent.child")
    # child.propagate = False

    child.setLevel(logging.DEBUG)
    child.addHandler(handler)

    child.info("HELLO")


    """
    OUTPUT:
    HELLO
    HELLO
    """



# type the name of the function that you want to run here
func2()

"""
By default, the logger is called the 'root' logger. If you want to log in different modules, then it's best practice to not 
use the root logger, but to create your own logger in your modules (create a new python file).


When I create a custom logger, you are creating a hierarchy of loggers. You start with the "root" logger and all the new loggers get added to this hierarchy it will
propagate (to cause to spread out and affect a greater number or greater area : extend.) to the base logger.
So if you import the "helper" module that we created again but disable propagate (make propagate = False), you won't see the log from helper because it won't 
propagate/extend to base logger in this python file (loggingPython.py)
"""