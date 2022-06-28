"""
https://youtu.be/9N6a-VLBa2I

Working with JSON data using the json module.

JSON = JavaScript Object Notation       # Was inspired by JavaScript but is now independent of any one language
    - Very common data format for storing some information.
    - Commonly used when fetching data from online APIs.
    - Also used for configuration files and different kinds of data that can be saved on your local machine.
"""

def func1():
    """
    Introduction to JSON
    """
    import json

    # The following "people_string" is a string that happens to be JSON compatiable/valid JSON,
# The following JSON file (in string format) has a key called "people" and the value of people is an array consisting of 2 objects and each object has a key of "name", "phone", "emails", and "has_license" 
# In other words, this a string of JSON code
    people_string = """
    {
        "people": [
            {
                "name": "John Smith",
                "phone": "615-555-7164",
                "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
                "has_license": false
            }, 
            {
                "name": "Jane Doe",
                "phone": "560-555-5153",
                "emails": ["janedoe@bogusemail.com", "jane.doe@work-place.com"],
                "has_license": true
            }
        ]
    }
    """

    # We can load this string into a Python objet so that we can work with the data more easily
    # In order to load "people_string" into Python from a string, we can use the "json.loads(people_string)"
    data = json.loads(people_string)
    
    print(data) # Returns the dictionary with a key of "people" and a value of a list of 2 dictionaries
    print(type(data)) # Just as proof, we can see that this is actually a dictionary


def func2():
    """
    When we load JSON into a Python object, it uses the following conversion table to convert from JSON to Python.
    We call this serialization or encoding.

    Python           VS     JSON
    dict             |      object 
    list             |      array 
    str              |      string
    int              |      number (int)
    float            |      number (real)
    True             |      true
    False            |      false
    None             |      null

    For example, a JSON object would be converted into a Python dictionary, a JSON array would be converted into a Python list,
    etc.  
    """
    import json

    people_string = """
    {
        "people": [
            {
                "name": "John Smith",
                "phone": "615-555-7164",
                "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
                "has_license": false
            }, 
            {
                "name": "Jane Doe",
                "phone": "560-555-5153",
                "emails": ["janedoe@bogusemail.com", "jane.doe@work-place.com"],
                "has_license": true
            }
        ]
    }
    """

    data = json.loads(people_string)
    
    print(data) # Notice how the things like the blooean values for "has_license" has changed from lowercase "true" to uppercase "True"


def func3():
    """
    Once we convert the JSON data (in string format) to Python, we are able to use it like a regular python dictionary, list, string, int, etc.
    """
    import json

    people_string = """
    {
        "people": [
            {
                "name": "John Smith",
                "phone": "615-555-7164",
                "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
                "has_license": false
            }, 
            {
                "name": "Jane Doe",
                "phone": "560-555-5153",
                "emails": ["janedoe@bogusemail.com", "jane.doe@work-place.com"],
                "has_license": true
            }
        ]
    }
    """

    data = json.loads(people_string) # We can now use "data" like it's a regular dictionary in Python
    
    for individuals in data["people"]:
        print(individuals["name"])
        print(individuals["phone"])


def func4():
    """
    We can convert a Python file back into JSON, even after we modified it in Python first before converting it to JSON (as a Python string).
    
    We can covnert Python back into a JSON (as a string in Python) using "json.dumps(<variable>)".
    """
    import json

    people_string = """
    {
        "people": [
            {
                "name": "John Smith",
                "phone": "615-555-7164",
                "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
                "has_license": false
            }, 
            {
                "name": "Jane Doe",
                "phone": "560-555-5153",
                "emails": ["janedoe@bogusemail.com", "jane.doe@work-place.com"],
                "has_license": true
            }
        ]
    }
    """

    data = json.loads(people_string)

    for person in data["people"]:
        del person["emails"] # We are modifying the dictionary by deleteing stuff from it
    
    new_string = json.dumps(data) # This converts the "data" dictionary without the "phone" key (because it was deleted) as a JSON (as a python multiline string)
    print(new_string) # Just printing out the JSON version


def func5():
    """
    When we convert from Python to JSON, it doesn't indent the code unless we tell it to.

    In order to have the JSON version of python code be indented, we can type "indent = <number of times to indent">" inside of "json.dumps()"
        "json.dumps(<variable/python_code>, indent=<# of indents>)"
    """
    import json

    people_string = """
    {
        "people": [
            {
                "name": "John Smith",
                "phone": "615-555-7164",
                "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
                "has_license": false
            }, 
            {
                "name": "Jane Doe",
                "phone": "560-555-5153",
                "emails": ["janedoe@bogusemail.com", "jane.doe@work-place.com"],
                "has_license": true
            }
        ]
    }
    """

    data = json.loads(people_string)
    
    new_string = json.dumps(data, indent=1) # adds only one indent for every line that needs that indent
    print(new_string)
    

def func6():
    """
    You can sort the keys (sorting the keys in alphabetical order)
        Another thing you can do to clean up your JSON when dumping it to a string. 

    "json.dumps(<variable>, sort_keys=<boolean value>)"
    """
    import json

    people_string = """
    {
        "people": [
            {
                "name": "John Smith",
                "phone": "615-555-7164",
                "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
                "has_license": false
            }, 
            {
                "name": "Jane Doe",
                "phone": "560-555-5153",
                "emails": ["janedoe@bogusemail.com", "jane.doe@work-place.com"],
                "has_license": true
            }
        ]
    }
    """

    data = json.loads(people_string)
    
    new_string = json.dumps(data, indent=2, sort_keys = True)
    print(new_string)


def func7():
    """
    How to load JSON files into Python objects and then write those Python objects back into JSON files

    If we wanted to load the "states.json" file into a Python object, then we can use the "json.load" method. 


    THE DIFFERENCE BETWEEN "json.loads" and "json.load" 
        - .loads        =           loads a string into a Python object
        - .load         =           loads a JSON file into a Python object
    """
    import json
    
    with open("states.json") as file_object: 
        data = json.load(file_object) 

    for a_state in data["states"]:
        print(a_state["name"], a_state["abbreviation"])

    print(type(data)) # You can see that this is stored as a dictionary (or it could be stored as any other object, just not in this case) (REMEMBER: JSON objects = Python dictionaries)
    


def func8():
    """
    We can also write Python objects out into a JSON file.

    THE DIFFERENCE BETWEEN "json.dumps" and "json.dump" 
    - .dumps        =           dumps a Python object into a string
    - .dump         =           dumps a Python object into a JSON file


    "json.dump(<Python Ojbect that you want to convert>, <the file that you want to dump to>)
    """
    import json

    with open("states.json") as f:
        data = json.load(f)

    with open("new_states.json", "w") as f: # We are opening/creating a new file to write the Python-to-JSON-conversion to
        json.dump(data, f, sort_keys=True, indent=5) # indent and sort_keys also works


def func9():
    """
    A Real-World Example

    Since it's pretty common for websites to return JSON from their APIs (because it's easy to parse), our real-world 
    example is going to do exactly that.
    """
    import json
    from urllib.request import urlopen # built-in/standard library module

    with urlopen("http://date.jsontest.com") as response:
        source = response.read()

    data = json.loads(source)
    print(json.dumps(data, indent=2)) # Since just straight up returning the JSON file returns a string in a single line with /n, loading and then dumping it will help to clear the JSON
    # Example output: b'{\n   "date": "06-28-2022",\n   "milliseconds_since_epoch": 1656429745740,\n   "time": "03:22:25 PM"\n}\n'



# type the name of the function that you want to run here
func9()