"""
https://youtu.be/daefaLgNkw0

Dictionary: Allows us to work with key-value pairs in Python (a.k.a, Hashmap or associative arrays)
Key-value pairs are two linked values where the KEY is a unique identifier where we can find our data and the
VALUE is that data.

For example, the words in a real life dictionary are the keys and their definitions are the data.
"""

def func1():
    dictionary = dict() # You can start an empty dictionary with "dict()"
    dictionary = {} # Or ou can start a dictionary with curly backets


def func2(): 
    # This is how to make a dictionary and how to call the values using keys
    Cars = {"Model": "WRX STI", "Manufacturer": "Suburu", "Year": 2005, "Designed For": ["Rally", "Off-Roading", "Daily-Diver"]}
    print(Cars["Model"])
    print(Cars["Designed For"])


def func3():
    # The key and the value can be nearly any data type (For example, we can't have a data collection (e.g., a list) be a key)
    Random_Dict = {1: True, False: "Monkeys", "?": 23456.5}
    print(Random_Dict[1])
    print(Random_Dict[False])
    print(Random_Dict["?"])


def func4():
    # A "KeyError" will be thrown if we try to access a key that does not exist
    Cars = {"Model": "WRX STI", "Manufacturer": "Suburu", "Year": 2005, "Designed For": ["Rally", "Off-Roading", "Daily-Diver"]}
    print(Cars["Price"])


def func5():
    # However, if we instead used the ".get()" method, we can just print out "none" (or something else) instead of an error being thrown
    Cars = {"Model": "WRX STI", "Manufacturer": "Suburu", "Year": 2005, "Designed For": ["Rally", "Off-Roading", "Daily-Diver"]}
    print(Cars.get("Model")) # Getting values that exists still works as normal
    print(Cars.get("Price")) # Returns "none" instead of an error being thrown
    print(Cars.get("Horsepower", "Key-Not-Found")) # We can choose the value that we want to be returned when a key does not exist


def func6(): 
    # With dictionaries, we can change the values stored under a certain key
    Cars = {"Model": "WRX STI", "Manufacturer": "Suburu", "Year": 2005, "Designed For": ["Rally", "Off-Roading", "Daily-Diver"]}
    Cars["Year"] = 2022
    print(Cars.get("Year"))


def func7(): 
    # We can also change the values stored in dictionaries using the "update" method
    # This method is especialy useful when we want to update multiple values at a time
    Cars = {"Model": "WRX STI", "Manufacturer": "Suburu", "Year": 2005, "Designed For": ["Rally", "Off-Roading", "Daily-Diver"]}
    Cars.update({'Model': "Supra", "Year" : 2021, "Manufacturer": "Toyota", "Price": 50000}) # As you can also see, you can new keys and values using the update function
    print(Cars)


def func8(): 
    # You can delete a key-value using "del"
    Cars = {"Model": "WRX STI", "Manufacturer": "Suburu", "Year": 2005, "Designed For": ["Rally", "Off-Roading", "Daily-Diver"]}
    del Cars["Designed For"]
    print(Cars)


def func9(): 
    # You can also delete a key-value pair using ".pop(<key>)" (".pop()" doesn't remove the last key-value pair in a dictionary)
    Cars = {"Model": "WRX STI", "Manufacturer": "Suburu", "Year": 2005, "Designed For": ["Rally", "Off-Roading", "Daily-Diver"]}
    popped_Model = Cars.pop("Model")
    print(Cars)
    print(popped_Model)


def func10(): 
    # Use the "len()" function print out length/number of key-value pairs that a dictionary has
    Cars = {"Model": "WRX STI", "Manufacturer": "Suburu", "Year": 2005, "Designed For": ["Rally", "Off-Roading", "Daily-Diver"]}
    print(len(Cars))


def func11():
    # The ".keys()" function returns all of the keys that a dictionary has
    Cars = {"Model": "WRX STI", "Manufacturer": "Suburu", "Year": 2005, "Designed For": ["Rally", "Off-Roading", "Daily-Diver"]}
    print(Cars.keys())


def func12():
    # The ".values()" function returns all of the values that a dictionary has
    Cars = {"Model": "WRX STI", "Manufacturer": "Suburu", "Year": 2005, "Designed For": ["Rally", "Off-Roading", "Daily-Diver"]}
    print(Cars.values())


def func13():
    # The ".items()" function returns both the keys and values
    Cars = {"Model": "WRX STI", "Manufacturer": "Suburu", "Year": 2005, "Designed For": ["Rally", "Off-Roading", "Daily-Diver"]}
    print(Cars.items())


def func14():
    # If you create a simple for-each loop with a dictionary, the keys are returned
    Cars = {"Model": "WRX STI", "Manufacturer": "Suburu", "Year": 2005, "Designed For": ["Rally", "Off-Roading", "Daily-Diver"]}
    for random_key_variable_name in Cars:
        print(random_key_variable_name)


def func15():
    # However, if you wanted to loop through the values or both keys and values, you have to do the following
    Cars = {"Model": "WRX STI", "Manufacturer": "Suburu", "Year": 2005, "Designed For": ["Rally", "Off-Roading", "Daily-Diver"]}
    for rand_keys, rand_values in Cars.items(): # REMEMBER: Keys are first then values
        print(rand_keys, "\t", rand_values)


"""
A dictionary is a data collection type that is unordered and mutable.
It consists of a collection key value pairs (Like the word and the definition in a dictionary)
The keys (keywords) cannot have duplicates.
The values (definition) can have duplicates.
"""

def func16():
    # When using dict() instead of {}, you don't have to put quotes around the keywords
    mydict2 = dict(name="Mary", age=27, city="Boston")
    print(mydict2)

    value = mydict2["city"]
    print(value)


def func17():
    # We can add a new key, value pair to a dictionary
    mydict = {"name": "Max", "age": 28, "city": "New York"}
    mydict["email"] = "max@zyx.com"
    print(mydict)


def func18():
    # If we create a new key value pair but the key already exists, the previous key value pair will be overwritten
    mydict = {"name": "Max", "age": 28, "city": "New York"}
    mydict["name"] = "Min"
    print(mydict)


def func19():
    # We can remove/pop the last item in a dictionary with the .popitem() method
    mydict = {"name": "Max", "age": 28, "city": "New York"}
    mydict.popitem()
    print(mydict)


def func20():
    # We can check if a key is in the dictionary with an "if, in" statement or with the "try, except" statement
    mydict = {"name": "Max", "age": 28, "city": "New York"}
    if "city" in mydict: # The if, in statement in python
        print(mydict["city"])


def func21():
    # We can loop through all the dictionary keys
    mydict = {"name": "Max", "age": 28, "city": "New York"}
    for i in mydict:
        print(i)


def func22():
    # If you want to make a copy of the dictionary, you can just make another variable equal to the dictionary but any changes you make to the copy will change the original as well (so it's not really a copy)
    mydict = {"name": "Max", "age": 28, "city": "New York"}
    mydict_copy = mydict
    print(mydict_copy)
    mydict_copy["school"] = "MIT"
    print(mydict_copy)
    print(mydict) # You can see that both the "copy" and the original are modified

    # How to make a TRUE copy of a dictionary that is independent from the original dictionary by using .copy()
    mydict = {"name": "Max", "age": 28, "city": "New York"}
    mydict_copy = mydict.copy()
    mydict_copy["school"] = "MIT"
    print(mydict)
    print(mydict_copy) # You can see that the copy changed but the original copy didn't


def func23():
    # You can also make a TRUE copy of a dictionary that is independent from the original dictionary by using dict()
    mydict = {"name": "Max", "age": 28, "city": "New York"}
    mydict_copy = dict(mydict)
    mydict_copy["schools"] = "MIT"
    print(mydict)
    print(mydict_copy)


def func23():
    # You can use any immutable types of data as a key in dictionaries
    # For example, you can use numbers or even tuples (the tuples work if it contains only immutable elements)
    my_dict = {3: 9, 6: 36, 8: 84, 9: 81}
    print(my_dict)
    value = my_dict[3] # We are finding for the key "3"
    print(value)

    # Using tuples as a key
    mytuple = (8, 7)
    mydict = {mytuple: 15}
    print(mydict)


def func24():
    # You cannot use a list as a key in a dictionary
    mylist = [8, 7]
    mydict = {mylist: 15}  # This will throw an error



# type the name of the function that you want to run here
func15()