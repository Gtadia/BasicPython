"""
https://youtu.be/jCzT9XFZ5bw

Property Decorators
    This allos us to give our class attributes (getters, setters, and deleters).

Property decorators allows us to define a method but we can access like an attribute.

@property                    getters
@<method name>.setter        setters
@<method name>.deleter       deleter
"""

def func1():
    """
    Explaining why we would want getters, setters, and deleters
    """
    class Employee:
        def __init__(self, first_name, last_name):
            self.first = first_name 
            self.last = last_name
            self.email = f"{self.first[0]}{last_name}@email.com"

        def fullname(self):
            return f"{self.first} {self.last}"

    
    emp_1 = Employee("Jonathan", "Moose")

    # When you print out the attributes and the results of the methods in class instance, we can see that they print out as we would expect them to
    print(emp_1.first)
    print(emp_1.email)
    print(emp_1.fullname())

    # However, when we change one of the attributes, such as the first name, some of the results are not what we would expect
    emp_1.first = "Newton"

    print(emp_1.first)
    print(emp_1.email) # since the constructor/__init__ method only runs once, it doesn't change when we update some of the data (it would have returned "NMoose@email.com" but it still prints out "JMoose@email.com")
    print(emp_1.fullname()) # Since the fullname method runs everytime we call it, it is able to grab the new attributes and return the correct results accordingly


def func2():
    # We can resolve the issue mentioned in func1 by making "email" a method
    class Employee:
        def __init__(self, first_name, last_name):
            self.first = first_name 
            self.last = last_name
            # We removed "self.email" from the constructor 

        def fullname(self):
            return f"{self.first} {self.last}"

        def email(self):
            return f'{self.first[0]}.{self.last}@email.com'


    emp_1 = Employee("Jimmy", "Neutron")


   # Now we are able to change attributes and have the changes applied to "email" as well
    emp_1.first = "Newton"

    print(emp_1.first)
    print(emp_1.email()) # "email" is now a method so we need the parentheses
    print(emp_1.fullname())


def func3():
    """
    We could also resolve the issue mentioned in func1 by using getter and setters like Java. 
    However, in Python, we have property decorators.
    """
    class Employee:
        def __init__(self, first_name, last_name):
            self.first = first_name 
            self.last = last_name
            # An attribute and a method can have the same name but once the method has a property decorator, they can't share the same name anymore or else an "AttributeError" will be thrown

        @property # "@property" are (essentially) getters in Python
        def fullname(self):
            return f"{self.first} {self.last}"

        @property # This is now a property decorator, which means that we can define "email" as a method in the class but we're able to access it like an attribute  
        def email(self):
            return f'{self.first[0]}.{self.last}@email.com'

        
    emp_1 = Employee("Jimmy", "Johns")

    print(emp_1.email) # This returns the results from the "email" method even enough it's formatting suggests that it's an attribute
    print(emp_1.fullname)


def func4():
    """
    How to "technically" make setters 
    """
    class Employee:
        def __init__(self, first_name, last_name):
            self.first = first_name 
            self.last = last_name

        @property
        def fullname(self):
            return f"{self.first} {self.last}"

        @property 
        def email(self):
            return f'{self.first[0]}.{self.last}@email.com'

        
        def fullname_setter(self, name): # This "setter" changes the first and last name
            first, last = name.split(" ") # This splits the full name string into two individual string variables
            self.first = first
            self.last = last


    emp_1 = Employee("Jimmy", "Neutron")
    print(emp_1.fullname)

    emp_1.fullname_setter("New Name")
    print(emp_1.fullname) # You can see that the name has been changed


def func5():
    """
    The proper way of making setters
    """
    class Employee:
        def __init__(self, first_name, last_name):
            self.first = first_name 
            self.last = last_name

        @property
        def fullname(self):
            return f"{self.first} {self.last}"

        @property 
        def email(self):
            return f'{self.first[0]}.{self.last}@email.com'

        @fullname.setter # This property decorator lets the "fullname" method have a setter version of itself
        def fullname(self, name): # The property decorator and the method should have the same method name
            first, last = name.split(" ") # This splits the full name string into two individual string variables
            self.first = first
            self.last = last

        
    emp_1 = Employee("Jimmy", "Neutron")
    print(emp_1.fullname)

    emp_1.fullname("New Name")
    print(emp_1.fullname) # You can see that the name has been changed


def func6():
    """
    Just like how we made our setter method, we can also make a deleter method in the same way

    For example, let's say that we want to make a method that deletes the full name of our employee
    """
    class Employee:
        def __init__(self, first_name, last_name):
            self.first = first_name 
            self.last = last_name

        @property
        def fullname(self):
            return f"{self.first} {self.last}"

        @property 
        def email(self):
            return f'{self.first[0]}.{self.last}@email.com'

        @fullname.deleter
        def fullname(self):
            self.first = None
            self.last = None
            print("Name Deleted")


    emp_1 = Employee("Google", "Chrome")
    print(emp_1.fullname)

    del emp_1.fullname # This runs the fullname deleter method
    print(emp_1.fullname)

# type the name of the function that you want to run here
func6()
