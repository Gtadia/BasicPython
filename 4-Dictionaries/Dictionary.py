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


# type the name of the function that you want to run here
func15()